# Missing Value Handling – House Prices & Medical Appointment Datasets

## 📌 Project Overview

This project demonstrates how missing values are identified, visualized, and handled using Python for two datasets: **House Prices Dataset** and **Medical Appointment No Shows Dataset**. The goal is to improve data quality before applying any machine learning or analysis tasks.

## 🛠 Tools Used

* Python
* Pandas
* NumPy
* Matplotlib (for visualization)

## Datasets Used

* **House Prices Dataset**
* **Medical Appointment No Shows Dataset**

---

## Steps Performed

### 1. Load Dataset

Both datasets were loaded using Pandas and inspected to understand their structure.

### 2. Identify Missing Values

Missing values were detected using:
`df.isnull().sum()`

This helped identify columns with null entries.

### 3. Visualize Missing Data

Simple bar charts were created to visualize the number of missing values in each column.

### 4. Numerical Data Imputation

For numerical columns:

* **Mean Imputation** was applied where data was normally distributed.
* **Median Imputation** was used where outliers were present.

### 5. Categorical Data Imputation

For categorical columns, missing values were replaced using the **Mode (most frequent value)**.

### 6. Remove Highly Missing Columns

Columns having extremely high missing values (more than 50%) were removed to maintain data quality.

### 7. Dataset Validation

After cleaning, the dataset was rechecked to confirm that missing values were handled properly.

### 8. Before vs After Comparison

The dataset size and missing value count were compared before and after cleaning to verify improvements in data quality.

---

## Results

* Missing values were successfully handled
* Dataset became cleaner and more consistent
* Improved data quality for further analysis and machine learning tasks
