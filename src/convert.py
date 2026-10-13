"""Convert downloaded MEPS files to Parquet with lower-case column names.

Usage:
    python -m src.convert --raw data/raw --out data/processed [--force]

Input layout:  data/raw/<year>/<file>.{csv,dta,sas7bdat,xpt}
Output layout: data/processed/<year>/<file>.parquet

Values are not recoded here. MEPS uses negative codes for missing / inapplicable answers; those are
handled later, per variable, after reading the codebook.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

SUPPORTED = {".csv", ".dta", ".sas7bdat", ".xpt"}


def read_any(path: Path):
    """Read one data file into a DataFrame, based on its extension."""
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path, low_memory=False)
    if suffix == ".dta":
        return pd.read_stata(path, convert_categoricals=False)
    if suffix == ".sas7bdat":
        return pd.read_sas(path, format="sas7bdat", encoding="latin-1")
    if suffix == ".xpt":
        return pd.read_sas(path, format="xport", encoding="latin-1")
    raise ValueError(f"Unsupported file type: {path.name} (supported: {sorted(SUPPORTED)})")


def normalise_columns(df: pd.DataFrame)
    """Strip and lower-case column names; refuse to silently merge columns that collide."""
    out = df.copy()
    out.columns = [str(c).strip().lower() for c in out.columns]
    dupes = sorted({c for c in out.columns if list(out.columns).count(c) > 1})
    if dupes:
        raise ValueError(f"Column names collide after lower-casing: {dupes}")
    return out


def output_path(src: Path, raw_root: Path, out_root: Path):
    """data/raw/<year>/<name>.<ext>  ->  data/processed/<year>/<name>.parquet"""
    rel = src.relative_to(raw_root)
    return (out_root / rel).with_suffix(".parquet")


def convert_file(src: Path, dst: Path):
    """Convert one file; returns the number of rows written."""
    df = normalise_columns(read_any(src))
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        df.to_parquet(dst, index=False)
    except ImportError as exc:
        raise SystemExit(
            "Writing Parquet needs pyarrow (pip install pyarrow). Original error: " + str(exc)
        ) from exc
    return len(df)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--raw", type=Path, default=Path("data/raw"))
    parser.add_argument("--out", type=Path, default=Path("data/processed"))
    parser.add_argument("--force", action="store_true", help="overwrite existing Parquet files")
    args = parser.parse_args()

    files = sorted(p for p in args.raw.rglob("*") if p.suffix.lower() in SUPPORTED)
    if not files:
        print(f"No supported files found under {args.raw}. See data/README.md.", file=sys.stderr)
        raise SystemExit(1)

    for src in files:
        dst = output_path(src, args.raw, args.out)
        if dst.exists() and not args.force:
            print(f"skip   {src}")
            continue
        n = convert_file(src, dst)
        print(f"wrote  {dst}  ({n} rows)")


if __name__ == "__main__":
    main()
