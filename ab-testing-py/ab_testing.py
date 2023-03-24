!pip install pandas plotly

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from typing import List

"""
This module imports necessary libraries for working with data analysis and visualization.

Libraries imported:
- Pandas: for working with tabular data
- Plotly graph objects: for creating interactive visualizations
- Plotly Express: for creating simple and fast visualizations
- Plotly IO: for configuring Plotly settings
- typing.List: for type hinting in function definitions
"""

# Set the default plotly template
pio.templates.default = "plotly_white"

# Read data from a CSV file and return as a pandas DataFrame
def read_data(file_name: str) -> pd.DataFrame:
    data = pd.read_csv(file_name, sep=";")
    # Rename columns for clarity
    data.columns = ["Campaign Name", "Date", "Amount Spent", 
                    "Number of Impressions", "Reach", "Website Clicks", 
                    "Searches Received", "Content Viewed", "Added to Cart",
                    "Purchases"]
    return data

# Fill in missing values in specified columns with the mean of the column
def fill_missing_values(data: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    for column in columns:
        data[column].fillna(value=data[column].mean(), inplace=True)
        # Convert column data to integer type
        data[column] = data[column].astype(int)
    return data

# Generate a pie chart comparing a column of two sets of data
def generate_pie_chart(title: str, control_data: pd.DataFrame, test_data: pd.DataFrame, column_name: str):
    label = [f"{column_name} from Control Campaign", f"{column_name} from Test Campaign"]
    counts = [sum(control_data[column_name]), sum(test_data[column_name])]
    colors = ['gold', 'lightgreen']
    fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
    # Add title to the pie chart
    fig.update_layout(title_text=f'Control Vs Test: {title}')
    fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                      textfont_size=30,
                      marker=dict(colors=colors, 
                                  line=dict(color='black', width=3)))
    fig.show()

# Read data from CSV files for the control and test campaigns
control_data = read_data("control_group.csv")
test_data = read_data("test_group.csv")

# Print the first 5 rows of each DataFrame
print(control_data.head())
print(test_data.head())

# Fill in missing values in both sets of data
fill_missing_values(control_data, ["Number of Impressions", "Reach", "Website Clicks", "Searches Received", "Content Viewed", "Added to Cart", "Purchases"])
fill_missing_values(test_data, ["Number of Impressions", "Reach", "Website Clicks", "Searches Received", "Content Viewed", "Added to Cart", "Purchases"])

# Merge the control and test data and sort by date
ab_data = control_data.merge(test_data, how="outer").sort_values(["Date"])

# Reset the index of the dataframe after merging and sorting
ab_data = ab_data.reset_index(drop=True)

# Print the first few rows of the merged data and the value count of "Campaign Name" column
print(ab_data.head())
print(ab_data["Campaign Name"].value_counts())

# Create a scatter plot to show the relationship between "Number of Impressions" and "Amount Spent" by campaign
figure = px.scatter(data_frame=ab_data, 
                    x="Number of Impressions",
                    y="Amount Spent", 
                    size="Amount Spent", 
                    color="Campaign Name", 
                    trendline="ols",
                    title="Amount Spent vs Number of Impressions by Campaign")
figure.show()

# Generate pie charts to compare the metrics for control and test groups
generate_pie_chart("Searches", control_data, test_data, "Searches Received")
generate_pie_chart("Website Clicks", control_data, test_data, "Website Clicks")
generate_pie_chart("Content Viewed", control_data, test_data, "Content Viewed")
generate_pie_chart("Added to Cart", control_data, test_data, "Added to Cart")
generate_pie_chart("Amount Spent", control_data, test_data, "Amount Spent")
generate_pie_chart("Purchases", control_data, test_data, "Purchases")

# Create a scatter plot to show the relationship between "Content Viewed" and "Website Clicks" by campaign
figure = px.scatter(data_frame=ab_data, 
                    x="Content Viewed",
                    y="Website Clicks", 
                    size="Website Clicks", 
                    color="Campaign Name", 
                    trendline="ols",
                    title="Content Views vs Website Clicks by Campaign")
figure.show()

# Create a scatter plot to show the relationship between "Added to Cart" and "Content Viewed" by campaign
figure = px.scatter(data_frame=ab_data, 
                    x="Added to Cart",
                    y="Content Viewed", 
                    size="Added to Cart", 
                    color="Campaign Name", 
                    trendline="ols",
                    title="Items Added to Cart vs Content Views by Campaign")
figure.show()

# Create a scatter plot to show the relationship between "Purchases" and "Added to Cart" by campaign
figure = px.scatter(data_frame=ab_data, 
                    x="Purchases",
                    y="Added to Cart", 
                    size="Purchases", 
                    color="Campaign Name", 
                    trendline="ols",
                    title="Purchases vs Items Added to Cart by Campaign")
figure.show()
