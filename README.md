# Time Series Forecasting of Energy Consumption in Turkey

## Project Overview

This repository contains a time series forecasting project focused on predicting the hourly energy consumption of Turkey using data from 2016 to 2018 to forecast for the year 2019. The project aims to demonstrate my skills in handling time series data, suitable for applications in startups and companies dealing with time series forecasting.

## Data

The dataset used is "Hourly Power Consumption of Turkey (2016-2020)" which includes hourly energy consumption data in Megawatt-hours (MWh). The data from 2016 to 2018 was used to train the model, and the data from 2019 was used for testing and validating the predictions.

## Methodology

The project follows these steps:

1. **Data Preprocessing (`make_dataset.py`):** Importing, cleaning, and preparing the dataset for analysis.
2. **Exploratory Data Analysis (`visualize.py`):** Visualizing the energy consumption trends over time.
3. **Feature Engineering (`build_features.py`):** Creating additional features like day of the week, month, and hour to improve the model's performance.
4. **Model Training and Evaluation (`train_model.py`):** Using XGBoost for time series forecasting and evaluating its performance on the 2019 data.

## Key Results

- The XGBoost model was trained with early stopping to prevent overfitting.
- Feature importance was analyzed to understand the impact of different time-related features.
- The model's predictions for the year 2019 were plotted against actual values, showing how closely the model could predict real-world data.
- Evaluation metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² Score were used to quantify the model's accuracy.

## Conclusion

This project successfully demonstrates the ability to forecast energy consumption using machine learning techniques. It highlights the importance of careful feature engineering and the effectiveness of gradient boosting algorithms in handling time series data.

---

Feel free to adjust or add any additional details as needed for your GitHub repository. This README provides a structured summary of your project, emphasizing the data, methodology, results, and conclusion.
