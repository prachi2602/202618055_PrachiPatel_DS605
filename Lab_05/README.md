# DS605 - Fundamentals of Machine Learning
## Lab Assignment 5

### Machine Learning with Scikit-learn and From Scratch

This project implements Linear Regression and Logistic Regression using both Scikit-learn and manual NumPy/Pandas implementations.

The models are trained and evaluated using the UCI Productivity Prediction of Garment Employees dataset.

---

## Dataset

Dataset: UCI Productivity Prediction of Garment Employees

The dataset contains garment production information such as:

- Department
- Team
- Targeted productivity
- Standard minute value
- Work in progress
- Overtime
- Incentives
- Number of workers
- Actual productivity

---

## Targets

### Regression

The regression task predicts:

`actual_productivity`

using Linear Regression.

### Classification

A new binary target called `MeetsTarget` was created.

`MeetsTarget = 1` when:

`actual_productivity >= targeted_productivity`

Otherwise:

`MeetsTarget = 0`

Logistic Regression is used for this classification task.

---

## Part A - Scikit-learn Implementation

The Scikit-learn workflow includes:

- Missing-value handling
- Categorical feature encoding
- Feature scaling
- Fixed train-test split
- Linear Regression
- Logistic Regression
- Training and prediction time measurement
- Regression and classification evaluation

Regression metrics:

- MAE
- RMSE
- R²

Classification metrics:

- Accuracy
- Precision
- Recall
- F1-score

---

## Part B - From-Scratch Implementation

The complete workflow was recreated using NumPy and Pandas.

The manual implementation includes:

- Missing-value handling
- One-hot encoding
- Feature scaling
- Linear Regression using a closed-form solution
- Logistic Regression using gradient descent
- Sigmoid function
- Probability prediction
- Classification thresholding
- Manual calculation of evaluation metrics

The same train-test samples from Part A were reused to ensure a fair comparison.

---

## Part C - Comparison and Optimization

The Scikit-learn and manual implementations were compared using predictive metrics, training time, and prediction time.

The manual Logistic Regression model was optimized by testing different learning rates and iteration settings.

The original manual model achieved approximately:

- Accuracy: 0.7375
- F1-score: 0.8475

The optimized manual model achieved approximately:

- Accuracy: 0.7542
- Precision: 0.7566
- Recall: 0.9771
- F1-score: 0.8529

The optimized model used:

- Learning rate: 0.01
- Maximum iterations: 5000

A convergence experiment was also performed. The model converged after 12,759 iterations with a tolerance of 1e-6, but its test performance was slightly lower and its training time was much higher.

Therefore, the 5000-iteration configuration was retained as the final optimized manual Logistic Regression model.

---

## Key Observations

1. The manual Linear Regression implementation produced almost identical MAE, RMSE, and R² values compared with Scikit-learn.

2. The from-scratch Logistic Regression implementation successfully reproduced the complete classification workflow using NumPy and Pandas.

3. Learning-rate and iteration tuning improved the manual Logistic Regression performance.

4. Convergence did not necessarily produce better test-set performance.

5. Scikit-learn was significantly more efficient for training Logistic Regression, while the optimized manual implementation achieved competitive predictive performance.

---

## Requirements

The project uses:

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook

---

## Files

- `Lab5.ipynb` - Complete implementation
- `garments_worker_productivity.csv` - Dataset
- `README.md` - Project documentation

