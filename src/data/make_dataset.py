# import libraries to read in csv data
import pandas as pd

# import data from data/raw
raw_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\raw\RealTimeConsumption-01012016-04082020.csv'
df = pd.read_csv(raw_data_path)
df.head(300)
df.tail()
df.set_index('Date', inplace=True)

# change index to datetime
df.index = pd.to_datetime(df.index, format="%d.%m.%Y")


# change Consumption (MWh) column type to float (first remove commas)
df['Consumption (MWh)'] = df['Consumption (MWh)'].str.replace(',', '')
df['Consumption (MWh)'] = df['Consumption (MWh)'].astype(float)
df.info()

# remove Consumption (MWh) values under 1000 since they are errors
df = df[df['Consumption (MWh)'] > 1000]

# save data frame to data/processed
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-04082020.csv'
df.to_csv(processed_data_path)