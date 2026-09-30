202618055
# DS605 Lab Assignment 6

## Feature Extraction and Machine Learning with Image and Text Data

This repository contains the implementation of Lab Assignment 6 for DS605: Fundamentals of Machine Learning.

The assignment focuses on converting raw image and text data into numerical feature representations and applying traditional machine-learning models for classification.

---

## Part A - Asphalt Crack Classification

### Dataset
Asphalt Crack Dataset containing 400 images:

- 200 Crack images
- 200 Non-Crack images

### Image Preprocessing

The images were:

- Loaded using OpenCV
- Resized to 256 × 256
- Converted to grayscale
- Smoothed using Gaussian Blur
- Processed using Canny Edge Detection

### Extracted Features

The following numerical features were extracted from each image:

- Mean brightness
- Contrast
- Minimum intensity
- Maximum intensity
- Median intensity
- 25th percentile
- 75th percentile
- Interquartile range
- Dark-pixel ratio
- Bright-pixel ratio
- Intensity range
- Edge count
- Edge density

One numerical feature row was generated for every image.

### Machine Learning Models

The following traditional classifiers were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest

Performance was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Training Time
- Prediction Time

---

## Part B - Email Spam Classification

### Dataset

Email Spam Classification Dataset containing:

- 5,172 emails
- 3,672 Non-Spam emails
- 1,500 Spam emails
- 3,000 word-based numerical features

The dataset contains a sparse word-count representation of the emails.

### Models

The following classifiers were evaluated:

- Multinomial Naive Bayes
- Logistic Regression

### Results

Logistic Regression achieved higher classification performance, while Multinomial Naive Bayes required less computation.

Both models were evaluated using accuracy, precision, recall, F1-score, confusion matrix, training time, and prediction time.

---

## Part C - Representation Improvement

Chi-square feature selection was applied using `SelectKBest`.

The original representation contained:

- 3,000 features

The reduced representation contained:

- 1,000 features

The reduced representation significantly decreased training and prediction time while maintaining similar classification performance.

This demonstrates the trade-off between:

- Feature dimensionality
- Computational cost
- Classification performance

---

## Libraries Used

- NumPy
- Pandas
- OpenCV
- Matplotlib
- Scikit-learn

---

## Repository Files

- `Lab6.ipynb` - Complete implementation
- `image_features.csv` - Extracted image feature table
- `emails.csv` - Email spam dataset
- `dataset/` - Asphalt image dataset
- `README.md` - Assignment summary

---

## Important Requirement

Only traditional machine-learning methods were used.

No CNNs, deep-learning models, or pretrained image embeddings were used.