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

# save data frame to data/processed.
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-31122019.csv'
df.to_csv(processed_data_path)