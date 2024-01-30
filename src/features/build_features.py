import pandas as pd

# import processed data
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-31122019.csv'
df = pd.read_csv(processed_data_path, index_col=0)

# convert index to datetime
df.index = pd.to_datetime(df.index)

# build features day_of_week, day_of_month, month, year, hour.
df['year'] = df.index.year
df['day_of_month'] = df.index.day
df['month'] = df.index.month
df['hour'] = df.index.hour
df['day_of_week'] = df.index.dayofweek

# save data frame to data/processed as RealTimeConsumption-01012016-31122019_features.csv
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-31122019_features.csv'
df.to_csv(processed_data_path)