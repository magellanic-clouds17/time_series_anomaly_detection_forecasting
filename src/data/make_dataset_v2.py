# import libraries to read in csv data
import pandas as pd

# import data from data/raw
raw_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\raw\RealTimeConsumption-01012016-04082020.csv'
df = pd.read_csv(raw_data_path)
df.head(300)


# change the column name date to datetime
df.rename(columns={'Date': 'Datetime'}, inplace=True)

# integrate hour column with date column ()
df['Datetime'] = df['Datetime'] + ' ' + df['Hour']

# drop Hour column
df.drop(['Hour'], axis=1, inplace=True)

# set Datetime column as index
df.set_index('Datetime', inplace=True)

# change index to datetime
df.index = pd.to_datetime(df.index, format="%d.%m.%Y %H:%M")

# remove 2020 data
df = df[df.index.year < 2020]

# change Consumption (MWh) column type to float (first remove commas)
df['Consumption (MWh)'] = df['Consumption (MWh)'].str.replace(',', '')
df['Consumption (MWh)'] = df['Consumption (MWh)'].astype(float)
df.info()

# check for duplicated indeces
duplicate_indices = df.index[df.index.duplicated()]
# Display the duplicated timestamps
print(duplicate_indices)
# Display rows with duplicated indices
duplicates = df.loc[df.index.isin(duplicate_indices)]
print(duplicates)
# remove on of the duplicated rows
df.drop_duplicates(inplace=True)
# check for row with datetime index 2016-03-27 04:00:00
df.loc['2016-03-27 04:00:00']

## Outlier analysis and removal
# plot histogram of consumption data
df['Consumption (MWh)'].hist(bins=500)

# have a closer look at lower values with dot plot
df[df['Consumption (MWh)'] < 20000].plot(style='.', figsize=(15,5))

# add an id column that just counts +1 for each row
df['id'] = range(1, len(df) + 1)
#convert id column values to float
df['id'] = df['id'].astype(float)

# remove Consumption (MWh) values under 1000 and replace with average of prior and following row using the id column
error_ids = []
error_ids = df[df['Consumption (MWh)'] < 1000]['id']

for id in error_ids:
    # Find rows where 'id' is prior_id or following_id
    prior_row = df[df['id'] == id - 1]
    following_row = df[df['id'] == id + 1]

    # Check if prior_row and following_row are not empty and fill in the missing value with average of prior and following row
    if not prior_row.empty and not following_row.empty:
        df.loc[df['id'] == id, 'Consumption (MWh)'] = (prior_row['Consumption (MWh)'].values[0] + following_row['Consumption (MWh)'].values[0]) / 2
       
## ADD MISSING HOURS TO DATA FRAME AND INTERPOLATE VALUES
#check how many hours each year has
print (df[df.index.year == 2016].shape) 
print (df[df.index.year == 2017].shape)
print (df[df.index.year == 2018].shape)
print (df[df.index.year == 2019].shape)

# how many hours should a normal and a leap year have?
print(24*366)
print(24*365)

# calculate sum of missing hours in 2016, 2017, 2018 and 2019
print(24*366 - df[df.index.year == 2016].shape[0]) # 21
print(24*365 - df[df.index.year == 2017].shape[0]) # 75
print(24*365 - df[df.index.year == 2018].shape[0]) # 122 
print(24*365 - df[df.index.year == 2019].shape[0]) # 150

# check df.index.hour for missing hours
df.index.hour.value_counts().sort_index()

# Identify missing hours
missing_hour_info = []

for i in range(1, len(df) - 1):
    prev_hour = df.index[i - 1].hour
    current_hour = df.index[i].hour
    next_hour = df.index[i + 1].hour

    # Check if there's a missing hour between the previous and next
    if not ((current_hour == (prev_hour + 1) % 24) or (prev_hour == 23 and current_hour == 0)):
            missing_hour_info.append((df.iloc[i - 1], df.iloc[i + 1]))

# Print the rows before and after the missing hour
for before, after in missing_hour_info:
    print("Row before missing hour:\n", before)
    print('------------------------')
    print("Row after missing hour:\n", after)
    print('\n')

# create a datetime series ranging from 2016-01-01 00:00:00 to 2019-12-31 23:00:00
dt_series = pd.date_range(start='2016-01-01 00:00:00', end='2019-12-31 23:00:00', freq='H') # 35064
len(df) # 34696

x = len(dt_series) - len(df) # => missing hours = 368 which aligns with the above calculation

# left join df with dt_series based on index of df and dt_series so that all missing hours are added to df
df_full = df.join(dt_series.to_frame(), how='right')

# check if join worked as intended
df_full[990:1000]
len(df_full)

# interpolate missing values
df_full['Consumption (MWh)'] = df_full['Consumption (MWh)'].interpolate(method='linear', limit_direction='both')

# drop id and 0 columns
df_full.drop(['id', 0], axis=1, inplace=True)

# save df_clean to data/processed.
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-31122019_full.csv'
df_full.to_csv(processed_data_path)