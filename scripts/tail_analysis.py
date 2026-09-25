"""Band and tail, apart: how often and by how much the outcome leaves the 90 % band, what the tail beyond the band
looks like, and how much of it falls on days when the ensemble members disagreed.

    python scripts/tail_analysis.py --group frozen4 --model final4 --runs ~/ba-load-forecast-runs/phase_e_ghcnh
                                    --out results/tail_analysis --doc docs/tail_analysis.md

Reads the hourly files (``<group>_<BA>_hourly.parquet``: actual, the model, its q05 and q95, the members) and the
daily files (for the scored days and the forecast minimum temperature). For every scored hour the relative error
``(actual - forecast) / actual`` and the relative excess beyond the band (``(lo - actual) / actual`` below,
``(actual - hi) / actual`` above; below is an over-forecast beyond the band, above an under-forecast). The band is judged by coverage and width; the tail by the exceedance rate per
side, the mean excess when the band is left, the worst case, and a generalized Pareto distribution fitted to the
excesses of each side (all BAs and years pooled in relative units, then by temperature regime), from which the
1st and 99th percentiles of the error and the expected shortfall follow. Member disagreement is the hourly spread
of the members relative to the outcome; the tail is attributed to the days in the top quartile of disagreement.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from ba_load_forecast.report import markdown_table

ROOT = Path(__file__).resolve().parents[1]
BAS = ["PJM", "MISO", "ERCO", "CISO", "SWPP", "NYIS", "ISNE", "TVA", "DUK", "BPAT", "FPL"]
HOURS = [f"h{i:02d}" for i in range(24)]
REGIMES = [("cold", -np.inf, 32.0), ("mild", 32.0, 72.0), ("hot", 72.0, np.inf)]     # forecast minimum temperature, F


def load_ba(runs: Path, group: str, model: str, ba: str) -> pd.DataFrame | None:
    daily = runs / f"{group}_{ba}.parquet"
    hourly = runs / f"{group}_{ba}_hourly.parquet"
    if not daily.exists() or not hourly.exists():
        return None
    d = pd.read_parquet(daily)
    d = d[(d["model"] == model) & ~d["skipped"].astype(bool) & d["error"].isna()][["day", "temp_min_f"]]
    h = pd.read_parquet(hourly)
    h = h[h["day"].isin(set(d["day"]))]
    wide = {m: h[h["model"] == m].set_index("day")[HOURS] for m in h["model"].unique()}
    need = ["actual", model, f"{model}_q05", f"{model}_q95"]
    if any(k not in wide for k in need):
        return None
    idx = wide["actual"].index
    for k in need:
        idx = idx.intersection(wide[k].index)
    members = [m for m in wide if m.startswith(model + "_") and not m.endswith(("_q05", "_q95", "_ensemble"))]
    rows = []
    a = wide["actual"].loc[idx].to_numpy(float)
    f = wide[model].loc[idx].to_numpy(float)
    lo = wide[f"{model}_q05"].loc[idx].to_numpy(float)
    hi = wide[f"{model}_q95"].loc[idx].to_numpy(float)
    mem = np.stack([wide[m].loc[idx].to_numpy(float) for m in members], axis=0) if members else None
    tmin = d.set_index("day")["temp_min_f"].reindex(idx).to_numpy(float)
    ok = np.isfinite(a) & (a > 0) & np.isfinite(f) & np.isfinite(lo) & np.isfinite(hi)
    day_idx = np.repeat(np.arange(len(idx)), 24).reshape(len(idx), 24)
    spread = ((np.nanmax(mem, axis=0) - np.nanmin(mem, axis=0)) / a) if mem is not None else np.full_like(a, np.nan)
    rows = pd.DataFrame({
        "ba": ba, "day": np.asarray(idx)[day_idx[ok]], "hour": np.tile(np.arange(24), (len(idx), 1))[ok],
        "temp_min_f": np.repeat(tmin, 24).reshape(len(idx), 24)[ok],
        "rel_err": ((a - f) / a)[ok], "below": ((lo - a) / a)[ok], "above": ((a - hi) / a)[ok],
        "width": ((hi - lo) / a)[ok], "spread": spread[ok],
    })
    return rows


def regime_of(t: np.ndarray) -> np.ndarray:
    out = np.full(len(t), "mild", dtype=object)
    for name, lo, hi in REGIMES:
        out[(t >= lo) & (t < hi)] = name
    return out


def gpd_fit(excess: np.ndarray) -> dict:
    """Shape, scale and the implied tail quantiles of a generalized Pareto fitted to positive excesses (relative)."""
    x = excess[excess > 0]
    if len(x) < 50:
        return {"n_excess": len(x), "shape": np.nan, "scale": np.nan}
    shape, _, scale = stats.genpareto.fit(x, floc=0.0)
    return {"n_excess": len(x), "shape": float(shape), "scale": float(scale),
            "mean_excess": float(x.mean()), "p90_excess": float(np.quantile(x, 0.9)),
            "gpd_p80_excess": float(stats.genpareto.ppf(0.8, shape, loc=0, scale=scale)),
            "gpd_expected_shortfall": float(stats.genpareto.mean(shape, loc=0, scale=scale)) if shape < 1 else np.inf}


def tail_side(df: pd.DataFrame, side: str) -> dict:
    """Exceedance rate, mean excess, worst case and the GPD of one side (``below`` or ``above``)."""
    e = df[side].to_numpy(float)
    out = {"hours": len(e), "exceed_rate_pct": float((e > 0).mean() * 100.0),
           "mean_excess_pct": float(e[e > 0].mean() * 100.0) if (e > 0).any() else 0.0,
           "worst_pct": float(e.max() * 100.0)}
    g = gpd_fit(e)
    out.update({k: (v * 100.0 if k in ("mean_excess", "p90_excess", "gpd_p80_excess", "gpd_expected_shortfall") and np.isfinite(v) else v)
                for k, v in g.items()})
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--group", default="frozen4")
    ap.add_argument("--model", default="final4")
    ap.add_argument("--runs", type=Path, default=Path.home() / "ba-load-forecast-runs" / "phase_e_ghcnh")
    ap.add_argument("--bas", nargs="+", default=BAS)
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "tail_analysis")
    ap.add_argument("--doc", type=Path, default=ROOT / "docs" / "tail_analysis.md")
    a = ap.parse_args(argv)
    parts = [load_ba(a.runs, a.group, a.model, ba) for ba in a.bas]
    parts = [p for p in parts if p is not None and len(p)]
    if not parts:
        print("no data")
        return 1
    d = pd.concat(parts, ignore_index=True)
    d["regime"] = regime_of(d["temp_min_f"].to_numpy(float))
    d["inside"] = (d["below"] <= 0) & (d["above"] <= 0)
    a.out.mkdir(parents=True, exist_ok=True)

    # the band
    band = d.groupby("ba").agg(hours=("inside", "size"), coverage_pct=("inside", lambda s: s.mean() * 100),
                               width_pct=("width", lambda s: s.mean() * 100),
                               below_pct=("below", lambda s: (s > 0).mean() * 100), above_pct=("above", lambda s: (s > 0).mean() * 100)).round(2)
    band.loc["ALL"] = [len(d), d["inside"].mean() * 100, d["width"].mean() * 100, (d["below"] > 0).mean() * 100, (d["above"] > 0).mean() * 100]
    band = band.round(2)

    # the tail, per side and regime (pooled BAs, relative units)
    tail_rows = []
    for regime in ["ALL", "cold", "mild", "hot"]:
        g = d if regime == "ALL" else d[d["regime"] == regime]
        for side in ["below", "above"]:
            r = tail_side(g, side)
            r.update({"regime": regime, "side": side})
            tail_rows.append(r)
    tail = pd.DataFrame(tail_rows).set_index(["regime", "side"]).round(3)

    # per BA: exceedance and mean excess per side, worst case
    per_ba = []
    for ba, g in d.groupby("ba"):
        r = {"ba": ba}
        for side in ["below", "above"]:
            e = g[side].to_numpy(float)
            r[f"{side}_rate_pct"] = (e > 0).mean() * 100
            r[f"{side}_mean_excess_pct"] = e[e > 0].mean() * 100 if (e > 0).any() else 0.0
            r[f"{side}_worst_pct"] = e.max() * 100
        per_ba.append(r)
    per_ba = pd.DataFrame(per_ba).set_index("ba").round(2)

    # attribution to member disagreement: top quartile of the daily mean spread
    daily_spread = d.groupby(["ba", "day"])["spread"].mean().rename("day_spread").reset_index()
    d = d.merge(daily_spread, on=["ba", "day"])
    q75 = d.groupby("ba")["day_spread"].transform(lambda s: s.quantile(0.75))
    d["disagree"] = d["day_spread"] >= q75
    attr = d.groupby("disagree").agg(hours=("inside", "size"), coverage_pct=("inside", lambda s: s.mean() * 100),
                                     exceed_below_pct=("below", lambda s: (s > 0).mean() * 100), exceed_above_pct=("above", lambda s: (s > 0).mean() * 100),
                                     mean_excess_below_pct=("below", lambda s: s[s > 0].mean() * 100 if (s > 0).any() else 0.0),
                                     mean_excess_above_pct=("above", lambda s: s[s > 0].mean() * 100 if (s > 0).any() else 0.0),
                                     width_pct=("width", lambda s: s.mean() * 100)).round(2)
    attr.index = ["members agree (bottom three quarters)", "members disagree (top quarter)"]
    share_exceed = float(d.loc[d["disagree"], ["below", "above"]].gt(0).any(axis=1).sum() / max(1, d[["below", "above"]].gt(0).any(axis=1).sum()) * 100)
    share_excess = float(d.loc[d["disagree"], ["below", "above"]].clip(lower=0).sum().sum() / max(1e-9, d[["below", "above"]].clip(lower=0).sum().sum()) * 100)

    for name, t in [("band_by_ba", band), ("tail_by_regime", tail), ("tail_by_ba", per_ba), ("attribution", attr)]:
        t.to_csv(a.out / f"{name}.csv")

    all_tail = tail.loc[("ALL", "below")], tail.loc[("ALL", "above")]
    lines = [
        f"# Band and tail, apart: `{a.model}` on the scored days of `{a.group}`",
        "",
        f"{len(d)} scored hours at {d['ba'].nunique()} BAs. Relative error `(actual - forecast) / actual`; the band is the 90 % "
        "interval (percentiles 5 and 95 of the errors of the 40 known days nearest in forecast minimum temperature, with the "
        "adaptive level). Below: the outcome under the lower bound (the forecast band was too high, an over-forecast beyond the band); above: the outcome over the upper bound (an under-forecast beyond the band). Excesses are in "
        "percent of the outcome. Regimes by forecast minimum temperature: cold below 32 F, hot 72 F and above.",
        "",
        "## The band",
        "",
        f"Coverage {band.loc['ALL', 'coverage_pct']:.1f} % (target 90), width {band.loc['ALL', 'width_pct']:.1f} % of the outcome; "
        f"the outcome leaves the band below on {band.loc['ALL', 'below_pct']:.1f} % of the hours and above on "
        f"{band.loc['ALL', 'above_pct']:.1f} % (5 % each side would be exact).",
        "",
        markdown_table(band, 2),
        "",
        "## The tail",
        "",
        f"When the band is left below, the outcome is on average {all_tail[0]['mean_excess_pct']:.2f} % of itself under the lower "
        f"bound (worst {all_tail[0]['worst_pct']:.1f} %); above, {all_tail[1]['mean_excess_pct']:.2f} % over the upper bound "
        f"(worst {all_tail[1]['worst_pct']:.1f} %). A generalized Pareto distribution fitted to the excesses gives shape "
        f"{all_tail[0]['shape']:.2f} below and {all_tail[1]['shape']:.2f} above (a positive shape is a heavy tail; the expected "
        "shortfall is finite only below 1). `p90_excess` is the 90th percentile of the observed excesses, `gpd_p80_excess` the "
        "80th percentile implied by the fit, both in percent of the outcome.",
        "",
        markdown_table(tail, 3),
        "",
        "### By BA",
        "",
        markdown_table(per_ba, 2),
        "",
        "## Attribution to member disagreement",
        "",
        "Days are split by the daily mean spread of the ensemble members (maximum minus minimum member, relative to the outcome): "
        "the top quarter of days per BA against the rest. A tail that concentrates on days of disagreement is one the model "
        "itself signals in advance; one that does not is invisible from the members.",
        "",
        markdown_table(attr, 2),
        "",
        f"Share of the hours outside the band that fall on days of disagreement: {share_exceed:.1f} % (a quarter would be no "
        f"signal); share of the total excess beyond the band on those days: {share_excess:.1f} %.",
        "",
        "Tables as CSV in `results/tail_analysis/`.",
        "",
    ]
    a.doc.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[6:10]))
    print(f"disagreement share of exceedance hours {share_exceed:.1f} %, of excess {share_excess:.1f} %")
    print(f"written {a.doc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
