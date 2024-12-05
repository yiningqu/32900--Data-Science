"""Run or update the project. This file uses the `doit` Python package. It works
like a Makefile, but is Python-based

NOTE!!!
To complete this assignment, you must adjust this file, the dodo.py
file, so that it will call the wage_growth_analytics.py file and
save the time series data from it in the data/pulled directory.
This then feeds into the next task which will create a plot
of the time series and save the plot in the output directory.

"""
import sys
sys.path.insert(1, './src/')


import config
from pathlib import Path
from doit.tools import run_once
import os
import shutil


OUTPUT_DIR = Path(config.OUTPUT_DIR)
DATA_DIR = Path(config.DATA_DIR)

def task_wage_growth_analytics():
    return {
        'file_dep': ['./src/wage_growth_analytics.py'],
        'targets': [DATA_DIR / 'pulled' / 'wage_growth.parquet'],
        'actions': ['ipython ./src/wage_growth_analytics.py'],
        'clean': True,
        'uptodate': [run_once]
    }

def task_plot_adj_wage_growth():
    return {
        'file_dep': [DATA_DIR / 'pulled' / 'wage_growth.parquet'],
        'targets': [OUTPUT_DIR / 'adj_wage_growth.png'],
        'actions': ['ipython ./src/plot_adj_wage_growth.py'],
        'clean': True,
        'uptodate': [run_once]
    }