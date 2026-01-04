# Quick Start Guide

## Installation (5 minutes)

```bash
# Clone the repository
git clone https://github.com/neilSchroeder/demo-sales-forecast.git
cd demo-sales-forecast

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Analysis

### Option 1: Jupyter Notebook (Recommended)

```bash
# Start Jupyter
jupyter notebook

# Navigate to notebooks/sales_forecasting_analysis.ipynb
# Run all cells (Cell > Run All)
```

### Option 2: Python Script

```bash
cd notebooks
python sales_forecasting_script.py
```

## What You'll Get

✅ **Exploratory Analysis**
- Summary statistics and key metrics
- Sales distribution by category and region
- Interactive dashboards

✅ **Time Series Analysis**
- Trend and seasonality decomposition
- Stationarity testing
- Pattern identification

✅ **Forecasting**
- Prophet model with 90-day validation
- 180-day future forecast
- Performance metrics (MAE, RMSE, MAPE)

✅ **Business Insights**
- Inventory management recommendations
- Staffing optimization strategies
- Marketing campaign timing
- Financial planning guidance

## Expected Output

### Key Metrics
- Total Sales: ~$15.3M
- Profit Margin: ~22.5%
- Model Accuracy: MAPE < 15%

### Visualizations
- Time series plots with trends
- Seasonal decomposition charts
- Forecast with confidence intervals
- Interactive dashboards

## Next Steps

1. **Customize**: Modify model parameters in the notebook
2. **Extend**: Add category or regional forecasts
3. **Deploy**: Build automated forecasting pipeline
4. **Share**: Present insights to stakeholders

## Troubleshooting

### Prophet Installation Issues
If you encounter issues installing Prophet:
```bash
# For macOS
brew install cmake
pip install prophet

# For Linux
sudo apt-get install python3-dev
pip install prophet

# For Windows
conda install -c conda-forge prophet
```

### Jupyter Not Found
```bash
pip install jupyter
jupyter notebook
```

## Support

- Open an issue on GitHub
- Check the main README for detailed documentation
- Review the CONTRIBUTING.md for development guidelines
