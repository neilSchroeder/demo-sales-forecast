"""
Example: Using the visualization module

This script demonstrates how to use the visualization utilities
to create interactive plots and dashboards.
"""

import sys
sys.path.append('../src')

import pandas as pd
from data_processing import load_sales_data, prepare_time_series
from visualization import (
    plot_time_series, 
    plot_forecast, 
    create_sales_dashboard
)

def main():
    print("="*80)
    print("VISUALIZATION MODULE EXAMPLES")
    print("="*80)
    
    # Load data
    print("\n1. Loading data...")
    df = load_sales_data('../data/superstore_sales.csv')
    print(f"   ✓ Loaded {len(df):,} records")
    
    # Example 1: Basic time series plot
    print("\n2. Creating time series plot...")
    daily_ts = prepare_time_series(df, freq='D')
    fig1 = plot_time_series(
        daily_ts, 
        title='Daily Sales - Example Visualization'
    )
    # Uncomment to display interactively:
    # fig1.show()
    print("   ✓ Time series plot created")
    print("   Tip: Call fig.show() to display interactively")
    print("   Tip: Call fig.write_html('output.html') to save")
    
    # Example 2: Sales dashboard
    print("\n3. Creating comprehensive dashboard...")
    dashboard = create_sales_dashboard(df)
    # Uncomment to display interactively:
    # dashboard.show()
    print("   ✓ Dashboard created with 4 subplots:")
    print("     - Daily sales trend")
    print("     - Sales by category")
    print("     - Sales by region")
    print("     - Monthly sales pattern")
    
    # Example 3: Forecast visualization (simulated)
    print("\n4. Creating forecast plot (simulated example)...")
    # Create mock forecast data for demonstration
    train_df = daily_ts.iloc[:1000].copy()
    test_df = daily_ts.iloc[1000:1100].copy()
    forecast_df = test_df.copy()
    forecast_df['yhat'] = forecast_df['y'] * 1.05  # Simulated prediction
    forecast_df['yhat_lower'] = forecast_df['yhat'] * 0.9
    forecast_df['yhat_upper'] = forecast_df['yhat'] * 1.1
    
    fig3 = plot_forecast(
        train_df.tail(200),
        test_df,
        forecast_df,
        title='Sales Forecast - Example'
    )
    # Uncomment to display:
    # fig3.show()
    print("   ✓ Forecast plot created")
    
    # Saving examples
    print("\n5. Saving visualizations...")
    print("   Examples:")
    print("   - fig.write_html('dashboard.html')")
    print("   - fig.write_image('plot.png')  # Requires kaleido")
    print("   - fig.to_json()  # For API responses")
    
    print("\n" + "="*80)
    print("EXAMPLES COMPLETE")
    print("="*80)
    print("\nNext steps:")
    print("  • Uncomment .show() calls to display plots interactively")
    print("  • Use .write_html() to save for sharing")
    print("  • Customize titles, colors, and layouts")
    print("  • Integrate into web applications or reports")


if __name__ == "__main__":
    main()
