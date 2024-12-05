###########################
## Template
import matplotlib.pyplot as plt
import pandas as pd
import load_merged_repo_data

df = load_merged_repo_data.load_all()

i_replicated_figure_1 = False

spike_dates = df[df['REPO-TRI_AR_OO-P'] > df['DFEDTARU']].index

plt.plot(df.index, df['REPO-TRI_AR_OO-P'], label='Tri-party repo average rate', color='darkblue')
plt.plot(df.index, df['EFFR'], label='Effective federal funds rate', color='lightblue')
plt.plot(df.index, df['IOER'], label='Interest on Excess Reserves', color='black', linestyle='--', dashes=(5, 2))
plt.plot(df.index, df['RRPONTSYAWARD'], label='ON RRP Facility Rate', color='black', linestyle='--', dashes=(10, 10))
plt.fill_between(df.index, df['DFEDTARL'], df['DFEDTARU'], color='gray', alpha=0.3)

plt.legend()
plt.title('Repo Rate Spikes, August 2014–Janurary 2024')
plt.xlabel('Date')
plt.ylabel('Spread over federal fund target')
plt.tight_layout()
plt.show()

i_replicated_figure_1 = True