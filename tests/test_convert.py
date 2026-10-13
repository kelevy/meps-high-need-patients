"""Tests for src/convert.py. Run with `pytest`, or `python tests/test_convert.py` without pytest."""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.convert import normalise_columns, output_path, read_any  # noqa: E402


def test_csv_columns_are_lowercased():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "x.csv"
        pd.DataFrame({"DUPERSID": ["1", "2"], " TOTEXP22 ": [0, 5]}).to_csv(p, index=False)
        df = normalise_columns(read_any(p))
    assert list(df.columns) == ["dupersid", "totexp22"]
    assert len(df) == 2


def test_stata_roundtrip():
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "x.dta"
        pd.DataFrame({"ERTOT": [0, 2], "AGE": [31, 64]}).to_stata(p, write_index=False)
        df = normalise_columns(read_any(p))
    assert list(df.columns) == ["ertot", "age"]
    assert df["ertot"].tolist() == [0, 2]


def test_colliding_names_are_rejected():
    df = pd.DataFrame({"A": [1], "a": [2]})
    try:
        normalise_columns(df)
    except ValueError as exc:
        assert "collide" in str(exc)
    else:
        raise AssertionError("expected ValueError")


def test_unsupported_extension_is_rejected():
    try:
        read_any(Path("thing.txt"))
    except ValueError as exc:
        assert "Unsupported" in str(exc)
    else:
        raise AssertionError("expected ValueError")


def test_output_path_mirrors_layout():
    out = output_path(Path("data/raw/2022/h233.dta"), Path("data/raw"), Path("data/processed"))
    assert out == Path("data/processed/2022/h233.parquet")


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print("ok  ", t.__name__)
    print(f"{len(tests)} passed")
