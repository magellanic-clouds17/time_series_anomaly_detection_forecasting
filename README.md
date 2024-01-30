# Time Series Forecasting of Energy Consumption in Turkey

## Project Overview

This repository contains a time series forecasting project focused on predicting the hourly energy consumption of Turkey using data from 2016 to 2018 to forecast for the year 2019 (https://www.kaggle.com/datasets/hgultekin/hourly-power-consumption-of-turkey-20162020). The project aims to demonstrate my skills in handling time series data.

## Data

The dataset used is "Hourly Power Consumption of Turkey (2016-2020)" from Kaggle, which includes hourly energy consumption data in Megawatt-hours (MWh). The data from 2016 to 2018 was used to train the model, and the data from 2019 was used for testing and validating the predictions.

## Methodology

The project follows these steps:

1. **Data Preprocessing (`make_dataset.py`):** Importing, cleaning, and preparing the dataset for analysis.
       1.1 **Data Preprocessing (`make_dataset_v2.py`):** adding missing hour rows and interpolate values
3. **Exploratory Data Analysis (`visualize.py`):** Visualizing the energy consumption trends over time.
4. **Feature Engineering (`build_features.py`):** Creating additional features like day of the week, month, and hour to improve the model's performance.
       4.1 **Feature Engineering (`build_features_v2.py`):** Creating additional features like day of the year, yearly lags 1 and 2.
6. **Model Training and Evaluation (`train_model.py`):** Using XGBoost for time series forecasting and evaluating its performance on the 2019 data.
    - The XGBoost model was trained with early stopping to prevent overfitting.
    - Feature importance was analyzed to understand the impact of different time-related features.
    - The model's predictions for the year 2019 were plotted against actual values, showing how closely the model could predict real-world data.
    - Evaluation metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² Score were used to quantify the model's accuracy.
        6.1 **Model Training and Evaluation (`train_model_v2.py`):** Trained on data with more advanced cleaning and feature engineering.
7. **Anomaly Detection (`anomaly_detection.py`):** Identifying unusual patterns in energy consumption.
    - Utilized the Isolation Forest algorithm to estimate and identify anomalies in the dataset.
    - Configured the model with a contamination factor of 0.01, indicating an expected proportion of outlier data.
    - Predicted and labeled data points as normal or anomalies, based on the model's output.

## Key Results
The _v2 data performed worse on the Evaluation (MAE:1567.426 MSE:5475637.342 R²:0.753), hence it's not visualized hereinafter.
  
  ### Evaluation
  - MAE: 1403.981
  - MSE: 4865901.909
  - R²: 0.781
  ### Visualization
  - ![image](https://github.com/magellanic-clouds17/time_series_anomaly_detection_forecasting/assets/72970703/e67fab2d-f9da-4838-9f56-c3995cc9dd4d)
  - ![image](https://github.com/magellanic-clouds17/time_series_anomaly_detection_forecasting/assets/72970703/3833a07c-848c-4dcf-8c0d-391b76366cc0)
  - ![image](https://github.com/magellanic-clouds17/time_series_anomaly_detection_forecasting/assets/72970703/ad72d878-6234-4289-822a-6f11a3e9829f)
  - ![image](https://github.com/magellanic-clouds17/time_series_anomaly_detection_forecasting/assets/72970703/21ef88ba-f298-4cdc-b08b-32a8a3d6d051)
  - ![image](https://github.com/magellanic-clouds17/time_series_anomaly_detection_forecasting/assets/72970703/d677f973-b06c-4615-a21a-a9a0a08b3f67)

## Conclusion

This project successfully demonstrates the ability to forecast energy consumption using machine learning techniques. It illustrates a simple form of feature engineering and the effectiveness of gradient boosting algorithms in handling time series data.
