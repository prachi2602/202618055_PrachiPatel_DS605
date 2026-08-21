Use this in your `README.md`:

# Lab Assignment 3

## Scikit-learn: Data Preprocessing and Model Performance Evaluation

**Name:** Prachi Patel
**ID:** 202618055

## Dataset

Kaggle Hotel Booking Demand Dataset
Dataset Link: [https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

## Objective

The objective of this lab is to build and compare Scikit-learn preprocessing pipelines and evaluate Logistic Regression and Decision Tree classification models for predicting hotel booking cancellations.

## Preprocessing

* `is_canceled` was used as the target variable.
* `company` was removed because around 94.31% of its values were missing.
* `reservation_status` and `reservation_status_date` were removed to avoid target leakage.
* Clear extreme outliers were removed after inspecting numerical features.
* Numerical missing values were handled using `KNNImputer(n_neighbors=5)`.
* Categorical missing values were handled using `SimpleImputer(strategy="most_frequent")`.
* Categorical variables were encoded using `OneHotEncoder(handle_unknown="ignore")`.
* Pipeline A used `StandardScaler`.
* Pipeline B used `MinMaxScaler`.
* The data was split using an 80:20 train-test split with stratification and `random_state=42`.

## Models

Two classification models were compared using both preprocessing pipelines:

1. Logistic Regression with StandardScaler
2. Logistic Regression with MinMaxScaler
3. Decision Tree with StandardScaler
4. Decision Tree with MinMaxScaler

## Final Observations

1. Among all four combinations, the Decision Tree with StandardScaler gave the best overall performance, with around 86.24% testing accuracy and an F1-score of 81.53%.

2. In Logistic Regression, StandardScaler performed slightly better than MinMaxScaler. The difference was small, but StandardScaler gave slightly higher testing accuracy and F1-score.

3. For the Decision Tree, changing from StandardScaler to MinMaxScaler did not make much difference. The results were almost identical in both cases.

4. The Decision Tree was better at identifying canceled bookings, with recall of around 82%, compared with around 67% for the best Logistic Regression model.

5. The Decision Tree showed signs of overfitting because its training accuracy was about 99.62%, while its testing accuracy was about 86.24%. Logistic Regression showed a much smaller difference between training and testing accuracy.



