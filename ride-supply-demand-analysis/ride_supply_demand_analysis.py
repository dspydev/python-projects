# -*- coding: utf-8 -*-
"""ride_supply_demand_analysis.ipynb

Automatically generated by Colaboratory.

# **1. Import Libraries and Set Default Plot Template**
"""

# Import necessary functions from libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

# Set default plot template to "plotly_white"
pio.templates.default = "plotly_white"

"""# **2. Load, Explore and Clean Dataset**"""

# Read data from a CSV file
data = pd.read_csv('rides.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Display information about the dataset
print("Information about the dataset:")
print(data.info())

# Check the number of missing values in each column of the 'data' dataframe.
print(data.isnull().sum())

# Drop rows with missing values
data.dropna(inplace=True)

"""# **3. Data Analysis**"""

# Calculate the elasticity of demand
elasticity = np.polyfit(data['Drivers Active Per Hour'], data['Riders Active Per Hour'], 1)[0]
print("Elasticity of demand with respect to the number of active drivers per hour: {:.2f}".format(elasticity))

# Calculate the supply ratio and add it as a new column
data['Supply Ratio'] = data['Rides Completed'] / data['Drivers Active Per Hour']

# Display the first few rows of the table to verify the result
print(data.head())

"""# **4. Data Visualizations**"""

# Create a scatter plot of demand vs. supply with an OLS regression line
fig_demand_supply = px.scatter(data, x="Drivers Active Per Hour", y="Riders Active Per Hour", trendline="ols", title="Demand and Supply Analysis")
fig_demand_supply.update_layout(
    xaxis_title="Number of Drivers Active per Hour (Supply)",
    yaxis_title="Number of Riders Active per Hour (Demand)",
)

# Create a new plot of supply ratio vs. driver activity
fig_supply_ratio = go.Figure()
fig_supply_ratio.add_trace(go.Scatter(x=data['Drivers Active Per Hour'], y=data['Supply Ratio'], mode='markers'))
fig_supply_ratio.update_layout(
    title='Supply Ratio vs. Driver Activity',
    xaxis_title='Driver Activity (Drivers Active per Hour)',
    yaxis_title='Supply Ratio (Rides Completed per Driver Active per Hour)'
)

# Display the plots
fig_demand_supply.show()
fig_supply_ratio.show()