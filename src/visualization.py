"""
Visualization utilities for sales forecasting.
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from typing import Optional


def plot_time_series(df: pd.DataFrame, 
                     date_col: str = 'ds', 
                     value_col: str = 'y',
                     title: str = 'Sales Time Series') -> go.Figure:
    """
    Create an interactive time series plot.
    
    Args:
        df: DataFrame with time series data
        date_col: Name of date column
        value_col: Name of value column
        title: Plot title
        
    Returns:
        Plotly figure object
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df[date_col],
        y=df[value_col],
        mode='lines',
        name='Sales',
        line=dict(color='#1f77b4', width=1)
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title='Date',
        yaxis_title='Sales ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400
    )
    
    return fig


def plot_forecast(train_df: pd.DataFrame,
                 test_df: pd.DataFrame,
                 forecast_df: pd.DataFrame,
                 title: str = 'Sales Forecast') -> go.Figure:
    """
    Create an interactive forecast plot with confidence intervals.
    
    Args:
        train_df: Training data
        test_df: Test data (actual values)
        forecast_df: Forecast predictions with confidence intervals
        title: Plot title
        
    Returns:
        Plotly figure object
    """
    fig = go.Figure()
    
    # Historical data
    fig.add_trace(go.Scatter(
        x=train_df['ds'],
        y=train_df['y'],
        mode='lines',
        name='Historical',
        line=dict(color='#1f77b4', width=2)
    ))
    
    # Actual test data
    if test_df is not None and len(test_df) > 0:
        fig.add_trace(go.Scatter(
            x=test_df['ds'],
            y=test_df['y'],
            mode='lines',
            name='Actual',
            line=dict(color='#2ca02c', width=2)
        ))
    
    # Forecast
    fig.add_trace(go.Scatter(
        x=forecast_df['ds'],
        y=forecast_df['yhat'],
        mode='lines',
        name='Forecast',
        line=dict(color='#ff7f0e', width=2, dash='dash')
    ))
    
    # Confidence interval
    if 'yhat_lower' in forecast_df.columns and 'yhat_upper' in forecast_df.columns:
        fig.add_trace(go.Scatter(
            x=forecast_df['ds'],
            y=forecast_df['yhat_upper'],
            mode='lines',
            line=dict(width=0),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        fig.add_trace(go.Scatter(
            x=forecast_df['ds'],
            y=forecast_df['yhat_lower'],
            mode='lines',
            line=dict(width=0),
            fillcolor='rgba(255, 127, 14, 0.2)',
            fill='tonexty',
            name='95% Confidence',
            hoverinfo='skip'
        ))
    
    fig.update_layout(
        title=title,
        xaxis_title='Date',
        yaxis_title='Sales ($)',
        hovermode='x unified',
        template='plotly_white',
        height=500
    )
    
    return fig


def plot_components(forecast_df: pd.DataFrame,
                   components: list = ['trend', 'yearly', 'weekly']) -> go.Figure:
    """
    Plot forecast components (trend, seasonality).
    
    Args:
        forecast_df: Forecast DataFrame with components
        components: List of components to plot
        
    Returns:
        Plotly figure with subplots
    """
    available_components = [c for c in components if c in forecast_df.columns]
    n_components = len(available_components)
    
    fig = make_subplots(
        rows=n_components, 
        cols=1,
        subplot_titles=[c.capitalize() for c in available_components],
        vertical_spacing=0.1
    )
    
    for i, component in enumerate(available_components, 1):
        fig.add_trace(
            go.Scatter(
                x=forecast_df['ds'],
                y=forecast_df[component],
                mode='lines',
                name=component.capitalize(),
                line=dict(width=2)
            ),
            row=i, col=1
        )
    
    fig.update_layout(
        height=300 * n_components,
        showlegend=False,
        template='plotly_white'
    )
    
    return fig


def create_sales_dashboard(df: pd.DataFrame) -> go.Figure:
    """
    Create an interactive sales dashboard with multiple metrics.
    
    Args:
        df: Sales DataFrame
        
    Returns:
        Plotly figure with dashboard layout
    """
    # Aggregate data
    daily_sales = df.groupby('Order_Date')['Sales'].sum().reset_index()
    category_sales = df.groupby('Category')['Sales'].sum().reset_index()
    region_sales = df.groupby('Region')['Sales'].sum().reset_index()
    
    # Create subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            'Daily Sales Trend',
            'Sales by Category',
            'Sales by Region',
            'Monthly Sales Heatmap'
        ),
        specs=[
            [{'type': 'scatter'}, {'type': 'bar'}],
            [{'type': 'bar'}, {'type': 'scatter'}]
        ],
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )
    
    # Daily sales trend
    fig.add_trace(
        go.Scatter(
            x=daily_sales['Order_Date'],
            y=daily_sales['Sales'],
            mode='lines',
            name='Daily Sales',
            line=dict(color='#1f77b4', width=1)
        ),
        row=1, col=1
    )
    
    # Sales by category
    fig.add_trace(
        go.Bar(
            x=category_sales['Category'],
            y=category_sales['Sales'],
            name='Category',
            marker_color='#2ca02c'
        ),
        row=1, col=2
    )
    
    # Sales by region
    fig.add_trace(
        go.Bar(
            x=region_sales['Region'],
            y=region_sales['Sales'],
            name='Region',
            marker_color='#ff7f0e'
        ),
        row=2, col=1
    )
    
    # Monthly trend
    df_monthly = df.copy()
    df_monthly['YearMonth'] = df_monthly['Order_Date'].dt.to_period('M').astype(str)
    monthly_sales = df_monthly.groupby('YearMonth')['Sales'].sum().reset_index()
    
    fig.add_trace(
        go.Scatter(
            x=monthly_sales['YearMonth'],
            y=monthly_sales['Sales'],
            mode='lines+markers',
            name='Monthly',
            line=dict(color='#d62728', width=2)
        ),
        row=2, col=2
    )
    
    fig.update_layout(
        height=800,
        showlegend=False,
        template='plotly_white',
        title_text='Sales Analytics Dashboard',
        title_x=0.5
    )
    
    # Update axes
    fig.update_xaxes(title_text='Date', row=1, col=1)
    fig.update_xaxes(title_text='Category', row=1, col=2)
    fig.update_xaxes(title_text='Region', row=2, col=1)
    fig.update_xaxes(title_text='Month', row=2, col=2, tickangle=45)
    
    fig.update_yaxes(title_text='Sales ($)', row=1, col=1)
    fig.update_yaxes(title_text='Sales ($)', row=1, col=2)
    fig.update_yaxes(title_text='Sales ($)', row=2, col=1)
    fig.update_yaxes(title_text='Sales ($)', row=2, col=2)
    
    return fig
