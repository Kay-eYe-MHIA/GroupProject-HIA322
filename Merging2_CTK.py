# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:01:15 2024

@author: CHOW
"""


import pandas as pd

# Load CSV files first
df5 = pd.read_csv(r"C:/Users/CHOW/OneDrive/Desktop/HIA322 PROJECT/checkin_state.csv")
df6 = pd.read_csv(r"C:/Users/CHOW/OneDrive/Desktop/HIA322 PROJECT/cases_state.csv")
merged_4dfs = pd.read_csv(r"C:/Users/CHOW/OneDrive/Desktop/HIA322 PROJECT/checkin_merged_4dfs.csv")


# Reshaping the df1 such that the each state are reorganised to columns for their respective metrics by date 
# Pivot the DataFrame to create a wide format
df_wide = df5.pivot_table(index='date', columns='state', values=['checkins', 'unique_ind', 'unique_loc'], aggfunc='first')
# Flatten the multi-level columns
df_wide.columns = [f'{col[1]}_{col[0]}' for col in df_wide.columns]
# Reset the index to bring 'date' back as a column
df_wide.reset_index(inplace=True)

# List of DataFrames
dfs = [df5, df6, df_wide, merged_4dfs]


# Convert 'date' column to datetime for all DataFrames
for df in dfs:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
 
 
   
# Removing dates outside of range in cases_states
# Define the date range
start_date = '2020-12-01 00:00:00'
end_date = '2022-06-11 00:00:00'

# Convert 'start_date' and 'end_date' to datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)
# Filter rows where 'date' is within the specified range
df6_filtered = df6[(df6['date'] >= start_date) & (df6['date'] <= end_date)]
print(f"New df6 shape: {df6_filtered.shape}")
    

 
# Merging the dfs
merged_5dfs = pd.merge(merged_4dfs, df_wide, on='date', how='outer')
print(f"After merging df1-4 with tranformed df5: {merged_5dfs.shape}")  

merged_states = pd.merge(df5, df6_filtered, on=['date','state'], how='outer')
print(f"After merging df5 with df6: {merged_states.shape}")

# Exporting merged dfs to pc.
output_file_path = r"C:\Users\CHOW\OneDrive\Desktop\HIA322 PROJECT\checkin_merged_5dfs.csv"
merged_5dfs.to_csv(output_file_path, index=False)
output_file_path = r"C:\Users\CHOW\OneDrive\Desktop\HIA322 PROJECT\merged_states.csv"
merged_states.to_csv(output_file_path, index=False)


