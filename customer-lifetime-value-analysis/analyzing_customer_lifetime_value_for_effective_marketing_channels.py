# -*- coding: utf-8 -*-
"""analyzing_customer_lifetime_value_for_effective_marketing_channels.ipynb

Automatically generated by Colaboratory.

# **1. Import Required Libraries and Set Default Template for Plots**
"""

# Import required libraries
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio

# Set default template for plots
pio.templates.default = "plotly_white"

"""# **2. Data Exploration**"""

# Load data from CSV file
data = pd.read_csv("customer_acquisition_data.csv")

# Print first 5 rows of data
print(data.head())

# Print the shape of the data (number of rows, number of columns)
print("Data shape:", data.shape)

# Print a summary of the data including the count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum values for each column
print("\nData summary:")
print(data.describe())

# Print the data types of each column
print("\nData types:")
print(data.dtypes)

# Print the unique values for the categorical variable (channel)
print("\nUnique values for categorical variable (channel):")
print(data['channel'].unique())

# Check for missing values
print("Number of missing values per column:\n", data.isnull().sum())

"""# **3. Data Visualization**"""

# Create histogram of acquisition cost distribution
def create_cost_hist(data):
    fig = px.histogram(data, 
                        x="cost", 
                        nbins=20, 
                        title='Distribution of Acquisition Cost')
    return fig

# Create histogram of revenue distribution
def create_revenue_hist(data):
    fig = px.histogram(data, 
                           x="revenue", 
                           nbins=20, 
                           title='Distribution of Revenue')
    return fig

# Calculate and plot acquisition cost by channel
def create_cost_by_channel(data):
    cost_by_channel = data.groupby('channel')['cost'].mean().reset_index()
    fig = px.bar(cost_by_channel, 
                          x='channel', 
                          y='cost', 
                          title='Customer Acquisition Cost by Channel')
    fig.update_xaxes(title='Channel')
    fig.update_yaxes(title='Acquisition Cost')
    fig.update_layout(legend_title='Channel')
    return fig

# Calculate and plot conversion rate by channel
def create_conversion_by_channel(data):
    conversion_by_channel = data.groupby('channel')['conversion_rate'].mean().reset_index()
    fig = px.bar(conversion_by_channel, 
                                x='channel', 
                                y='conversion_rate', 
                                title='Conversion Rate by Channel')
    fig.update_xaxes(title='Channel')
    fig.update_yaxes(title='Conversion Rate')
    return fig

# Calculate and plot total revenue by channel
def create_revenue_by_channel(data):
    revenue_by_channel = data.groupby('channel')['revenue'].sum().reset_index()
    fig = px.pie(revenue_by_channel, 
                             values='revenue', 
                             names='channel', 
                             title='Total Revenue by Channel', 
                             hole=0.6, 
                             color_discrete_sequence=px.colors.qualitative.Pastel)
    return fig

# Calculate and plot return on investment (ROI) by channel
def create_roi_by_channel(data):
    data['roi'] = data['revenue'] / data['cost']
    roi_by_channel = data.groupby('channel')['roi'].mean().reset_index()
    fig = px.bar(roi_by_channel, 
                          x='channel', 
                          y='roi', 
                          title='Return on Investment (ROI) by Channel')
    fig.update_xaxes(title='Channel')
    fig.update_yaxes(title='ROI')
    return fig

# Calculate and plot customer lifetime value (CLTV) by channel
def create_cltv_by_channel(data):
    data['cltv'] = (data['revenue'] - data['cost']) * data['conversion_rate'] / data['cost']
    cltv_by_channel = data.groupby('channel')['cltv'].mean().reset_index()
    fig = px.bar(cltv_by_channel, 
                           x='channel', 
                           y='cltv', 
                           color='channel',
                           title='Customer Lifetime Value by Channel')
    fig.update_xaxes(title='Channel')
    fig.update_yaxes(title='CLTV')
    return fig

# Create box plot of CLTV distribution by channel
def create_cltv_box_by_channel(data):
    subset = data.loc[data['channel'].isin(['social media', 'referral'])]
    fig = px.box(subset, 
                      x='channel', 
                      y='cltv', 
                      title='CLTV Distribution by Channel')
    fig.update_xaxes(title='Channel')
    fig.update_yaxes(title='CLTV')
    fig.update_layout(legend_title='Channel')
    return fig

# Show plots
fig_cost = create_cost_hist(data)
fig_revenue = create_revenue_hist(data)
fig_cost_channel = create_cost_by_channel(data)
fig_conversion_channel = create_conversion_by_channel(data)
fig_revenue_channel = create_revenue_by_channel(data)
fig_roi_channel = create_roi_by_channel(data)
fig_cltv_channel = create_cltv_by_channel(data)
fig_cltv_box = create_cltv_box_by_channel(data)

fig_cost.show()
fig_revenue.show()
fig_cost_channel.show()
fig_conversion_channel.show()
fig_revenue_channel.show()
fig_roi_channel.show()
fig_cltv_channel.show()
fig_cltv_box.show()