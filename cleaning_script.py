import pandas as pd

# Load dataset
df = pd.read_excel(r"C:\Users\HP\Downloads\ApexPlanet_Dataset.xlsx")

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Handle missing Age values using the median
age_median = df["Age"].median()
df["Age"] = df["Age"].fillna(age_median)

# Handle missing City values
df["City"] = df["City"].fillna("Unknown")

# Standardize text columns by removing leading/trailing spaces
text_columns = [
    "Order_ID",
    "Customer_ID",
    "Customer_Name",
    "Gender",
    "City",
    "Product",
    "Category"
]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

# Convert Age to integer
df["Age"] = df["Age"].astype(int)

# Check for exact duplicate rows
duplicate_count = df.duplicated().sum()
print("Exact duplicate rows:", duplicate_count)

# Validate Total_Sales
calculated_sales = df["Quantity"] * df["Unit_Price"]
sales_match = (
    df["Total_Sales"].round(2)
    == calculated_sales.round(2)
)

print("Sales calculation mismatches:", (~sales_match).sum())

# Final validation
print("Final dataset shape:", df.shape)
print("Total missing values:", df.isnull().sum().sum())

# Export cleaned dataset
df.to_csv("cleaned_sales_data_ApexPlanet.csv", index=False)

print("Cleaned dataset exported successfully!")
