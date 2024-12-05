import pandas as pd
from matplotlib import pyplot as plt

import config
DATA_DIR = config.DATA_DIR
OUTPUT_DIR = config.OUTPUT_DIR

tdf = pd.read_parquet(DATA_DIR / "pulled" / "wage_growth.parquet")
tdf[['ave_wages', 'adj_ave_wages']].plot()
plt.savefig(OUTPUT_DIR / "adj_wage_growth.png")
