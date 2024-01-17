import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

# read processed data
processed_data_path = r'C:\Users\Latitude\Desktop\Kaggle\time_series_energy_portfolio_project\data\processed\RealTimeConsumption-01012016-31122019_features.csv'
df = pd.read_csv(processed_data_path, index_col=0)

# convert index to datetime
df.index = pd.to_datetime(df.index)

# split data into train and test sets, train is data from 2016-01-01 to 2018-12-31, test is data from 2019-01-01 to 2019-12-31. The goal is to forecast the year 2019 based on the data from 2016-2018.
train = df.loc['2016-01-01':'2018-12-31']
test = df.loc['2019-01-01':'2019-12-31']
y_train = train['Consumption (MWh)']
y_test = test['Consumption (MWh)']

# drop target variable from train and test x sets
X_train = train.drop(['Consumption (MWh)'], axis=1)
X_test = test.drop(['Consumption (MWh)'], axis=1)

# check if index type is datetime
print(X_train.index.dtype)

# convert index type of x_train and x_test to datetime
X_train.index = pd.to_datetime(X_train.index)
X_test.index = pd.to_datetime(X_test.index)

# check if index type is datetime
print(X_train.index.dtype)
print(X_test.index.dtype)

# visualize train and test sets in a dot plot
plt.figure(figsize=(15,5))
plt.plot(X_train.index, y_train, '.', label='train')
plt.plot(X_test.index, y_test, '.', label='test')
plt.legend()
plt.title('Train and Test Sets')

# create xgboost regressor with early stopping and eval_set
xg_reg = xgb.XGBRegressor(objective='reg:squarederror', early_stopping_rounds=50, learning_rate=0.1, n_estimators=1000)

# fit regressor to training data. Implement early stopping and eval_set to see how well the model performs on the test set.
xg_reg.fit(X_train, y_train, eval_set=[(X_train,y_train),(X_test, y_test)], verbose=100)

# feature importance
xgb.plot_importance(xg_reg)

# visualize the predictions of the model on the test set
test['predictions'] = xg_reg.predict(X_test)

# convert index to datetime
test.index = pd.to_datetime(test.index)


# plot predictions and actual values for the test set
plt.figure(figsize=(15,5))
plt.plot(test['Consumption (MWh)'], label='actual')
plt.plot(test['predictions'], label='predictions')
plt.legend()
plt.title('Predictions and Actual Data for 2019')

# plot predictions and actual values for the test set for january 2019
plt.figure(figsize=(15,5))
plt.plot(test.loc['2019-01-01':'2019-01-31', 'Consumption (MWh)'], label='actual')
plt.plot(test.loc['2019-01-01':'2019-01-31', 'predictions'], label='predictions')
plt.legend()
plt.title('Predictions and Actual Data for January 2019')

# plot predictions and actual values for the test set for first week of august 2019
plt.figure(figsize=(15,5))
plt.plot(test.loc['2019-08-01':'2019-08-07', 'Consumption (MWh)'], label='actual')
plt.plot(test.loc['2019-08-01':'2019-08-07', 'predictions'], label='predictions')
plt.legend()
plt.title('Predictions and Actual Data for a Week in August 2019')

# merge df with predictions in order to plot the actual values and predictions in one plot
df = df.merge(test[['predictions']], how='left', left_index=True, right_index=True)

# plot predictions and actual values for the test for all years
plt.figure(figsize=(15,5))
plt.plot(df['Consumption (MWh)'], label='actual')
plt.plot(df['predictions'], label='predictions')
plt.legend()
plt.title('Complete Actual Data and Predictions')

# print the mean absolute error, mean squared error and r2 score for the year 2019
mae = mean_absolute_error(test['Consumption (MWh)'], test['predictions'])
mse = mean_squared_error(test['Consumption (MWh)'], test['predictions'])
r2 = r2_score(test['Consumption (MWh)'], test['predictions'])
print('Mean Absolute Error: %.3f' % mae)
print('Mean Squared Error: %.3f' % mse)
print('R² Score: %.3f' % r2)










