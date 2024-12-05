"""
NOTE!!!
To complete this assignment, you must adjust this file, the dodo.py
file, so that it will call the wage_growth_analytics.py file and
save the time series data from it in the data/pulled directory.
This then feeds into the next task which will create a plot
of the time series and save the plot in the output directory.

"""
import config
import os

DATA_DIR = config.DATA_DIR
OUTPUT_DIR = config.OUTPUT_DIR

def test_adj_wage_growth_file_exists():
    file_path = os.path.join(OUTPUT_DIR, "adj_wage_growth.png")
    assert os.path.exists(file_path), "adj_wage_growth.png file does not exist"
