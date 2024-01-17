import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# read processed data
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-31122019.csv'
df = pd.read_csv(processed_data_path, index_col=0)
df.tail()

# plot Consumption (MWh) column from 2016-01-01 to 2020-08-04
color_pal = sns.color_palette()
df['Consumption (MWh)'].plot(style='.', figsize=(15,5), color=color_pal[0], title='Energy Consumption in MWh')

# plot Consumption (MWh) column for the an exemplary week in 2016 a line plot and dot plot.
df['Consumption (MWh)'].loc['2016-01-04':'2016-01-10'].plot(figsize=(15,5), title='Energy Consumption in MWh')
df['Consumption (MWh)'].loc['2016-01-04':'2016-01-10'].plot(style='.', figsize=(15,5), color=color_pal[0], title='Energy Consumption in MWh')

# plot data for the an exemplary month in 2016 a line plot
df['Consumption (MWh)'].loc['2016-01-01':'2016-01-31'].plot(figsize=(15,5), title='Energy Consumption in MWh')
