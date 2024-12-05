"""
Pull from the short-term funding API
Info here:
https://www.financialresearch.gov/short-term-funding-monitor/api/
"""
import pandas as pd
import numpy as np
import requests

##########################################################
## Template
series_descriptions = {
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
    'FNYR-TGCR-A': 'Tri-Party General Collateral Rate'
}


def pull_variable_from_ofr_api(mnemonic=None):
    """
    An example:
    https://data.financialresearch.gov/v1/series/timeseries?mnemonic=REPO-TRI_AR_TOT-F
    """
    url = f"https://data.financialresearch.gov/v1/series/timeseries?mnemonic={mnemonic}"
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data, columns=['DATE', mnemonic])
    df['DATE'] = pd.to_datetime(df['DATE'])
    df.set_index('DATE', inplace=True)
    return df


def pull_repo_data(start_date, end_date, series_list = list(series_descriptions.keys())):
    all_data = []

    for mnemonic in series_list:
        series_df = pull_variable_from_ofr_api(mnemonic)
        all_data.append(series_df)

    df = pd.concat(all_data, axis=1)
    df = df.loc[start_date:end_date]
    
    return df

