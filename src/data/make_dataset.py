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

# change Consumption (MWh) column type to float (first remove commas)
df['Consumption (MWh)'] = df['Consumption (MWh)'].str.replace(',', '')
df['Consumption (MWh)'] = df['Consumption (MWh)'].astype(float)
df.info()

# remove Consumption (MWh) values under 1000 since they are errors
df = df[df['Consumption (MWh)'] > 1000]

# remove 2020 data
df = df[df.index.year < 2020]

# save data frame to data/processed
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-31122019.csv'
df.to_csv(processed_data_path)