# 📊 Sales Forecasting Portfolio Project

A comprehensive time series forecasting analysis for retail sales data using Facebook Prophet and advanced analytics techniques.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Project Overview

This portfolio project demonstrates end-to-end sales forecasting capabilities for a Superstore retail chain. The analysis provides actionable insights for inventory management, staffing optimization, and strategic business planning.

### Key Features

- **📈 Time Series Analysis**: Comprehensive exploration of 4 years of daily sales data
- **🔮 Forecasting Models**: Facebook Prophet implementation with seasonal decomposition
- **📊 Interactive Dashboards**: Plotly visualizations for stakeholder communication
- **💡 Business Recommendations**: Data-driven insights for operational decisions
- **🎯 High Accuracy**: MAPE < 15% on test data

## 🗂️ Project Structure

```
demo-sales-forecast/
├── data/                           # Data directory
│   ├── superstore_sales.csv       # Retail sales dataset (4 years)
│   └── README.md                  # Data documentation
├── notebooks/                      # Jupyter notebooks
│   ├── sales_forecasting_analysis.ipynb  # Main analysis notebook
│   └── sales_forecasting_script.py       # Python script version
├── src/                            # Source code modules
│   ├── __init__.py
│   ├── data_processing.py         # Data loading and preparation utilities
│   └── visualization.py           # Plotting and dashboard functions
├── requirements.txt                # Python dependencies
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Jupyter Notebook (for interactive analysis)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/neilSchroeder/demo-sales-forecast.git
   cd demo-sales-forecast
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

5. **Open the analysis notebook**
   - Navigate to `notebooks/sales_forecasting_analysis.ipynb`
   - Run all cells to reproduce the analysis

### Quick Run (Script Version)

For a quick text-based analysis without Jupyter:

```bash
cd notebooks
python sales_forecasting_script.py
```

## 📊 Dataset

The project uses a synthetic Superstore sales dataset with the following characteristics:

- **Time Period**: 2020-2023 (4 years)
- **Records**: ~19,000 orders
- **Features**: Order Date, Category, Region, Segment, Sales, Profit, Quantity, Discount
- **Patterns**: Seasonal trends, holiday effects, weekday/weekend variations

See `data/README.md` for detailed data documentation.

## 🔬 Analysis Workflow

### 1. Exploratory Data Analysis
- Summary statistics and data quality checks
- Sales distribution by category, region, and segment
- Trend and seasonality visualization

### 2. Time Series Analysis
- Stationarity testing (Augmented Dickey-Fuller)
- Seasonal decomposition (trend, seasonal, residual)
- Monthly and weekly pattern identification

### 3. Forecasting Model
- **Model**: Facebook Prophet
- **Features**: 
  - Yearly seasonality (holiday effects)
  - Weekly seasonality (weekday patterns)
  - Multiplicative seasonality mode
  - 95% confidence intervals
- **Validation**: 90-day test set with performance metrics

### 4. Business Insights
- Inventory management recommendations
- Staffing optimization strategies
- Marketing campaign timing
- Financial planning guidance

## 📈 Key Findings

### Seasonal Patterns
- 📅 **Peak Season**: November-December (40-50% higher sales)
- 📉 **Low Season**: January-February (post-holiday dip)
- 📆 **Weekly Trend**: 30% lower sales on weekends

### Growth Trends
- 📈 **Overall Growth**: 30% increase over 4 years
- ✅ **Consistency**: Steady upward trajectory
- 🎯 **Predictability**: Strong seasonal patterns enable accurate forecasting

### Model Performance
- 🎯 **MAPE**: < 15% (high accuracy)
- 📊 **MAE**: Average prediction error within acceptable range
- ✅ **Validation**: Strong performance on unseen test data

## 💼 Business Recommendations

### Inventory Management
- Increase stock 40-50% for November-December
- Reduce inventory in January-February to minimize holding costs
- Maintain safety stock for high-demand Technology products

### Staffing Optimization
- Hire 30-40% more staff for holiday season
- Reduce weekend staff by 20-30%
- Implement flexible workforce for peak periods

### Marketing Strategy
- Launch aggressive campaigns in October-November
- Introduce "New Year" sales for January recovery
- Focus marketing efforts on weekdays

### Financial Planning
- Use forecasts for quarterly revenue planning
- Prepare for seasonal cash flow variations
- Align budgets with predicted demand patterns

## 🛠️ Technologies Used

- **Data Processing**: pandas, numpy
- **Forecasting**: Facebook Prophet, statsmodels
- **Visualization**: matplotlib, seaborn, plotly
- **Development**: Jupyter Notebook, Python 3.8+

## 📚 Key Modules

### `src/data_processing.py`
Utilities for data loading, time series preparation, train/test splitting, and metric calculation.

### `src/visualization.py`
Functions for creating interactive time series plots, forecast visualizations, and sales dashboards using Plotly.

## 🔮 Future Enhancements

- [ ] Category-specific forecasting models
- [ ] Regional forecast breakdowns
- [ ] Promotional impact analysis
- [ ] External factor integration (economic indicators)
- [ ] Automated forecasting pipeline
- [ ] Real-time dashboard deployment
- [ ] ARIMA/SARIMA model comparison

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Neil Schroeder**

- GitHub: [@neilSchroeder](https://github.com/neilSchroeder)

## 🙏 Acknowledgments

- Dataset inspired by the popular Superstore dataset
- Facebook Prophet for robust forecasting capabilities
- Plotly for interactive visualizations

## 📧 Contact

For questions, feedback, or collaboration opportunities, please open an issue or reach out through GitHub.

---

**⭐ If you find this project helpful, please consider giving it a star!**