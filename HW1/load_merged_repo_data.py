import pandas as pd

import load_fred
import load_ofr_api_data

# ################################################
# ## Template
series_descriptions = {
    'DPCREDIT': 'Discount Window Primary Credit Rate',
    'EFFR': 'Effective Federal Funds Rate',
    'OBFR': 'Overnight Bank Funding Rate',
    'SOFR': 'SOFR',
    'IORR': 'Interest on Required Reserves',
    'IOER': 'Interest on Excess Reserves',
    'IORB': 'Interest on Reserve Balances',
    'DFEDTARU': 'Federal Funds Target Range - Upper Limit',
    'DFEDTARL': 'Federal Funds Target Range - Lower Limit',
    'WALCL': 'Federal Reserve Total Assets',
    'TOTRESNS': 'Reserves of Depository Institutions: Total',
    'TREAST': 'Treasuries Held by Federal Reserve',
    'CURRCIR': 'Currency in Circulation',
    'GFDEBTN': 'Federal Debt: Total Public Debt',
    'WTREGEN': 'Treasury General Account',
    'RRPONTSYAWARD': 'Fed ON/RRP Award Rate',
    'RRPONTSYD': 'Treasuries Fed Sold In Temp Open Mark',
    'RPONTSYD': 'Treasuries Fed Purchased In Temp Open Mark',
    'Gen_IORB': 'Interest on Reserves',
    'REPO-TRI_AR_OO-P': 'Tri-Party Average Rate: Overnight/Open (Preliminary)',
    'REPO-TRI_TV_OO-P': 'Tri-Party Transaction Volume: Overnight/Open (Preliminary)',
    'REPO-TRI_TV_TOT-P': 'Tri-Party Transaction Volume: Total (Preliminary)',
    'REPO-DVP_AR_OO-P': 'DVP Service Average Rate: Overnight/Open (Preliminary)',
    'REPO-DVP_TV_OO-P': 'DVP Service Transaction Volume: Overnight/Open (Preliminary)',
    'REPO-DVP_TV_TOT-P': 'DVP Service Transaction Volume: Total (Preliminary)',
    'REPO-DVP_OV_TOT-P': 'DVP Service Outstanding Volume: Total (Preliminary)',
    'REPO-GCF_AR_OO-P': 'GCF Repo Service Average Rate: Overnight/Open (Preliminary)',
    'REPO-GCF_TV_OO-P': 'GCF Repo Service Transaction Volume: Overnight/Open (Preliminary)',
    'REPO-GCF_TV_TOT-P': 'GCF Repo Service Transaction Volume: Total (Preliminary)',
    'FNYR-BGCR-A': 'Broad General Collateral Rate',
    'FNYR-TGCR-A': 'Tri-Party General Collateral Rate',
}


def load_all(start_date="2014-08-22", end_date="2024-01-03", normalize_timing=True):
    """Merge the data sets created in load_fred and load_ofr_api_data
    """    
    df_fred = load_fred.pull_fred_repo_data(start_date, end_date)
    df_ofr = load_ofr_api_data.pull_repo_data(start_date, end_date)
    
    df = pd.merge(df_fred, df_ofr, on='DATE', how='outer')

    # The following is useful for replication of the Kahn et al. (2023)
    if normalize_timing:
        # Normalize end-of-day vs start-of-day difference
        df.loc['2016-12-14', ['DFEDTARU', 'DFEDTARL']] = df.loc['2016-12-13', ['DFEDTARU', 'DFEDTARL']]
        df.loc['2015-12-16', ['DFEDTARU', 'DFEDTARL']] = df.loc['2015-12-15', ['DFEDTARU', 'DFEDTARL']]

    return df


