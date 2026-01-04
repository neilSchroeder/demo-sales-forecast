# Data Directory

## Dataset: Superstore Sales

**File:** `superstore_sales.csv`

### Description
This dataset contains retail sales data for a fictional superstore chain spanning 4 years (2020-2023). The data includes order-level information with temporal patterns, seasonality, and business metrics suitable for time series forecasting.

### Data Dictionary

| Column | Type | Description |
|--------|------|-------------|
| Order_ID | String | Unique identifier for each order |
| Order_Date | Date | Date when the order was placed |
| Category | String | Product category (Technology, Furniture, Office Supplies) |
| Sub_Category | String | Product sub-category |
| Region | String | Geographic region (East, West, Central, South) |
| Segment | String | Customer segment (Consumer, Corporate, Home Office) |
| Sales | Float | Sales amount in USD |
| Quantity | Integer | Number of items ordered |
| Profit | Float | Profit amount in USD |
| Discount | Float | Discount percentage applied |

### Dataset Statistics
- **Records:** ~19,000 orders
- **Date Range:** January 1, 2020 - December 31, 2023
- **Total Sales:** ~$15M USD
- **Patterns:** Includes seasonal trends, holiday effects, and growth patterns

### Data Characteristics
- **Seasonality:** Strong end-of-year patterns (November-December holiday season)
- **Trend:** Positive growth trend over the 4-year period
- **Weekday Effects:** Lower sales on weekends
- **Category Distribution:** Mixed across Technology, Furniture, and Office Supplies

### Usage
This data is suitable for:
- Time series forecasting and analysis
- Seasonality decomposition
- Sales trend analysis
- Business intelligence and reporting
- Machine learning model training
