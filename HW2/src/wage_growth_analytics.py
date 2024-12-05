import pandas as pd
import numpy as np
import weightedstats

import config
DATA_DIR = config.DATA_DIR

import load_cps

def s04_subsample(df):
    df = df[(df['AGE'] >= 25) & (df['AGE'] <= 54)]
    df = df[df['SEX'] == 1]
    df = df[df['GQ'] != 2]
    df = df[df['INCWAGE'] > 0]
    return df


def s05_new_vars(df):
    df['real_incwage'] = df['CPI99'] * df['INCWAGE']
    df['annual_hours'] = df['WKSWORK1'] * df['UHRSWORKLY']
    df['real_wage'] = df['INCWAGE'] / df['annual_hours'] * df['CPI99']
    df['in_labor_force'] = np.where(df['LABFORCE']==2, True, False)
    df.loc[df['annual_hours'] <= 0, 'real_wage'] = 0
    
    return df


def s06_drop(df):
    labels = ['GQ', 'SEX', 'LABFORCE', 'CPI99', 'INCTOT', 'WKSWORK1', ]
    for label in labels:
        try:
            df.drop(labels=label, inplace=True, axis=1)
        except:
            pass
    df = df.dropna()
    return df


def s10_drop_by_percentiles(df):
    q01 = df['real_wage'].quantile(q=0.01)
    q99 = df['real_wage'].quantile(q=0.99)
    mask = (df['real_wage'] > q01) & (df['real_wage'] < q99)
    df = df[mask]
    return df



def s11_median_wages(df):
    col = 'real_wage'
    weights='ASECWT'

    median_wages = (
        df
        .dropna(subset=[col], how='any')
        .groupby('YEAR')
        .apply(lambda row: weightedstats.weighted_median(row[col], weights=row[weights]))
        # Shift time back since the series represents wages from the previous year
        .shift(-1) 
    )
    return median_wages


def s11_ave_wages(df):
    col = 'real_wage'
    weights = 'ASECWT'

    ave_wages = (
        df
        .dropna(subset=[col], how='any')
        .groupby('YEAR')
        .apply(lambda row: np.average(row[col], weights=row[weights]))
        .shift(-1) 
    )
    return ave_wages


def s11_employment(df):
    col_employed = 'in_labor_force'
    weights = 'ASECWT'

    employment = (
        df
        .dropna(subset=[col_employed, weights], how='any')
        .groupby('YEAR')
        .apply(lambda x: np.average(x[col_employed], weights=x[weights]))
    )
    return employment


def s12_time_series(df):
    median_wages = s11_median_wages(df)
    ave_wages = s11_ave_wages(df)
    employment = s11_employment(df)
    tdf = pd.concat([ave_wages, median_wages, employment], axis=1)
    tdf.columns = ['ave_wages', 'median_wages', 'employment']
    return tdf


def s20_bin_vars(df):
    bins = [25, 30, 35, 40, 45, 50, 55]
    df['age_binned'] = pd.cut(df['AGE'], bins=bins, include_lowest=True, right=False)

    educ_bins = [0, 72, 73, 92, 112, 900]
    educ_bin_labels = ['Some_High_School', 'High_School_Diploma', 'Some_College',
                    'Bachelors_Degree', 'Beyond_Bachelors']
    df['educ_binned'] = pd.cut(df['EDUC'], bins=educ_bins, labels=educ_bin_labels, include_lowest=True)
    return df


def s21_within_group_averages(df):
    col = 'real_wage'
    weights = 'ASECWT'
    
    group_means = (
        df.dropna(subset=[col], how='any')
        .groupby(['age_binned', 'educ_binned'])
        .apply(lambda row: np.average(row[col], weights=row[weights]))
    )
    return group_means


def s24_demographically_adj_series(df, tdf):
    col = 'real_wage'
    weights = 'ASECWT'
    
    inner_means = (
        df
        .groupby(by=['YEAR', 'age_binned', 'educ_binned'], observed=False) 
        .apply(lambda x: np.average(x[col], weights=x[weights])))
    
    # Freeze weights at year 2000
    weights_2000 = (df[df. YEAR.dt.year == 2000]
                    .dropna()
                    .groupby(by=['age_binned', 'educ_binned'], observed=False)
                    ['ASECWT']
                    .sum())
    
    # Compute adjusted average wages
    adj_series = (inner_means
                .groupby(level='YEAR', observed=False)
                .apply(lambda x: np.average (x, weights = weights_2000)))
    
    #Lag the series
    adj_series = adj_series.shift(-1)
    tdf ['adj_ave_wages'] = adj_series
    
    # Compute Adjusted Average Wage Growth
    tdf ['adj_ave_wage_growth'] = tdf ['adj_ave_wages'].pct_change(fill_method=None)


    return tdf

if __name__ == "__main__":
    df = load_cps.load_clean(DATA_DIR, start_date="2000-01-01", end_date="2024-01-01")
    df = s04_subsample(df)
    df = s05_new_vars(df)
    df = s06_drop(df)
    df = s10_drop_by_percentiles(df)
    tdf = s12_time_series(df)
    df = s20_bin_vars(df)
    group_means = s21_within_group_averages(df)
    tdf = s24_demographically_adj_series(df, tdf)
    # Save to the pulled subdirectory because this data is automatically derived
    # from another source (even if the original source is from manual, this goes
    # in the pulled subdirectory because it's automatically created)
    tdf.to_parquet(DATA_DIR / "pulled" / "wage_growth.parquet")
