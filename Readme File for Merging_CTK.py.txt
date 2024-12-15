Readme File for Merging_CTK.py

(Line 10-16)
Imported 6 csv files into 6 separate dataframes (row,coluns):
df1: checkin_malaysia.csv (558,4)
df2: checkin_malaysia_time.csv (558,49)
df3: checkin_state.csv (8928,5)
df4: cases_malaysia.csv (1765,31)
df5: cases_state.csv (28240,25)
df6: trace_malaysia.csv (423,4)

(Line 22-24)
Standardize the column format for date

(Line 26-31)
Next determined the start and end date for each of the dfs. 
Noticed the most common start date (smallest) was 2020-12-01 
And the most common end date (largest) was 2022-06-11

(Line 33-45)
Remove data from df4 and df5 which was outside the range of 2022-12-01 to 2022-06-11

(Line 49-59)
Merge all 6 dataframes into 1 dataframe called merged_df

(Line 61-63)
Export merged_df to csv files on desktop.


ISSUES for Discussion
1. df3 and df5 are problematic. 
   Reason for 8900+ rows = Each date is split in 13 states + 3 WPs. 
   Do we want to re-organise the data and then merge?
   Suggestion: Each date remains as one row but convert the states into columns.
               Therefore, we will have Johor-Checkins,Johor-Unique_ind, Johor-Unique_loc, 
                                       Kedah-Checkins,Johor-Unique_ind..... as columns.
               But if we do that, df5 is problematic with 23 x 16 columns.... 

2. I don't know what are the additional / duplicate data after merging with df5 and df6. 