import pandas as pd
import numpy as np

import config
DATA_DIR = config.DATA_DIR

def load_raw(data_dir=DATA_DIR, start_date='2000-01-01', end_date='2024-01-01'):
    
    ## Read and Prepare the Data

    # When you save the file, it must be named `cps.csv`
    # and saved in the directory `../data/manual`.
    # It is placed in the `manual` directory because it is not
    # automatically downloaded from the internet.
    path = data_dir / 'manual' / 'cps.csv'

    df = pd.read_csv(path)
    
    df = df[["YEAR","GQ","CPI99", "CPSIDV","ASECWT","AGE","SEX","LABFORCE","EDUC",
        "WKSWORK1","UHRSWORKLY","INCWAGE"]]
    
    
    df['YEAR'] = pd.to_datetime(df['YEAR'], format='%Y')
    df['GQ'] = df['GQ'].astype('category')
    df['SEX'] = df['SEX'].astype('category')
    df['LABFORCE'] = df['LABFORCE'].astype('category')
    df['EDUC'] = df['EDUC'].astype('category')
    df['CPSIDV'] = df['CPSIDV'].astype('int64')
    df['AGE'] = df['AGE'].astype('int64')
    df['WKSWORK1'] = df['WKSWORK1'].astype('int64')
    df['UHRSWORKLY'] = df['UHRSWORKLY'].astype('int64')
    df['INCWAGE'] = df['INCWAGE'].astype('int64')
    
    return df

def load_clean(data_dir=DATA_DIR, start_date='2000-01-01', end_date='2024-01-01'):
    df = load_raw(data_dir, start_date, end_date)
    ## Fill in Missing Values or NIU
    
    df.loc[df['SEX'] == 9, 'SEX'] = np.nan
    df.loc[df['LABFORCE'] == 0, 'LABFORCE'] = np.nan
    df.loc[df['EDUC'] == 1, 'EDUC'] = np.nan
    df.loc[df['EDUC'] == 999, 'EDUC'] = np.nan
    df.loc[df['UHRSWORKLY'] == 999, 'UHRSWORKLY'] = np.nan
    df.loc[df['INCWAGE'] == 9999999, 'INCWAGE'] = np.nan
    df.loc[df['INCWAGE'] == 9999998, 'INCWAGE'] = np.nan

    return df


if __name__ == "__main__":
    pass