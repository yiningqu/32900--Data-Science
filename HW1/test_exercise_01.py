"""
In normal circumstances, I would call this file "test_load_fred.py"

Here, we'll let the unit tests specify the requirements of the load_fred module.
We want to make sure that the pull_fred_repo_data function
pulls a number of data series related to repo markets from the FRED API.
We won't use all of the series in the immediate analysis, but we
want to make sure we collect a number of the important related
series. We'll also do a few transformations so that the imported
data is more useful for the charts we'd like to make.
These tests will specify those transformations and make
sure that they have been implemented correctly.

Please modify the load_fred file to complete this exercise.

"""
import numpy as np
import pandas as pd
import load_fred


series_descriptions = load_fred.series_descriptions

start_date = "2012-01-01"
end_date = "2024-01-03"
df = load_fred.pull_fred_repo_data(start_date, end_date)


def test_pull_fred_repo_data__transforms():
    """Create a longer, generalized time series for interest on reserve balances.
    Call this series "Gen_IORB"
    Let Gen_IORB be equal to interest on reserve balances (IORB). When this value is missing,
    fill it in with interest on excess reserves (IOER).
    """

    assert np.isclose(df.loc["2012-02-15", "Gen_IORB"], 0.25)
    assert np.isclose(df.loc["2021-02-15", "Gen_IORB"], 0.1)


def test_series_descriptions():
    """test_series_descriptions
    Test that you have created a dictionary that is available in the load_fred module
    that provides a description of the series codes pulled by load_fred.

    You should hard code these into the module. In this case, it's ok since this
    we're going to use this as part of the documentation of the module that
    we'll maintain ourselves.
    """
    # fmt: off
    assert series_descriptions['DPCREDIT'] == 'Discount Window Primary Credit Rate'
    assert series_descriptions['EFFR'] == 'Effective Federal Funds Rate'
    assert series_descriptions['OBFR'] == 'Overnight Bank Funding Rate'
    assert series_descriptions['SOFR'] == 'SOFR'
    assert series_descriptions['IORR'] == 'Interest on Required Reserves'
    assert series_descriptions['IOER'] == 'Interest on Excess Reserves'
    assert series_descriptions['IORB'] == 'Interest on Reserve Balances'
    assert series_descriptions['DFEDTARU'] == 'Federal Funds Target Range - Upper Limit'
    assert series_descriptions['DFEDTARL'] == 'Federal Funds Target Range - Lower Limit'
    assert series_descriptions['WALCL'] == 'Federal Reserve Total Assets'
    assert series_descriptions['TOTRESNS'] == 'Reserves of Depository Institutions: Total'
    assert series_descriptions['TREAST'] == 'Treasuries Held by Federal Reserve'
    assert series_descriptions['CURRCIR'] == 'Currency in Circulation'
    assert series_descriptions['GFDEBTN'] == 'Federal Debt: Total Public Debt'
    assert series_descriptions['WTREGEN'] == 'Treasury General Account'
    assert series_descriptions['RRPONTSYAWARD'] == 'Fed ON/RRP Award Rate'
    assert series_descriptions['RRPONTSYD'] == 'Treasuries Fed Sold In Temp Open Mark'
    assert series_descriptions['RPONTSYD'] == 'Treasuries Fed Purchased In Temp Open Mark'
    assert series_descriptions['Gen_IORB'] == 'Interest on Reserves'
    # fmt: on


def test_pull_fred_repo_data__shape():
    """ """
    assert df.shape[0] == 4386
    assert np.array_equal(
        df.columns.sort_values(),
        pd.Index(
            [
                "CURRCIR",
                "DFEDTARL",
                "DFEDTARU",
                "DPCREDIT",
                "EFFR",
                "GFDEBTN",
                "Gen_IORB",
                "IOER",
                "IORB",
                "IORR",
                "OBFR",
                "RPONTSYD",
                "RRPONTSYAWARD",
                "RRPONTSYD",
                "SOFR",
                "TOTRESNS",
                "TREAST",
                "WALCL",
                "WTREGEN",
            ],
            dtype="object",
        ),
    )

    assert df.index[0] == pd.Timestamp("2012-01-01 00:00:00")
    assert df.index[-1] == pd.Timestamp("2024-01-03 00:00:00")


def test_pull_fred_repo_data__nans():
    """ """
    ## Please apply a forward fill to the NaNs in the following series (for convenience)
    forward_fill = [
        "OBFR",
        "DPCREDIT",
        "TREAST",
        "TOTRESNS",
        "WTREGEN",
        "WALCL",
        "CURRCIR",
        "RRPONTSYAWARD",
    ]

    ## Please fill in the NaNs with zeros in the following series
    fill_zeros = ["RRPONTSYD", "RPONTSYD"]

    assert df.isna().sum().sum() == 16094
