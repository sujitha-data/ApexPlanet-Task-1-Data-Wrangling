# ApexPlanet Data Analytics Internship — Task 1

## Data Immersion & Wrangling

### Overview

This project was completed as part of the **ApexPlanet Software Pvt. Ltd. Data Analytics Internship**.

The objective of Task 1 was to understand the provided sales transaction dataset, assess its data quality, perform data cleaning and transformation, and prepare an analysis-ready dataset using Python and Pandas.

## Dataset

The dataset contains **1,000 transaction records and 12 columns** covering:

* Order information
* Customer information
* Demographic information
* Product and category details
* Quantity and pricing
* Total sales

### Columns

`Order_ID`, `Order_Date`, `Customer_ID`, `Customer_Name`, `Age`, `Gender`, `City`, `Product`, `Category`, `Quantity`, `Unit_Price`, `Total_Sales`

## Data Quality Assessment

The following checks were performed:

* Missing-value assessment
* Exact duplicate-row check
* Repeated `Order_ID` investigation
* Data-type validation
* Categorical-value validation
* Text-formatting checks
* Date validation
* Numerical-statistics assessment
* Outlier assessment
* Sales calculation validation

### Issues Identified

* 20 missing values were found in `Age`.
* 13 missing values were found in `City`.
* No exact duplicate rows were identified.
* `ORD100050` appeared multiple times, but the associated records contained different transaction details and were therefore retained.
* 19 potential statistical outliers were identified in `Total_Sales` using the IQR method.
* The potential sales outliers were retained because they were consistent with `Quantity × Unit_Price`.
* No obvious categorical spelling or capitalization inconsistencies were identified.

## Data Cleaning

The following cleaning steps were performed:

1. Converted `Order_Date` to datetime format and validated the resulting dates.
2. Filled missing `Age` values using the median age of **41**.
3. Replaced missing `City` values with **`Unknown`**.
4. Removed leading and trailing spaces from text columns.
5. Converted `Age` to integer format.
6. Checked for exact duplicate rows.
7. Validated `Total_Sales` against `Quantity × Unit_Price`.

## Sales Validation

The `Total_Sales` column was independently validated using:

`Quantity × Unit_Price`

All **1,000 records** matched after rounding to two decimal places.

## Final Dataset

After cleaning:

* **Rows:** 1,000
* **Columns:** 12
* **Missing values:** 0
* **Exact duplicate rows:** 0
* **Order_Date:** `datetime64[ns]`
* **Age:** `int64`
* **Quantity:** `int64`
* **Unit_Price:** `float64`
* **Total_Sales:** `float64`

The resulting dataset is ready for further analysis.

## Repository Contents

```text
Task-1-Data-Immersion-Wrangling/
│
├── Task_1_Data_Immersion_Wrangling.ipynb
├── cleaned_sales_data_ApexPlanet.csv
├── data_dictionary.md
├── cleaning_script.py
└── README.md
```

## Tools Used

* Python
* Pandas
* Jupyter Notebook
* GitHub

## Deliverables

This repository contains the completed materials for **ApexPlanet Task 1 — Data Immersion & Wrangling**, including the notebook, data dictionary, cleaning script, and cleaned dataset.
