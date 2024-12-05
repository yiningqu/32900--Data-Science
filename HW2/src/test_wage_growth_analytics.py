import pandas as pd
import numpy as np

import config

DATA_DIR = config.DATA_DIR

import load_cps
import wage_growth_analytics

df_original = load_cps.load_clean(DATA_DIR, start_date="2000-01-01", end_date="2024-01-01")

def test_s04():
    df = df_original.copy()
    df = wage_growth_analytics.s04_subsample(df)
    expected_output = '''
    YEAR          CPI99        CPSIDV         ASECWT            AGE       WKSWORK1     UHRSWORKLY       INCWAGE
    count                         769289  769289.000000  7.692890e+05  769289.000000  769289.000000  769289.000000  769289.000000  7.692890e+05
    mean   2010-09-12 14:19:39.280088576       0.784055  1.290173e+14    1680.481934      39.523704      49.189409      43.371912  5.890466e+04
    min              2000-01-01 00:00:00       0.569000  0.000000e+00      25.330000      25.000000       1.000000       1.000000  1.000000e+00
    25%              2005-01-01 00:00:00       0.703000  0.000000e+00     816.090000      33.000000      52.000000      40.000000  2.600000e+04
    50%              2010-01-01 00:00:00       0.774000  2.003121e+14    1503.350000      40.000000      52.000000      40.000000  4.400000e+04
    75%              2016-01-01 00:00:00       0.882000  2.012030e+14    2177.640000      47.000000      52.000000      48.000000  7.000000e+04
    max              2023-01-01 00:00:00       1.000000  2.023031e+14   44423.830000      54.000000      52.000000      99.000000  2.099999e+06
    std                              NaN       0.112511  9.636801e+13    1246.005545       8.323588       8.458423       9.639418  6.790786e+04
    '''

    assert df.describe().to_string().replace(" ", "").replace("\n", "") == expected_output.replace(" ", "").replace("\n", "")


def test_s05():
    df = df_original.copy()
    df = wage_growth_analytics.s04_subsample(df)
    df = wage_growth_analytics.s05_new_vars(df)
    expected_output = '''
    YEAR          CPI99        CPSIDV         ASECWT            AGE       WKSWORK1     UHRSWORKLY       INCWAGE  real_incwage   annual_hours      real_wage
    count                         769289  769289.000000  7.692890e+05  769289.000000  769289.000000  769289.000000  769289.000000  7.692890e+05  7.692890e+05  769289.000000  769289.000000
    mean   2010-09-12 14:19:39.280088576       0.784055  1.290173e+14    1680.481934      39.523704      49.189409      43.371912  5.890466e+04  4.514682e+04    2146.530205      21.945576
    min              2000-01-01 00:00:00       0.569000  0.000000e+00      25.330000      25.000000       1.000000       1.000000  1.000000e+00  7.260000e-01       1.000000       0.000213
    25%              2005-01-01 00:00:00       0.703000  0.000000e+00     816.090000      33.000000      52.000000      40.000000  2.600000e+04  2.090400e+04    2080.000000      10.384615
    50%              2010-01-01 00:00:00       0.774000  2.003121e+14    1503.350000      40.000000      52.000000      40.000000  4.400000e+04  3.408600e+04    2080.000000      15.772436
    75%              2016-01-01 00:00:00       0.882000  2.012030e+14    2177.640000      47.000000      52.000000      48.000000  7.000000e+04  5.362500e+04    2340.000000      24.187500
    max              2023-01-01 00:00:00       1.000000  2.023031e+14   44423.830000      54.000000      52.000000      99.000000  2.099999e+06  1.352399e+06    5148.000000  312342.282000
    std                              NaN       0.112511  9.636801e+13    1246.005545       8.323588       8.458423       9.639418  6.790786e+04  5.016841e+04     607.767474     368.104578
    '''
    # print(df.describe().to_string().replace(" ", "").replace("\n", ""))
    assert df.describe().to_string().replace(" ", "").replace("\n", "") == expected_output.replace(" ", "").replace("\n", "")

def test_s06():
    df = df_original.copy()
    df = wage_growth_analytics.s04_subsample(df)
    df = wage_growth_analytics.s05_new_vars(df)
    df = wage_growth_analytics.s06_drop(df)
    expected_output = '''
    YEAR        CPSIDV         ASECWT            AGE     UHRSWORKLY       INCWAGE  real_incwage   annual_hours      real_wage
    count                         769289  7.692890e+05  769289.000000  769289.000000  769289.000000  7.692890e+05  7.692890e+05  769289.000000  769289.000000
    mean   2010-09-12 14:19:39.280088576  1.290173e+14    1680.481934      39.523704      43.371912  5.890466e+04  4.514682e+04    2146.530205      21.945576
    min              2000-01-01 00:00:00  0.000000e+00      25.330000      25.000000       1.000000  1.000000e+00  7.260000e-01       1.000000       0.000213
    25%              2005-01-01 00:00:00  0.000000e+00     816.090000      33.000000      40.000000  2.600000e+04  2.090400e+04    2080.000000      10.384615
    50%              2010-01-01 00:00:00  2.003121e+14    1503.350000      40.000000      40.000000  4.400000e+04  3.408600e+04    2080.000000      15.772436
    75%              2016-01-01 00:00:00  2.012030e+14    2177.640000      47.000000      48.000000  7.000000e+04  5.362500e+04    2340.000000      24.187500
    max              2023-01-01 00:00:00  2.023031e+14   44423.830000      54.000000      99.000000  2.099999e+06  1.352399e+06    5148.000000  312342.282000
    std                              NaN  9.636801e+13    1246.005545       8.323588       9.639418  6.790786e+04  5.016841e+04     607.767474     368.104578
    '''
    # print(df.describe().to_string().replace(" ", "").replace("\n", ""))
    assert df.describe().to_string().replace(" ", "").replace("\n", "") == expected_output.replace(" ", "").replace("\n", "")


def test_s10():
    df = df_original.copy()
    df = wage_growth_analytics.s04_subsample(df)
    df = wage_growth_analytics.s05_new_vars(df)
    df = wage_growth_analytics.s06_drop(df)
    df = wage_growth_analytics.s10_drop_by_percentiles(df)
    expected_output = '''
    YEAR        CPSIDV         ASECWT            AGE     UHRSWORKLY        INCWAGE   real_incwage   annual_hours      real_wage
    count                         753893  7.538930e+05  753893.000000  753893.000000  753893.000000  753893.000000  753893.000000  753893.000000  753893.000000
    mean   2010-09-15 20:14:58.255853568  1.290703e+14    1680.891075      39.499364      43.396608   55359.312912   42445.377476    2150.576785      19.419075
    min              2000-01-01 00:00:00  0.000000e+00      25.330000      25.000000       1.000000       8.000000       6.432000       1.000000       2.375237
    25%              2005-01-01 00:00:00  0.000000e+00     816.240000      33.000000      40.000000   27000.000000   21168.000000    2080.000000      10.471154
    50%              2010-01-01 00:00:00  2.003121e+14    1503.170000      40.000000      40.000000   44000.000000   34120.000000    2080.000000      15.772436
    75%              2016-01-01 00:00:00  2.012030e+14    2178.200000      46.000000      47.000000   70000.000000   53040.000000    2340.000000      23.930288
    max              2023-01-01 00:00:00  2.023031e+14   44423.830000      54.000000      99.000000  850000.000000  554200.000000    5148.000000     116.576010
    std                              NaN  9.635294e+13    1246.554767       8.320886       9.506759   46939.777996   35094.709835     598.662377      13.973878
    '''
    # print(df.describe().to_string().replace(" ", "").replace("\n", ""))
    assert df.describe().to_string().replace(" ", "").replace("\n", "") == expected_output.replace(" ", "").replace("\n", "")


def test_s12():
    df = df_original.copy()
    df = wage_growth_analytics.s04_subsample(df)
    df = wage_growth_analytics.s05_new_vars(df)
    df = wage_growth_analytics.s06_drop(df)
    df = wage_growth_analytics.s10_drop_by_percentiles(df)
    tdf = wage_growth_analytics.s12_time_series(df)

    expected_output = '''
    ave_wages  median_wages  employment
    YEAR                                           
    2019-01-01  20.416218     15.980392    0.967102
    2020-01-01  21.310733     16.843077    0.959912
    2021-01-01  20.763327     16.262019    0.955919
    2022-01-01  20.463601     16.003125    0.967468
    2023-01-01        NaN           NaN    0.967883
    '''
    # print(tdf.tail().to_string().replace(" ", "").replace("\n", ""))
    assert tdf.tail().to_string().replace(" ", "").replace("\n", "") == expected_output.replace(" ", "").replace("\n", "")


def test_s20():
    df = df_original.copy()
    df = wage_growth_analytics.s04_subsample(df)
    df = wage_growth_analytics.s05_new_vars(df)
    df = wage_growth_analytics.s06_drop(df)
    df = wage_growth_analytics.s10_drop_by_percentiles(df)
    # tdf = wage_growth_analytics.s12_time_series(df)
    df = wage_growth_analytics.s20_bin_vars(df)

    expected_output = '''
    YEAR        CPSIDV         ASECWT            AGE     UHRSWORKLY        INCWAGE   real_incwage   annual_hours      real_wage
    count                         753893  7.538930e+05  753893.000000  753893.000000  753893.000000  753893.000000  753893.000000  753893.000000  753893.000000
    mean   2010-09-15 20:14:58.255853568  1.290703e+14    1680.891075      39.499364      43.396608   55359.312912   42445.377476    2150.576785      19.419075
    min              2000-01-01 00:00:00  0.000000e+00      25.330000      25.000000       1.000000       8.000000       6.432000       1.000000       2.375237
    25%              2005-01-01 00:00:00  0.000000e+00     816.240000      33.000000      40.000000   27000.000000   21168.000000    2080.000000      10.471154
    50%              2010-01-01 00:00:00  2.003121e+14    1503.170000      40.000000      40.000000   44000.000000   34120.000000    2080.000000      15.772436
    75%              2016-01-01 00:00:00  2.012030e+14    2178.200000      46.000000      47.000000   70000.000000   53040.000000    2340.000000      23.930288
    max              2023-01-01 00:00:00  2.023031e+14   44423.830000      54.000000      99.000000  850000.000000  554200.000000    5148.000000     116.576010
    std                              NaN  9.635294e+13    1246.554767       8.320886       9.506759   46939.777996   35094.709835     598.662377      13.973878
    '''
    # print(df.describe().to_string().replace(" ", "").replace("\n", ""))
    assert df.describe().to_string().replace(" ", "").replace("\n", "") == expected_output.replace(" ", "").replace("\n", "")


def test_s21():
    df = df_original.copy()
    df = wage_growth_analytics.s04_subsample(df)
    df = wage_growth_analytics.s05_new_vars(df)
    df = wage_growth_analytics.s06_drop(df)
    df = wage_growth_analytics.s10_drop_by_percentiles(df)
    tdf = wage_growth_analytics.s12_time_series(df)
    df = wage_growth_analytics.s20_bin_vars(df)
    group_means = wage_growth_analytics.s21_within_group_averages(df)
    tdf = wage_growth_analytics.s24_demographically_adj_series(df, tdf)

    expected_output = '''
    ave_wages  median_wages  employment  adj_ave_wages  adj_ave_wage_growth
    YEAR                                                                               
    2019-01-01  20.416218     15.980392    0.967102      19.369346             0.022354
    2020-01-01  21.310733     16.843077    0.959912      20.127113             0.039122
    2021-01-01  20.763327     16.262019    0.955919      19.554291            -0.028460
    2022-01-01  20.463601     16.003125    0.967468      19.120552            -0.022181
    2023-01-01        NaN           NaN    0.967883            NaN                  NaN
    '''
    # print(tdf.tail().to_string().replace(" ", "").replace("\n", ""))
    assert tdf.tail().to_string().replace(" ", "").replace("\n", "") == expected_output.replace(" ", "").replace("\n", "")


