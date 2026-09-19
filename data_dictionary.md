# Data Dictionary

| Column Name   | Description                                | Data Type   | Business Relevance                                        |
| ------------- | ------------------------------------------ | ----------- | --------------------------------------------------------- |
| Order_ID      | Transaction/order reference identifier     | Object      | Used to identify and track transaction records            |
| Order_Date    | Date on which the transaction occurred     | Datetime    | Useful for analyzing sales over time                      |
| Customer_ID   | Identifier assigned to the customer        | Object      | Used for customer-level analysis                          |
| Customer_Name | Name or label associated with the customer | Object      | Provides customer reference information                   |
| Age           | Age of the customer in years               | Integer     | Useful for demographic and customer segmentation analysis |
| Gender        | Gender category of the customer            | Categorical | Useful for demographic analysis                           |
| City          | Customer's city or location                | Categorical | Useful for geographic analysis                            |
| Product       | Product purchased by the customer          | Categorical | Used for product-level sales analysis                     |
| Category      | Category to which the product belongs      | Categorical | Useful for category-level sales analysis                  |
| Quantity      | Number of units purchased                  | Integer     | Used to measure sales volume                              |
| Unit_Price    | Price of one unit of the product           | Float       | Used for pricing and sales calculations                   |
| Total_Sales   | Total value of the transaction             | Float       | Used to analyze sales/revenue performance                 |
