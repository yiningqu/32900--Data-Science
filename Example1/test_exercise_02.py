import numpy as np
import load_fred


## Setup Code for Exercises 2.1 and 2.2
series_to_pull = {
            'EFFR': 'Effective Federal Funds Rate', 
            'SOFR': 'SOFR',
        }
start_date = '2012-01-01'
end_date = '2024-04-01'
df = load_fred.pull_fred_repo_data(start_date, end_date, series_to_pull=series_to_pull)



def test_SOFR_rate_on_Sep_17_2019():
    """
    Exercise 2.1
    """

    assert df.loc['2019-09-17', 'SOFR'] == 5.25

def test_average_diff_SOFR_EFFR():
    """
    Exercise 2.2
    Calculate the average difference between SOFR and EFFR:
    Ave(EFFR - SOFR) = ?
    and report the answer in basis points.

    Only pull data between the following date range:
    start_date = '2012-01-01'
    end_date = '2024-04-01'
    Don't fill in missing values. Only compare values that are available for both series.
    """

    calculated_mean_diff = 100 * (df['EFFR'] - df['SOFR']).dropna().mean()
    actual_mean_diff = 0.8715277777777833
    # Assert that calculated_mean_diff is numerically close to 
    # actual_mean_diff. Allow for some user-specified rounding error,
    # within an absolute tolerance of 0.01.
    assert np.isclose(calculated_mean_diff, actual_mean_diff, atol=0.01)
