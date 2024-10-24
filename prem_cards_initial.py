#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:39:54 2024

@author: judewh
"""

# =============================================================================
# import pandas as pd
# import matplotlib.pyplot as plt
#
# data = 'prem_23-24.csv'
#
# year = data[5:len(data)-4]
#
# df = pd.read_csv(data)
#
# df_hy = df.groupby(['HomeTeam'])['HY'].sum()
# df_ay = df.groupby(['AwayTeam'])['AY'].sum()
#
# df_hr = df.groupby(['HomeTeam'])['HR'].sum()
# df_ar = df.groupby(['AwayTeam'])['AR'].sum()
#
# df_yellows = df_hy.add(df_ay, fill_value=0).reset_index(name='TotalYellows')
# df_reds = df_hr.add(df_ar, fill_value=0).reset_index(name='TotalReds')
#
# df_yellows = df_yellows.rename(columns={'HomeTeam': 'Team'})
# df_reds = df_reds.rename(columns={'HomeTeam': 'Team'})
# df_final = pd.merge(df_yellows, df_reds, on='Team', how='outer')
#
# plt.figure()
# plt.bar(df_final['Team'], df_final['TotalYellows'],
#         width=0.5, color="gold", label="Yellow Cards")
# plt.bar(df_final['Team'], df_final['TotalReds'],
#         width=0.5, bottom=df_final['TotalYellows'], color="red", label="Red Cards")
# plt.legend(loc='best', prop={'size': 8})
# plt.xlabel("Team")
# plt.ylabel("Number of Cards")
# plt.title('Total Cards per Team in the {} season'.format(year))
# plt.xticks(rotation=90)
# plt.savefig('prem_cards_{}.png'.format(year), dpi=300,
#             bbox_inches='tight')
# plt.tight_layout()
# plt.show()
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
print('plotly is here')


# Load the dataset
data = 'prem_23-24.csv'
year = data.split('_')[1].split('.')[0]

df = pd.read_csv(data)

# Group yellow and red cards for both home and away teams
df_yellows = (df.groupby('HomeTeam')['HY'].sum(
) + df.groupby('AwayTeam')['AY'].sum()).reset_index(name='TotalYellows')
df_reds = (df.groupby('HomeTeam')['HR'].sum(
) + df.groupby('AwayTeam')['AR'].sum()).reset_index(name='TotalReds')
df_yellows = df_yellows.rename(columns={'HomeTeam': 'Team'})
df_reds = df_reds.rename(columns={'HomeTeam': 'Team'})

# Merge the yellow and red cards data into a final DataFrame
df_final = pd.merge(df_yellows, df_reds, on='Team', how='outer')

# Create the stacked bar plot
plt.figure(figsize=(10, 6))  # Adjusted the figure size for better readability
bars_yellow = plt.bar(df_final['Team'], df_final['TotalYellows'],
                      width=0.5, color="gold", label="Yellow Cards")
bars_red = plt.bar(df_final['Team'], df_final['TotalReds'], width=0.5,
                   bottom=df_final['TotalYellows'], color="red", label="Red Cards")

# Add labels and legends
plt.legend(loc='best', prop={'size': 8})
plt.xlabel("Team")
plt.ylabel("Number of Cards")
plt.title(f'Total Cards per Team in the {year} season')
plt.xticks(rotation=90)


# =============================================================================
# # Use mplcursors for interactivity
# cursor = mplcursors.cursor([bars_yellow, bars_red], hover=True)
#
#
# @cursor.connect("add")
# def on_add(sel):
#     team = df_final['Team'].iloc[sel.index]
#     total_yellows = df_final['TotalYellows'].iloc[sel.index]
#     total_reds = df_final['TotalReds'].iloc[sel.index]
#     sel.annotation.set(
#         text=f"{team}\nYellow Cards: {total_yellows}\nRed Cards: {total_reds}")
# =============================================================================


# Save and show the plot
plt.savefig(f'prem_cards_{year}.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()

# =============================================================================
# This was my initial try
# df.head()
#
# hy = df['HY']
# ay = df['AY']
#
# arsenal_home = df[df['HomeTeam'].str.contains('Arsenal')]
# arsenal_away = df[df['AwayTeam'].str.contains('Arsenal')]
# arsenal = pd.concat([arsenal_home, arsenal_away])
# =============================================================================


# =============================================================================
# This was me getting to grips with the outputs of some pd functions
# df_yellows = df_hy + df_ay
# df_reds = df_hr + df_ar
#
# =============================================================================

# =============================================================================
# print(df_grouped_away, df_grouped_home, df_grouped)
# =============================================================================
# =============================================================================
# total_home_yellow = sum(hy)
# total_away_yellow = sum(ay)
#
# print(hy)
# print(ay)
# =============================================================================
