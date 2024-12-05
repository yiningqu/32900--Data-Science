"""
In normal circumstances, I would call this file "test_load_merged_repo_data.py"

Again, we'll let the unit tests specify the requirements of the
module in question. Here, that's the load_merged_repo_data module.

Please modify the load_fred file to complete this exercise.

"""
import numpy as np
import pandas as pd
import load_merged_repo_data


series_descriptions = load_merged_repo_data.series_descriptions

start_date = "2014-08-22"
end_date = "2024-01-03"
df = load_merged_repo_data.load_all(start_date=start_date, end_date=end_date)

def test_series_descriptions():
    """test_series_descriptions
    Test that you have created a dictionary that is available in the load_merged_repo_data module
    that provides a description of the series codes pulled by load_merged_repo_data.

    Do NOT hard code these into the module. That is, read the `series_description`
    variable in from each of load_fred and load_ofr_data_api and merge those two
    dictionaries to create the dictionary for this module. 
    """
    # fmt: off
    assert series_descriptions['DPCREDIT'] ==  'Discount Window Primary Credit Rate'
    assert series_descriptions['EFFR'] ==  'Effective Federal Funds Rate'
    assert series_descriptions['OBFR'] ==  'Overnight Bank Funding Rate'
    assert series_descriptions['SOFR'] ==  'SOFR'
    assert series_descriptions['IORR'] ==  'Interest on Required Reserves'
    assert series_descriptions['IOER'] ==  'Interest on Excess Reserves'
    assert series_descriptions['IORB'] ==  'Interest on Reserve Balances'
    assert series_descriptions['DFEDTARU'] ==  'Federal Funds Target Range - Upper Limit'
    assert series_descriptions['DFEDTARL'] ==  'Federal Funds Target Range - Lower Limit'
    assert series_descriptions['WALCL'] ==  'Federal Reserve Total Assets'
    assert series_descriptions['TOTRESNS'] ==  'Reserves of Depository Institutions: Total'
    assert series_descriptions['TREAST'] ==  'Treasuries Held by Federal Reserve'
    assert series_descriptions['CURRCIR'] ==  'Currency in Circulation'
    assert series_descriptions['GFDEBTN'] ==  'Federal Debt: Total Public Debt'
    assert series_descriptions['WTREGEN'] ==  'Treasury General Account'
    assert series_descriptions['RRPONTSYAWARD'] ==  'Fed ON/RRP Award Rate'
    assert series_descriptions['RRPONTSYD'] ==  'Treasuries Fed Sold In Temp Open Mark'
    assert series_descriptions['RPONTSYD'] ==  'Treasuries Fed Purchased In Temp Open Mark'
    assert series_descriptions['Gen_IORB'] ==  'Interest on Reserves'
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
    assert series_descriptions['FNYR-BGCR-A'] ==  'Broad General Collateral Rate'
    assert series_descriptions['FNYR-TGCR-A'] ==  'Tri-Party General Collateral Rate'
    # fmt: on

def test_load_all():
    """Test that variables are present from both data sources
    and that the values are correct.
    """
    assert np.isclose(df.loc['2019-08-16', 'REPO-TRI_AR_OO-P'], 2.13)
    assert np.isclose(df.loc['2019-09-16', 'REPO-TRI_AR_OO-P'], 2.44)
    assert np.isclose(df.loc['2019-09-17', 'REPO-TRI_AR_OO-P'], 5.04)
    assert np.isclose(df.loc['2019-09-18', 'REPO-TRI_AR_OO-P'], 2.57)

    assert np.isclose(df.loc['2019-09-17', 'SOFR'], 5.25)
    