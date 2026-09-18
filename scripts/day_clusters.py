"""Daily-shape clusters per BA: groups, their calendar and regime, special days, and the most atypical days.

    python scripts/day_clusters.py --bas PJM MISO ... --start 2018-01-01 --end 2022-12-31

Writes ``results/day_clusters/<BA>_days.csv`` (one row per complete day: cluster, distance, day type,
special day, regime) and ``docs/day_clusters.md``.
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
from grid_sentinel.calendar_us import SATURDAY, SUNDAY, WORKDAY, day_types, special_days

from ba_load_forecast.clusters import LabelClassifier, crosstab, daily_shapes, fit_clusters
from ba_load_forecast.forecasters.profile import COOLING, HEATING, MILD, regime
from ba_load_forecast.information_set import Loader, gross_guard
from ba_load_forecast.report import markdown_table

ROOT = Path(__file__).resolve().parents[1]
DEV_BAS = ("PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT")
TYPE_NAMES = {WORKDAY: "workday", SATURDAY: "saturday", SUNDAY: "sunday"}
REGIME_NAMES = {HEATING: "heating", MILD: "mild", COOLING: "cooling"}
SPECIAL_NAMES = {
    (1, 1): "New Year's Day", (7, 4): "Independence Day", (12, 24): "Christmas Eve", (12, 25): "Christmas Day",
    (12, 31): "New Year's Eve",
}


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", flush=True)


MONTH_NAMES = {5: "Memorial Day", 9: "Labor Day", 2: "Super Bowl Sunday", 1: "New Year's Day (observed)",
               7: "observed holiday", 12: "observed holiday"}


def special_name(d: date, kinds: dict) -> str:
    if (d.month, d.day) in SPECIAL_NAMES:
        return SPECIAL_NAMES[(d.month, d.day)]
    if d.month == 11:
        return "Thanksgiving" if d.weekday() == 3 else "Day after Thanksgiving"
    return MONTH_NAMES.get(d.month, "special day")


def analyse_ba(loader: Loader, ba: str, start: date, end: date) -> tuple[pd.DataFrame, dict]:
    load = pd.concat([loader.load(ba, y) for y in range(start.year, end.year + 1)]).sort_index()
    load = load[~load.index.duplicated()].loc[str(start): f"{end} 23:00"]
    load = gross_guard(load)
    temp = pd.concat([loader.temperature(ba, y) for y in range(start.year, end.year + 1)]).sort_index()
    temp = temp[~temp.index.duplicated()]
    days, shapes = daily_shapes(load)
    types = day_types(days.to_numpy())
    daily_temp = temp.groupby(pd.DatetimeIndex(temp.index).normalize()).mean().reindex(days)
    regimes = np.array([regime(float(t)) if np.isfinite(t) else -1 for t in daily_temp.to_numpy()])
    # One clustering per temperature regime: across regimes the shape is the season (a heating day peaks in
    # the morning, a cooling day in the afternoon) and that would hide what a special day looks like. Within a
    # regime, the groups are what is left: weekday against weekend, and the odd day.
    labels = np.full(len(days), -1)
    dist = np.full(len(days), np.nan)
    models = {}
    offset = 0
    for r in (HEATING, MILD, COOLING):
        m = regimes == r
        if m.sum() < 30:
            continue
        model = fit_clusters(shapes[m], k_range=range(2, 6))
        labels[m] = model.label(shapes[m]) + offset
        dist[m] = model.distance(shapes[m])
        models[r] = (model, offset)
        offset += model.k
    keep = labels >= 0
    days, shapes, types, regimes, daily_temp = days[keep], shapes[keep], types[keep], regimes[keep], daily_temp[keep]
    labels, dist = labels[keep], dist[keep]
    model = type("Models", (), {})()
    model.k = offset
    model.silhouette = float(np.mean([mm.silhouette for mm, _ in models.values()]))
    model.centroids = np.vstack([mm.centroids for mm, _ in models.values()])
    model.regime_of_cluster = {o + j: r for r, (mm, o) in models.items() for j in range(mm.k)}
    kinds = {}
    for y in range(start.year, end.year + 1):
        kinds.update(special_days(y))
    special = [kinds.get(d.date()) for d in days]
    table = pd.DataFrame({
        "day": days.date, "cluster": labels, "distance": np.round(dist, 4), "day_type": types,
        "special_day": special, "regime": regimes, "mean_temp_f": np.round(daily_temp.to_numpy(), 1),
        "daily_mean_mw": np.round(load.groupby(pd.DatetimeIndex(load.index).normalize()).mean().reindex(days).to_numpy(), 0),
    })
    clf = LabelClassifier().fit(labels[regimes >= 0], types[regimes >= 0], regimes[regimes >= 0])
    predicted = np.array([clf.predict(t, r if r >= 0 else None) for t, r in zip(types, regimes, strict=True)])
    info = {"k": model.k, "silhouette": model.silhouette, "n_days": len(days),
            "classifier_accuracy": float((predicted == labels).mean()), "centroids": model.centroids,
            "regime_of_cluster": model.regime_of_cluster,
            "crosstab": crosstab(labels, types, regimes), "clf": clf, "kinds": kinds}
    return table, info


def special_table(table: pd.DataFrame, info: dict) -> pd.DataFrame:
    """Every special day: its cluster, and the cluster the calendar type and the weekday would have given."""
    rows = []
    majority = table.groupby("day_type")["cluster"].agg(lambda s: s.mode().iloc[0]).to_dict()
    for r in table[table["special_day"].notna()].itertuples(index=False):
        weekday_type = WORKDAY if r.day.weekday() < 5 else (SATURDAY if r.day.weekday() == 5 else SUNDAY)
        rows.append({"day": r.day, "name": special_name(r.day, info["kinds"]), "cluster": r.cluster,
                     "as_calendar_type": TYPE_NAMES[int(r.special_day)], "cluster_of_that_type": majority.get(int(r.special_day)),
                     "weekday_type": TYPE_NAMES[weekday_type], "cluster_of_weekday_type": majority.get(weekday_type),
                     "distance": r.distance})
    return pd.DataFrame(rows)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bas", nargs="+", default=list(DEV_BAS))
    ap.add_argument("--start", type=date.fromisoformat, default=date(2018, 1, 1))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2022, 12, 31))
    ap.add_argument("--tidy", type=Path, default=ROOT.parent / "ba-forecast-scorecard" / "data" / "tidy")
    ap.add_argument("--isd-dir", type=Path, default=ROOT.parent / "notes" / "03-daily-load-profiles" / "data" / "isd")
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "day_clusters")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "day_clusters.md")
    a = ap.parse_args(argv)
    a.out.mkdir(parents=True, exist_ok=True)
    loader = Loader(a.tidy, a.isd_dir, ROOT / "data" / "hrrr")

    lines = ["# Daily load shapes grouped by similarity", "",
             f"For each BA, every complete day from {a.start} to {a.end} (gross faults removed) is a shape: 24 hourly "
             "values divided by the day's mean. Days are first split by temperature regime (heating below 59 F, cooling "
             "above 72 F, mild between, by the observed daily mean), because across regimes the shape is the season: a "
             "heating day peaks in the morning, a cooling day in the afternoon. Within each regime k-means groups the "
             "shapes, k being the value between 2 and 5 with the best silhouette (the silhouette shown is the mean over "
             "regimes). The groups are crossed with the calendar day type (workday, Saturday, Sunday; holidays as the "
             "type they resemble in the Note 2 table). The classifier is the most frequent cluster of each (day type, "
             "regime) cell; its accuracy is the share of days whose cluster it names correctly. Distances are to the "
             "nearest centroid of the day's regime; the largest ones are the most atypical days.", ""]
    summary = []
    for ba in a.bas:
        t0 = time.time()
        table, info = analyse_ba(loader, ba, a.start, a.end)
        table.to_csv(a.out / f"{ba}_days.csv", index=False)
        sp = special_table(table, info)
        sp.to_csv(a.out / f"{ba}_special_days.csv", index=False)
        ct = info["crosstab"].copy()
        ct.columns = [f"{TYPE_NAMES.get(t, t)}/{REGIME_NAMES.get(r, 'no temp')}" for t, r in ct.columns]
        top = table.sort_values("distance", ascending=False).head(20)[["day", "cluster", "distance", "day_type", "regime", "daily_mean_mw"]]
        peak_hour = [int(np.argmax(c)) for c in info["centroids"]]
        centroids = pd.DataFrame({"cluster": range(info["k"]),
                                  "regime": [REGIME_NAMES[info["regime_of_cluster"][c]] for c in range(info["k"])],
                                  "peak_hour": peak_hour,
                                  "peak_to_mean": np.round(info["centroids"].max(axis=1), 3),
                                  "min_to_mean": np.round(info["centroids"].min(axis=1), 3),
                                  "n_days": np.bincount(table["cluster"], minlength=info["k"])})
        summary.append({"ba": ba, "k": info["k"], "silhouette": round(info["silhouette"], 3), "n_days": info["n_days"],
                        "classifier_accuracy": round(info["classifier_accuracy"], 3)})
        lines += [f"## {ba}", "", f"k = {info['k']}, silhouette {info['silhouette']:.3f}, {info['n_days']} days, "
                  f"classifier accuracy {info['classifier_accuracy']:.3f}.", "",
                  "### Clusters", "", markdown_table(centroids), "",
                  "### Days per cluster, by day type and regime", "", markdown_table(ct.reset_index()), "",
                  "### Special days", "", markdown_table(sp), "",
                  "### The 20 most atypical days", "", markdown_table(top), ""]
        log(f"{ba}: k={info['k']} silhouette={info['silhouette']:.3f} accuracy={info['classifier_accuracy']:.3f} in {time.time() - t0:.0f} s")
    lines.insert(3, markdown_table(pd.DataFrame(summary)) + "\n")
    a.doc.write_text("\n".join(lines), encoding="utf-8")
    pd.DataFrame(summary).to_csv(a.out / "summary.csv", index=False)
    log(f"written {a.doc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
