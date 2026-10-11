"""How far the band's edges are from the levels they are scored at, from the hourly outputs of run groups.

    python scripts/check_quantile_labels.py --models frozen8@<folder>:final8q frozen10sa@<folder>:final10s \
        --bas PJM MISO SWPP DUK TVA FPL ERCO CISO NYIS ISNE BPAT

``AdaptiveIntervals`` reads the band at the adaptive levels ``alpha/2`` and ``1 - alpha/2`` and the extra quantiles at
their fixed levels; the evaluation scores the band's edges as the 0.05 and 0.95 quantiles. For each model this prints
the share of hours on which the edge labelled 0.95 sits above the fixed 0.98 quantile (and 0.05 below 0.02), and the
CRPS of the issued set as scored against the CRPS with 0.05 and 0.95 interpolated between the fixed 0.02/0.10 and
0.90/0.98: over all scored days and on the event days of ``grid_sentinel.events``, demand-weighted over the BAs as in
``compare_events.py``. Only the days the run scored (a CRPS in its daily rows) are counted.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from grid_sentinel.events import EVENTS

HOURS = [f"h{i:02d}" for i in range(24)]
EXTRA = (0.01, 0.02, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90,
         0.98, 0.99)
LEVELS = np.array([*EXTRA, 0.05, 0.5, 0.95])
ORDER = np.argsort(LEVELS)
I02, I10, I90, I98 = EXTRA.index(0.02), EXTRA.index(0.10), EXTRA.index(0.90), EXTRA.index(0.98)


def parse_spec(spec: str) -> tuple[str, Path, str]:
    """``group@folder:model`` -> (group, folder, model)."""
    group, rest = spec.split("@", 1)
    folder, model = rest.rsplit(":", 1)
    return group, Path(folder), model


def crps(q: np.ndarray, a: np.ndarray) -> float:
    """Twice the mean pinball loss over the 23 levels, in percent of the actual (as ``metrics.crps_from_quantiles``)."""
    q, lv = q[ORDER], LEVELS[ORDER]
    ok = np.isfinite(a) & (a > 0)
    diff = a[None, ok] - q[:, ok]
    loss = np.maximum(lv[:, None] * diff, (lv[:, None] - 1.0) * diff)
    return float(2.0 * np.mean(loss / a[None, ok]) * 100.0)


def ba_rows(group: str, folder: Path, model: str, ba: str) -> pd.DataFrame | None:
    daily_f, hourly_f = folder / f"{group}_{ba}.parquet", folder / f"{group}_{ba}_hourly.parquet"
    if not daily_f.exists() or not hourly_f.exists():
        return None
    daily = pd.read_parquet(daily_f)
    scored = daily[(daily["model"] == model) & daily["crps"].notna()].set_index("day")
    w = {m: g.set_index("day")[HOURS] for m, g in pd.read_parquet(hourly_f).groupby("model")}
    names = [f"{model}_q{round(lv * 100):02d}" for lv in EXTRA]
    if any(n not in w for n in [*names, f"{model}_q05", f"{model}_q95", model, "actual"]):
        return None
    event_days = {d for ev in EVENTS for d in pd.date_range(ev["start"], ev["end"]).date}
    rows = []
    for day in scored.index:
        try:
            qx = np.array([w[n].loc[day].to_numpy(float) for n in names])
            q05, q50, q95 = (w[f"{model}_q05"].loc[day].to_numpy(float), w[model].loc[day].to_numpy(float),
                             w[f"{model}_q95"].loc[day].to_numpy(float))
            a = w["actual"].loc[day].to_numpy(float)
        except KeyError:
            continue
        q05i = qx[I02] + (qx[I10] - qx[I02]) * (0.05 - 0.02) / (0.10 - 0.02)
        q95i = qx[I90] + (qx[I98] - qx[I90]) * (0.95 - 0.90) / (0.98 - 0.90)
        rows.append({"ba": ba, "day": day, "event": pd.Timestamp(day).date() in event_days,
                     "demand": float(scored.at[day, "actual_mean"]),
                     "up": float(np.mean(q95 > qx[I98])), "down": float(np.mean(q05 < qx[I02])),
                     "crps_scored": crps(np.vstack([qx, q05, q50, q95]), a),
                     "crps_interp": crps(np.vstack([qx, q05i, q50, q95i]), a)})
    return pd.DataFrame(rows)


def weighted(t: pd.DataFrame, col: str) -> float:
    g = t.groupby("ba").agg(v=(col, "mean"), w=("demand", "mean"))
    return float(np.average(g["v"], weights=g["w"]))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+", required=True, help="group@folder:model")
    ap.add_argument("--bas", nargs="+", required=True)
    a = ap.parse_args(argv)
    for spec in a.models:
        group, folder, model = parse_spec(spec)
        parts = [r for ba in a.bas if (r := ba_rows(group, folder, model, ba)) is not None and len(r)]
        if not parts:
            print(f"{group}:{model}: no rows")
            continue
        t = pd.concat(parts)
        ev = t[t["event"]]
        print(f"{group}:{model} ({t['ba'].nunique()} BAs, {len(t)} BA-days): hours with q95 > q98 {100 * t['up'].mean():.1f} %, "
              f"q05 < q02 {100 * t['down'].mean():.1f} %; CRPS as scored / interpolated: all days "
              f"{weighted(t, 'crps_scored'):.3f} / {weighted(t, 'crps_interp'):.3f}, event days "
              + (f"{weighted(ev, 'crps_scored'):.3f} / {weighted(ev, 'crps_interp'):.3f} ({len(ev)} BA-days)" if len(ev) else "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
