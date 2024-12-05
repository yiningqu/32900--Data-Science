import pandas_datareader.data as web
import pandas as pd
import numpy as np

import os
from pathlib import Path
##########################################################
## Template
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
}


def pull_fred_repo_data(start_date, end_date, ffill=True):
    """
    Lookup series code, e.g., like this:
    https://fred.stlouisfed.org/series/RPONTSYD
    """
    df = web.DataReader(list(series_descriptions.keys()), 'fred', start_date, end_date)
    df['Gen_IORB'] = df['IORB'].fillna(df['IOER'])
    
    if ffill:
        forward_fill_series = [
            "OBFR", "DPCREDIT", "TREAST", "TOTRESNS", "WTREGEN", 
            "WALCL", "CURRCIR", "RRPONTSYAWARD"
        ]
        df[forward_fill_series] = df[forward_fill_series].ffill()
    
    fill_zeros = ["RRPONTSYD", "RPONTSYD"]
    df[fill_zeros] = df[fill_zeros].fillna(0)
    
    return df
