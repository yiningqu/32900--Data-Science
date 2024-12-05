"""
In normal circumstances, I would call this file "test_load_ofr_api_data.py"

Again, we'll let the unit tests specify the requirements of the
module in question. Here, that's the load_ofr_api_data module.

Please modify the load_fred file to complete this exercise.

"""
import numpy as np
import pandas as pd
import load_ofr_api_data


series_descriptions = load_ofr_api_data.series_descriptions

start_date = "2014-08-22"
end_date = "2024-01-03"
df = load_ofr_api_data.pull_repo_data(start_date, end_date)


def test_series_from_ofr_api():
    """Here, let's test a function that we've created to pull a single
    series from the OFR data API. We'll then loop over this function
    to pull the full set of series.
    """
    dfs = load_ofr_api_data.pull_variable_from_ofr_api(mnemonic="REPO-TRI_AR_OO-P")
    assert np.isclose(dfs.loc["2014-08-28", "REPO-TRI_AR_OO-P"], 0.07)
    dfs = load_ofr_api_data.pull_variable_from_ofr_api(mnemonic="FNYR-BGCR-A")
    assert np.isclose(dfs.loc["2020-03-13", "FNYR-BGCR-A"], 1.08)


def test_series_descriptions():
    """test_series_descriptions
    Test that you have created a dictionary that is available in the load_ofr_api_data module
    that provides a description of the series codes pulled by load_ofr_api_data.

    You should hard code these into the module. In this case, it's ok since this
    we're going to use this as part of the documentation of the module that
    we'll maintain ourselves.
    """
    # fmt: off
    assert series_descriptions['REPO-TRI_AR_OO-P'] ==  'Tri-Party Average Rate: Overnight/Open (Preliminary)'
    assert series_descriptions['REPO-TRI_TV_OO-P'] ==  'Tri-Party Transaction Volume: Overnight/Open (Preliminary)'
    assert series_descriptions['REPO-TRI_TV_TOT-P'] ==  'Tri-Party Transaction Volume: Total (Preliminary)'
    assert series_descriptions['REPO-DVP_AR_OO-P'] ==  'DVP Service Average Rate: Overnight/Open (Preliminary)'
    assert series_descriptions['REPO-DVP_TV_OO-P'] ==  'DVP Service Transaction Volume: Overnight/Open (Preliminary)'
    assert series_descriptions['REPO-DVP_TV_TOT-P'] ==  'DVP Service Transaction Volume: Total (Preliminary)'  
    assert series_descriptions['REPO-DVP_OV_TOT-P'] ==  'DVP Service Outstanding Volume: Total (Preliminary)'
    assert series_descriptions['REPO-GCF_AR_OO-P'] ==  'GCF Repo Service Average Rate: Overnight/Open (Preliminary)'
    assert series_descriptions['REPO-GCF_TV_OO-P'] ==  'GCF Repo Service Transaction Volume: Overnight/Open (Preliminary)'
    assert series_descriptions['REPO-GCF_TV_TOT-P'] ==  'GCF Repo Service Transaction Volume: Total (Preliminary)'
    assert series_descriptions['FNYR-BGCR-A'] == 'Broad General Collateral Rate'
    assert series_descriptions['FNYR-TGCR-A'] == 'Tri-Party General Collateral Rate'
    # fmt: on


def test_pull_repo_data__shape():
    """The OFR api will give you the full series. Use the start_date
    and end_date arguments to truncate the dataframe after the data pulls
    and data merges of the individual series.
    """
    assert df.shape[0] == 2322
    assert np.array_equal(
        df.columns.sort_values(),
        pd.Index(
            [
                "FNYR-BGCR-A",
                "FNYR-TGCR-A",
                "REPO-DVP_AR_OO-P",
                "REPO-DVP_OV_TOT-P",
                "REPO-DVP_TV_OO-P",
                "REPO-DVP_TV_TOT-P",
                "REPO-GCF_AR_OO-P",
                "REPO-GCF_TV_OO-P",
                "REPO-GCF_TV_TOT-P",
                "REPO-TRI_AR_OO-P",
                "REPO-TRI_TV_OO-P",
                "REPO-TRI_TV_TOT-P",
            ],
            dtype="object",
        ),
    )

    assert df.index[0] == pd.Timestamp(start_date)
    assert df.index[-1] == pd.Timestamp(end_date)
    assert np.isclose(df.loc[end_date, "REPO-DVP_AR_OO-P"], 5.41)
