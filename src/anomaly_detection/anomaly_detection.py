import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# read in processed data
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-31122019.csv'
df = pd.read_csv(processed_data_path, index_col=0)

# convert index to datetime
df.index = pd.to_datetime(df.index)

# check type of consumption column (it's float)
df['Consumption (MWh)'].dtype

# estimation of outliers in the data using Isolation Forest
contamination = 0.01

# build isolation forest model
model = IsolationForest(contamination=contamination, n_estimators=1000)

#reshape the 'Consumption (MWh)' column since the model expects a 2D array
model.fit(df['Consumption (MWh)'].values.reshape(-1, 1))

# add anomaly column to dataframe
df['anomaly'] = model.predict(df['Consumption (MWh)'].values.reshape(-1, 1))
df

# plot the consumption data with anomalies in red
plt.figure(figsize=(15,5))
plt.plot(df.index, df['Consumption (MWh)'], color='blue', label='Consumption')
plt.scatter(df.index[df['anomaly'] == -1], df['Consumption (MWh)'][df['anomaly'] == -1], color='red', label='Anomaly')
plt.legend()
plt.title('Energy Consumption with Anomalies')
plt.show()