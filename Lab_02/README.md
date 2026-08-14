# Lab 2 - NumPy and Pandas

## Student Details

**Name:** Prachi Patel  
**Student ID:** 202618055  

## Assignment

Lab 2 - Vectorized Programming with NumPy and Data Wrangling with Pandas

## Dataset

Kaggle Titanic Dataset - `train.csv`

## Objective

The objective of this assignment is to practice vectorized programming using NumPy and perform basic data wrangling, filtering, aggregation, missing-value handling, feature engineering, and visualization using Pandas.

## Part A - Vectorized Programming with NumPy

### Task 1 - Arrays, Statistics, and Indexing

- Generated random NumPy arrays.
- Calculated minimum, maximum, median, mean, and standard deviation.
- Used `np.arange()`, `np.zeros()`, `np.ones()`, and `np.linspace()`.
- Created and explored 2D and 3D arrays.
- Performed indexing and slicing.
- Used `reshape()` and `flatten()`.

### Task 2 - Vectorized Arithmetic and Linear Algebra

- Matrix addition.
- Element-wise multiplication.
- Matrix multiplication.
- Matrix transpose.
- Determinant.
- Matrix inverse.
- Verified the inverse using `np.allclose()`.

All operations were performed using vectorized NumPy operations without explicit Python loops.

### Task 3 - Normal Distribution and Histogram

- Generated 1,000 values from a normal distribution.
- Compared chosen mean and standard deviation with sample values.
- Plotted a histogram of the generated data.

## Part B - Data Wrangling with Pandas

### Task 4 - Load and Inspect Data

Used:

- `head()`
- `tail()`
- `shape`
- `columns`
- `info()`
- `describe()`
- `loc`
- `iloc`

### Task 5 - Filtering and Querying

Boolean indexing was used to answer questions based on passenger age, sex, class, fare, survival status, embarkation point, and family information.

### Task 6 - GroupBy and Aggregation

Analyzed:

- Survival rate by Sex.
- Survival rate by Pclass.
- Average Age and Fare by Pclass.
- Passenger count and survival rate by Sex-Pclass.
- Passenger count, average Fare, and survival rate by Embarked.

### Task 7 - Missing Values and Fare Outliers

- Calculated missing-value count and percentage.
- Plotted missing-value counts.
- Filled missing Age values.
- Tried mean, median, mode, and random-value imputation.
- Detected Fare outliers using the 1.5 × IQR method.

### Task 8 - Feature Engineering and Pivot Table

Created:

- `FamilySize`
- `IsAlone`

A pivot table was created using Sex as rows, Pclass as columns, and mean Survived as values.

### Task 9 - Visualizations

Created:

- Correlation heatmap.
- Survival rate by Sex plot.
- Age vs Fare scatter plot.
- Normal distribution histogram.
- Missing-value bar chart.

## Key Observations

## Key Observations

1. The overall survival rate in the Titanic dataset was **38.38%**.

2. Female passengers had a much higher survival rate of **74.20%**, compared with only **18.89%** for male passengers.

3. Survival rate decreased as passenger class became lower. First-class passengers had the highest survival rate at **62.96%**, followed by second class at **47.28%**, while third-class passengers had the lowest survival rate at **24.24%**.

4. First-class passengers also paid a much higher average Fare of **84.15**, compared with **20.66** for second class and **13.68** for third class.

5. Passengers travelling with family had a survival rate of **50.56%**, while passengers travelling alone had a lower survival rate of **30.35%**.

6. The results suggest that both **Sex and Pclass were strongly associated with survival**, with female and higher-class passengers showing better survival outcomes.

7. The difference between passengers travelling alone and those travelling with family suggests that family presence may also have been associated with survival outcome.

## Project Files

- `Lab_2_NumPy_Pandas.ipynb` - Complete assignment notebook.
- `train.csv` - Original Titanic dataset.
- `titanic_cleaned.csv` - Cleaned Titanic dataset.
- `figures/` - Generated visualizations.
- `README.md` - Project documentation.

## Libraries Used

- NumPy
- Pandas
- Matplotlib
- Seaborn

## How to Run

1. Clone or download this repository.
2. Open `Lab_2_NumPy_Pandas.ipynb`.
3. Make sure NumPy, Pandas, Matplotlib, and Seaborn are installed.
4. Run all notebook cells from top to bottom.