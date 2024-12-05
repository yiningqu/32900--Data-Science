"""
Thank you to Tobias Rodriguez del Pozo for his assistance in writing this code.
"""
import pandas as pd
import numpy as np
import config

OUTPUT_DIR = config.OUTPUT_DIR
DATA_DIR = config.DATA_DIR

import misc_tools
import load_CRSP_stock


def calc_equal_weighted_index(df):
    """
    Calculate equal weighted index (just the average of all stocks)
    Note that ret is raw and retx is adjusted for dividends.
    """   
    ewretd = df.groupby('date')['ret'].mean()
    ewretx = df.groupby('date')['retx'].mean()
    # Count the total number of stocks per date to include in the DataFrame
    totcnt = df.groupby('date')['permno'].count()

    # Compile the calculated values into a DataFrame
    df_eq_idx = pd.DataFrame({
        'ewretd': ewretd,
        'ewretx': ewretx,
        'totcnt': totcnt
    })

    return df_eq_idx





def calc_CRSP_value_weighted_index(df):
    """
    The formula is:
    $$
    r_t = \\frac{\\sum_{i=1}^{N_t} w_{i,t-1} r_{i,t}}{\\sum_{i=1}^{N_t} w_{i,t-1}}
    $$
    That is, the return of the index is the weighted average of the returns, where
    the weights are the market cap of the stock at the end of the previous month.
    """
    
    df['mktcap'] = df['shrout'] * df['altprc']
    df['shift_mktcap'] = df.groupby('permno')['mktcap'].shift(1)
    total_mktcap = df.groupby('date')['mktcap'].sum()
    df['weighted_ret'] = df['ret'] * df['shift_mktcap']
    df['weighted_ret'] = df['ret'] * df['shift_mktcap']
    vwretd = df.groupby('date')['weighted_ret'].sum() / total_mktcap.shift(1)
    df['weighted_retx'] = df['retx'] * df['shift_mktcap']
    vwretx = df.groupby('date')['weighted_retx'].sum() / total_mktcap.shift(1)
    df_vw_idx = pd.DataFrame({
        'vwretd': vwretd,
        'vwretx': vwretx,
        'totval': total_mktcap
    })
    df_vw_idx.dropna(subset=['vwretd', 'vwretx'], inplace=True)
    return df_vw_idx



def calc_CRSP_indices_merge(df_msf, df_msix):
    # Merge everything with appropriate suffixes
    df_vw_idx = calc_CRSP_value_weighted_index(df_msf)
    df_eq_idx = calc_equal_weighted_index(df_msf)
    df_msix = df_msix.rename(columns={"caldt": "date"})

    df = df_msix.merge(
        df_vw_idx.reset_index(),
        on="date",
        how="inner",
        suffixes=("", "_manual"),
    )
    df = df.merge(
        df_eq_idx.reset_index(),
        on="date",
        suffixes=("", "_manual"),
    )
    df = df.set_index("date")
    return df


def _demo():
    df_msf = load_CRSP_stock.load_CRSP_monthly_file(data_dir=DATA_DIR)
    df_msix = load_CRSP_stock.load_CRSP_index_files(data_dir=DATA_DIR)

    df_eq_idx = calc_equal_weighted_index(df_msf)
    df_vw_idx = calc_CRSP_value_weighted_index(df_msf)
    df_idxs = calc_CRSP_indices_merge(df_msf, df_msix)
    df_idxs.head()


if __name__ == "__main__":
    pass
