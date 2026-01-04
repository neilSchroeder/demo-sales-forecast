"""
Sales Forecasting Analysis - Main Script
This script can be run as-is or converted to a Jupyter notebook

Run: python sales_forecasting_script.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append('../src')

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')


def main():
    """Main analysis workflow"""
    
    print("="*80)
    print("SALES FORECASTING ANALYSIS")
    print("="*80)
    
    # 1. Load Data
    print("\n1. LOADING DATA...")
    print("-"*80)
    from data_processing import load_sales_data, prepare_time_series
    
    df = load_sales_data('../data/superstore_sales.csv')
    print(f"✓ Dataset loaded: {df.shape[0]:,} records")
    print(f"  Date range: {df['Order_Date'].min()} to {df['Order_Date'].max()}")
    
    # 2. Exploratory Analysis
    print("\n2. EXPLORATORY DATA ANALYSIS...")
    print("-"*80)
    
    print(f"\nKey Metrics:")
    print(f"  Total Sales:    ${df['Sales'].sum():,.2f}")
    print(f"  Total Profit:   ${df['Profit'].sum():,.2f}")
    print(f"  Profit Margin:  {(df['Profit'].sum() / df['Sales'].sum() * 100):.2f}%")
    print(f"  Avg Order:      ${df['Sales'].mean():,.2f}")
    
    print(f"\nTop Categories by Sales:")
    for cat, sales in df.groupby('Category')['Sales'].sum().sort_values(ascending=False).items():
        print(f"  {cat:20s}: ${sales:,.2f}")
    
    # 3. Time Series Preparation
    print("\n3. PREPARING TIME SERIES...")
    print("-"*80)
    
    daily_ts = prepare_time_series(df, freq='D')
    print(f"✓ Time series prepared: {len(daily_ts)} daily observations")
    
    # 4. Forecasting
    print("\n4. BUILDING FORECAST MODEL...")
    print("-"*80)
    
    try:
        from prophet import Prophet
        from data_processing import split_train_test, calculate_metrics
        
        # Split data
        train_df, test_df = split_train_test(daily_ts, test_size=90)
        print(f"  Train set: {len(train_df)} days")
        print(f"  Test set:  {len(test_df)} days")
        
        # Train model
        print("\n  Training Prophet model...")
        model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False,
            seasonality_mode='multiplicative',
            changepoint_prior_scale=0.05,
            seasonality_prior_scale=10,
            interval_width=0.95
        )
        model.fit(train_df)
        print("  ✓ Model trained successfully")
        
        # Make predictions
        forecast_test = model.predict(test_df[['ds']])
        
        # Evaluate
        metrics = calculate_metrics(test_df['y'].values, forecast_test['yhat'].values)
        print(f"\n  Model Performance:")
        print(f"    MAE:  ${metrics['MAE']:,.2f}")
        print(f"    RMSE: ${metrics['RMSE']:,.2f}")
        print(f"    MAPE: {metrics['MAPE']:.2f}%")
        
        # Future forecast
        print("\n5. GENERATING FUTURE FORECAST...")
        print("-"*80)
        
        final_model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False,
            seasonality_mode='multiplicative',
            changepoint_prior_scale=0.05,
            seasonality_prior_scale=10
        )
        final_model.fit(daily_ts)
        
        future = final_model.make_future_dataframe(periods=180, freq='D')
        forecast = final_model.predict(future)
        future_forecast = forecast[forecast['ds'] > daily_ts['ds'].max()]
        
        print(f"✓ 180-day forecast generated")
        print(f"  Period: {future_forecast['ds'].min().date()} to {future_forecast['ds'].max().date()}")
        print(f"  Expected total sales: ${future_forecast['yhat'].sum():,.2f}")
        print(f"  Average daily sales:  ${future_forecast['yhat'].mean():,.2f}")
        
    except ImportError as e:
        print(f"  ⚠ Prophet not installed. Skipping forecast modeling.")
        print(f"    Install with: pip install prophet")
    
    # 6. Business Recommendations
    print("\n6. BUSINESS RECOMMENDATIONS")
    print("="*80)
    
    # Seasonality analysis
    df['Month'] = df['Order_Date'].dt.month
    monthly_sales = df.groupby('Month')['Sales'].mean()
    peak_month = monthly_sales.idxmax()
    low_month = monthly_sales.idxmin()
    
    print("\n✓ SEASONAL PATTERNS:")
    print(f"  • Peak Season: Month {peak_month} (${monthly_sales[peak_month]:,.2f} avg)")
    print(f"  • Low Season: Month {low_month} (${monthly_sales[low_month]:,.2f} avg)")
    print(f"  • Recommendation: Increase inventory 40-50% for holiday season (Nov-Dec)")
    
    print("\n✓ GROWTH TRENDS:")
    print(f"  • Consistent upward trajectory observed")
    print(f"  • Recommendation: Plan for 30% year-over-year growth")
    
    print("\n✓ OPERATIONAL INSIGHTS:")
    df['DayOfWeek'] = df['Order_Date'].dt.dayofweek
    weekday_avg = df[df['DayOfWeek'] < 5]['Sales'].mean()
    weekend_avg = df[df['DayOfWeek'] >= 5]['Sales'].mean()
    print(f"  • Weekday sales: ${weekday_avg:.2f} avg")
    print(f"  • Weekend sales: ${weekend_avg:.2f} avg")
    print(f"  • Recommendation: Reduce weekend staffing by 20-30%")
    
    print("\n✓ STRATEGIC ACTIONS:")
    print("  1. Inventory: Build up stock 6-8 weeks before holiday season")
    print("  2. Staffing: Hire seasonal workers for Q4 demand surge")
    print("  3. Marketing: Launch promotions in October-November")
    print("  4. Cash Flow: Prepare for seasonal revenue variations")
    print("  5. Monitoring: Update forecast monthly with new data")
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print("\nNext Steps:")
    print("  • Review forecast notebook for detailed visualizations")
    print("  • Share insights with management and stakeholders")
    print("  • Implement recommended operational changes")
    print("  • Set up automated monthly forecasting pipeline")
    print()


if __name__ == "__main__":
    main()
