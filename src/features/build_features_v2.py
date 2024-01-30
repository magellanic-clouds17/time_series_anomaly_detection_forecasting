import pandas as pd

# import processed data
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-31122019_full.csv'
df = pd.read_csv(processed_data_path, index_col=0)

# convert index to datetime
df.index = pd.to_datetime(df.index)

# build features day_of_week, day_of_month, month, year, hour.
df['year'] = df.index.year
df['day_of_month'] = df.index.day
df['month'] = df.index.month
df['hour'] = df.index.hour
df['day_of_week'] = df.index.dayofweek
df['day_of_year'] = df.index.dayofyear

# create yearly lag features
df['lag_1'] = df['Consumption (MWh)'].shift(24*365)
df['lag_2'] = df['Consumption (MWh)'].shift(24*365*2)

# Adjust for leap years:
# If year is a leap year shift by 366 days instead of 365 days
df.loc[df['year'] % 4 == 1, 'lag_1'] = df['Consumption (MWh)'].shift(24*366)
df.loc[df['year'] % 4 == 2, 'lag_2'] = df['Consumption (MWh)'].shift(24*365+24*366)

# check if lags work as intended
print(df.iloc[0])
print(df.iloc[366*24])
print(df.iloc[366*24 +365*24])
print(df.iloc[366*24 + 365*24 + 365*24])

# save data frame to data/processed as RealTimeConsumption-01012016-31122019_features.csv
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-31122019_features_full.csv'
df.to_csv(processed_data_path)