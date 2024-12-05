import pandas as pd
import load_fred

series_descriptions = load_fred.series_descriptions
start_date = '2000-01-01'
end_date = '2024-01-01'
df = load_fred.pull_all(start_date, end_date)

def test_pull_all():
    # Test if the function returns a DataFrame
    assert isinstance(df, pd.DataFrame)

def test_pull_all_date_range():
    # Test if the function returns data within the specified date range
    assert start_date <= df.index.min().strftime('%Y-%m-%d')
    assert end_date >= df.index.max().strftime('%Y-%m-%d')

def test_series_descriptions():
    """test_series_descriptions
    Test that you have created a dictionary that is available in the load_fred module
    that provides a description of the series codes pulled by load_fred.

    You should hard code these into the module. In this case, it's ok since this
    we're going to use this as part of the documentation of the module that
    we'll maintain ourselves.
    """
    # fmt: off
    assert series_descriptions['LES1252881600Q'] == 'Employed full time: Median usual weekly real earnings: Wage and salary workers: 16 years and over'
    assert series_descriptions['LES1252881900Q'] == 'Employed full time: Median usual weekly real earnings: Wage and salary workers: 16 years and over: Men'
    # fmt: on

def test_numbers():
    assert df.loc['2022-10-01', 'LES1252881600Q'] == 363
    assert df.loc['2022-10-01', 'LES1252881900Q'] == 394


