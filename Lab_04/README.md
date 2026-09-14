# Airbnb Price Prediction - DS605 Lab Assignment 4

This project was completed as part of the DS605 - Fundamentals of Machine Learning course.

The aim of this project is to build an end-to-end machine learning workflow for predicting Airbnb nightly prices using the New York City Airbnb Open Data dataset.

## Dataset

Dataset used: `AB_NYC_2019.csv`

Source: Kaggle - New York City Airbnb Open Data

## Project Workflow

The project includes:

- Data loading and inspection
- Missing value handling
- Duplicate checking
- Outlier handling
- Feature engineering
- Feature selection
- Exploratory Data Analysis
- Data preprocessing
- Train-test split
- Categorical encoding
- Numerical scaling
- Model training
- Model comparison
- Overfitting and underfitting check
- Hyperparameter tuning
- Final model selection
- Model saving
- Streamlit application

## Models Used

Three regression models were compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### Initial Model Results

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 49.88 | 79.07 | 0.426 |
| Decision Tree | 60.67 | 101.45 | 0.054 |
| Random Forest | 44.92 | 72.89 | 0.512 |

Random Forest gave the best overall test performance.

## Overfitting Check

The Decision Tree strongly overfit the training data.

Random Forest also showed some overfitting, so hyperparameter tuning was performed.

## Final Tuned Model

The tuned Random Forest was selected as the final model.

Final performance:

- Train R²: 0.679
- Test R²: 0.527
- Train RMSE: 58.72
- Test RMSE: 71.72
- Test MAE: 43.81

The tuned model reduced the gap between training and testing performance compared with the original Random Forest.

## Streamlit Application

A Streamlit application was created to make the model easy to use.

The user can enter listing details such as:

- Neighbourhood group
- Neighbourhood
- Room type
- Latitude
- Longitude
- Minimum nights
- Number of reviews
- Reviews per month
- Host listings count
- Availability

The application returns the estimated nightly Airbnb price.

## Project Files

- `airbnb_price_prediction.ipynb` - Complete machine learning notebook
- `app.py` - Streamlit application
- `airbnb_price_pipeline.pkl` - Saved preprocessing and trained model pipeline
- `requirements.txt` - Required Python packages
- `AB_NYC_2019.csv` - Dataset
- `screenshots/` - Application and model result screenshots

## Screenshots

### Streamlit Application

![App Input](screenshots/app_input.png)

![App Prediction](screenshots/app_prediction.png)

### Model Results

![Model Results](screenshots/model_results.png)

![Overfitting Check](screenshots/overfitting_check.png)

![Final Model Results](screenshots/final_model_results.png)

## How to Run the Application

Install the required packages:

```bash
pip install -r requirements.txt
