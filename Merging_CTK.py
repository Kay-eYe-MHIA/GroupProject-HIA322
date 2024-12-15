# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:28:49 2024

@author: CHOW
"""

import pandas as pd

# Load CSV files first
df1 = pd.read_csv(r"C:/Users/CHOW/OneDrive/Desktop/HIA322 PROJECT/checkin_malaysia.csv")
df2 = pd.read_csv(r"C:/Users/CHOW/OneDrive/Desktop/HIA322 PROJECT/checkin_malaysia_time.csv")
df3 = pd.read_csv(r"C:/Users/CHOW/OneDrive/Desktop/HIA322 PROJECT/cases_malaysia.csv")
df4 = pd.read_csv(r"C:/Users/CHOW/OneDrive/Desktop/HIA322 PROJECT/trace_malaysia.csv")

# List of DataFrames
dfs = [df1, df2, df3, df4]
df_names = ['df1', 'df2', 'df3', 'df4']

# Convert 'date' column to datetime for all DataFrames
for df in dfs:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Identify smallest and largest date for date columns in all dfs
for df, name in zip(dfs, df_names):
    smallest_date = df['date'].min()
    largest_date = df['date'].max()
    print(f"{name} Smallest date: {smallest_date}")
    print(f"{name} Largest date: {largest_date}")

# 
# Define the date range
start_date = '2020-12-01 00:00:00'
end_date = '2022-06-11 00:00:00'
# Ensure the 'date' columns in df3 and df5 
df3['date'] = pd.to_datetime(df3['date'], errors='coerce')

# Convert 'start_date' and 'end_date' to datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)
# Filter rows where 'date' is within the specified range
df3_filtered = df3[(df3['date'] >= start_date) & (df3['date'] <= end_date)]
print(f"New df3 shape: {df3_filtered.shape}")

# Merge data on 'date' column
merged_df = pd.merge(df1, df2, on='date', how='outer')
print(f"After merging df1 and df2: {merged_df.shape}")  
merged_df = pd.merge(merged_df, df3_filtered, on='date', how='outer') 
print(f"After merging df3: {merged_df.shape}") 
merged_df = pd.merge(merged_df, df4, on='date', how='outer')
print(f"After merging df4: {merged_df.shape}")  


# Exporting merged file to pc.
output_file_path = r"C:\Users\CHOW\OneDrive\Desktop\HIA322 PROJECT\checkin_merged_4dfs.csv"
merged_df.to_csv(output_file_path, index=False)
