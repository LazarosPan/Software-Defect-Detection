# Software Defect Detection

## 1. Introduction

Software defect detection is an essential application of machine learning, aiming to automatically identify defective components in programs. This project explores the performance of various classifiers on multiple software defect detection datasets to improve the accuracy and efficiency of identifying potential defects in software code.

## 2. Algorithms Used

The following machine learning algorithms were implemented and evaluated in this project:
- **Logistic Regression**
- **Perceptron**
- **Support Vector Machines (SVM)** (with linear and RBF kernel)
- **Decision Tree**
- **Random Forests**
- **Feed-forward Neural Network**

These classifiers were applied to three different software defect datasets to compare their ability to detect defects accurately.

## 3. Datasets

The datasets used for this project come from the domain of software defect prediction:
- `jm1`
- `mc1`
- `pc3`

Each dataset contains features related to software metrics and labels indicating whether a defect is present. Cases with missing values were handled by removing the respective rows to ensure data quality.

## 4. Experiments

The datasets were split into 80% training and 20% testing sets, and a 5-fold cross-validation technique was applied to evaluate model performance. For each classifier, performance was measured using the following metrics:
- **Accuracy**
- **F1-score**
- **G-Mean score**
- **Fit time**

To examine how feature scaling impacts the models, three different normalization techniques were applied:
- **No normalization** (raw features)
- **Min-max normalization**
- **Feature Standardization**

## 5. Results and Analysis

For each dataset, the performance of all classifiers was compared based on the aforementioned metrics. Bar plots were generated to visualize the comparison of classifier performance under different normalization methods.

A detailed discussion follows, highlighting the strengths and weaknesses of each classifier across the datasets. The results provide insights into which classifiers are most effective for software defect detection, and how different normalization methods impact their performance.

## 6. Conclusion

The study demonstrated that the choice of machine learning algorithms and data preprocessing techniques significantly impacts the performance of software defect detection. The Random Forest and Support Vector Machines, in particular, showed strong results across multiple metrics. Feature normalization also had a notable effect, with Feature Standardization improving performance for most classifiers.
