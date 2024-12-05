import pandas_datareader.data as web
import pandas as pd
import numpy as np

series_to_pull = {
    'EFFR': 'Effective Federal Funds Rate', 
    'SOFR': 'SOFR',
}

def pull_fred_repo_data(start_date, end_date, series_to_pull):
    """
    Lookup series code, e.g., like this:
    https://fred.stlouisfed.org/series/RPONTSYD
    """
    df = web.DataReader(list(series_to_pull.keys()), 'fred', start_date, end_date)
    return df


def _setup():
    ## Setup Code for Exercises 2.1 and 2.2
    series_to_pull = {
                'EFFR': 'Effective Federal Funds Rate', 
                'SOFR': 'SOFR',
            }
    start_date = '2012-01-01'
    end_date = '2024-04-01'
    df = pull_fred_repo_data(start_date, end_date, series_to_pull=series_to_pull)





# def _demo():
#     start_date = '2012-01-01'
#     end_date = '2024-04-01'
    
#     series_to_pull = {
#         'EFFR': 'Effective Federal Funds Rate', 
#         'SOFR': 'SOFR',
#     }

#     df = pull_fred_repo_data(start_date, end_date, series_to_pull=series_to_pull)
#     100 * (df['EFFR'] - df['SOFR']).dropna().mean() # basis points
#     df.loc['2019-09-13', 'SOFR']
#     df.loc['2019-09-16', 'SOFR']
#     df.loc['2019-09-17', 'SOFR']
#     df.loc['2019-09-18', 'SOFR']


if __name__ == "__main__":
    pass
    
