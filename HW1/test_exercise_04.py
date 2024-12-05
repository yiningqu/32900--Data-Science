"""
In this analysis, we'll do some analysis of repo
spikes.
"""
import repo_analytics
import pandas as pd
import numpy as np


def test_kahn_et_al_2023_figure_1():
    """In this test, you will create a chart that replicates
    Figure 1 from Kahn et al. (2023).

    Here, simply indicate whether you were able to
    replicate the chart
    https://elischolar.library.yale.edu/journal-of-financial-crises/vol5/iss4/1/
    It doesn't have to be perfect. As long as you believe it's close
    enough.
    """
    assert repo_analytics.i_replicated_figure_1


def test_spike_days():
    """Here, you'll create a list of the days in which the triparty repo
    rate spiked. We'll define a spike as a day in which the triparty repo rate
    as defined by the series "REPO-TRI_AR_OO-P" exceeded the upper limit
    of the Fed's policy rate target range (look for the right FRED series
    for this).

    Calculate the number of times there was a spike between the dates
    start_date = "2014-08-22"
    end_date = "2024-01-03"
    (at least those that you can observe in the data)
    """
    expected_spike_dates = pd.DatetimeIndex(
        [
            "2018-03-29",
            "2018-04-02",
            "2018-04-03",
            "2018-05-31",
            "2018-06-01",
            "2018-06-04",
            "2018-06-29",
            "2018-11-15",
            "2018-11-30",
            "2018-12-06",
            "2018-12-07",
            "2018-12-17",
            "2018-12-18",
            "2018-12-19",
            "2018-12-31",
            "2019-01-02",
            "2019-01-03",
            "2019-01-31",
            "2019-02-28",
            "2019-03-29",
            "2019-04-30",
            "2019-05-01",
            "2019-07-03",
            "2019-07-05",
            "2019-07-31",
            "2019-09-16",
            "2019-09-17",
            "2019-09-18",
            "2019-09-30",
            "2019-10-16",
            "2020-03-04",
            "2020-03-16",
            "2020-03-17",
        ]
    )

    assert np.array_equal(repo_analytics.spike_dates, expected_spike_dates)
