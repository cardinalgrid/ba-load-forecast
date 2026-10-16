"""Score the test on January to September 2026 exactly as fixed in ``docs/test_2026_protocol.md``.

    python scripts/test_2026.py --runs <folder of the t2026 run>

The run (``run_phase_e.py --groups t2026 --start 2025-01-01 --end 2026-09-30``) forecasts 2025 as a warm-up; this script
keeps only the scored period, writes the daily rows of every BA to ``results/test_2026/`` (``rows.parquet`` and one file
per BA under ``scored/``) and produces the three reports of the protocol from the scripts used for 2023 to 2025:

1. the scoreboard against each BA's ``DF`` (``scoreboard_43.py``): ``docs/test_2026_scoreboard.md`` and its figure;
2. the strata on the 38 comparable BAs (``compare_events.py``): ``docs/test_2026_strata.md``;
3. the same strata on the eleven development BAs: ``docs/test_2026_strata_dev.md``.

Nothing here chooses or tunes anything: the model, the BAs, the period and the strata are those of the protocol.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import compare_events  # noqa: E402
import figure_station_map  # noqa: E402
import scoreboard_43  # noqa: E402

GROUP, MODEL = "t2026", "recipe2026"
BAS_43 = tuple(figure_station_map.BAS_43)              # the 43 BAs of the station map


def scored_rows(runs: Path, out: Path, start: date, end: date) -> pd.DataFrame:
    """The daily rows of every BA within [start, end], one file per BA under ``out/scored`` and all together."""
    (out / "scored").mkdir(parents=True, exist_ok=True)
    parts = []
    for ba in BAS_43:
        f = runs / f"{GROUP}_{ba}.parquet"
        if not f.exists():
            print(f"{ba}: no run file")
            continue
        d = pd.read_parquet(f)
        day = pd.to_datetime(d["day"])
        d = d[(day >= pd.Timestamp(start)) & (day <= pd.Timestamp(end))]
        d.to_parquet(out / "scored" / f.name, index=False)
        parts.append(d)
    rows = pd.concat(parts, ignore_index=True)
    rows.to_parquet(out / "rows.parquet", index=False)
    return rows


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", type=Path, required=True)
    ap.add_argument("--start", type=date.fromisoformat, default=date(2026, 1, 1))
    ap.add_argument("--end", type=date.fromisoformat, default=date(2026, 9, 30))
    ap.add_argument("--results", type=Path, default=ROOT / "results" / "test_2026")
    ap.add_argument("--docs", type=Path, default=ROOT / "docs")
    a = ap.parse_args(argv)
    rows = scored_rows(a.runs, a.results, a.start, a.end)
    print(f"{rows['ba'].nunique()} BAs, {rows['day'].min()} to {rows['day'].max()}")
    scoreboard_43.main(["--results", str(a.results), "--model", MODEL, "--doc", str(a.docs / "test_2026_scoreboard.md"),
                        "--fig", str(a.docs / "figures" / "test_2026_scoreboard"), "--period", "January to September 2026",
                        "--source", "the test on 2026 (`run_phase_e.py --groups t2026`, run from 2025-01-01 to 2026-09-30, "
                                    "scored from 2026-01-01; 9 a.m. cut-off, protocol v2; `docs/test_2026_protocol.md`)"])
    comparable = [b for b in BAS_43 if b not in scoreboard_43.NOT_COMPARABLE]
    spec, ref = f"{GROUP}@{a.results / 'scored'}:{MODEL}", f"{GROUP}@{a.results / 'scored'}:DF"
    compare_events.main(["--candidate", spec, "--reference", ref, "--bas", *comparable,
                         "--doc", str(a.docs / "test_2026_strata.md")])
    compare_events.main(["--candidate", spec, "--reference", ref, "--bas", *scoreboard_43.DEV_BAS,
                         "--doc", str(a.docs / "test_2026_strata_dev.md")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
