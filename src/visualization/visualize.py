import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# read processed data
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-04082020.csv'
df = pd.read_csv(processed_data_path, index_col=0)

# plot data
color_pal = sns.color_palette()
df.plot(style='.', figsize=(15,5), color=color_pal[0], title='Energy Consumption in MWh')
