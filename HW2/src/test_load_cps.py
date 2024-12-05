import pandas as pd
import numpy as np

import config

DATA_DIR = config.DATA_DIR

import load_cps

df_raw = load_cps.load_raw(DATA_DIR, start_date="2000-01-01", end_date="2024-01-01")
df = load_cps.load_clean(DATA_DIR, start_date="2000-01-01", end_date="2024-01-01")


def test_df_raw_columns():
    expected_columns = [
        "YEAR",
        "GQ",
        "CPI99",
        "CPSIDV",
        "ASECWT",
        "AGE",
        "SEX",
        "LABFORCE",
        "EDUC",
        "WKSWORK1",
        "UHRSWORKLY",
        "INCWAGE",
    ]
    expected_dtypes = [
        np.dtype("datetime64[ns]"),
        "category",
        np.dtype("float64"),
        np.dtype("int64"),
        np.dtype("float64"),
        np.dtype("int64"),
        "category",
        "category",
        "category",
        np.dtype("int64"),
        np.dtype("int64"),
        np.dtype("int64"),
    ]

    assert df_raw.columns.tolist() == expected_columns
    assert df_raw.dtypes.tolist() == expected_dtypes


def test_df_missing_values():
    expected_missing_values = {
        "YEAR": 0,
        "GQ": 0,
        "CPI99": 0,
        "CPSIDV": 0,
        "ASECWT": 0,
        "AGE": 0,
        "SEX": 0,
        "LABFORCE": 1094719,
        "EDUC": 1079107,
        "WKSWORK1": 0,
        "UHRSWORKLY": 2268966,
        "INCWAGE": 0,
    }

    missing_values = df.isna().sum().to_dict()

    assert missing_values == expected_missing_values
