# -*- coding: utf-8 -*-
"""user_behaviour_insights_with_kmeans_clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w5Bdyyib4aeDgquPdVZs3WpIKv2zgOph

# **1. Importing libraries**
"""

import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

pio.templates.default = "plotly_white"

"""# **2. Loading data and descriptive statistics**"""

# Loading data
data = pd.read_csv("userbehaviour.csv")

# Displaying the first few rows
print("First few rows of the data:")
print(data.head())

# Descriptive statistics for key variables
print(f"\nDescriptive statistics for 'Average Screen Time':")
print(f" - Mean: {data['Average Screen Time'].mean()}")
print(f" - Maximum: {data['Average Screen Time'].max()}")
print(f" - Minimum: {data['Average Screen Time'].min()}")

print(f"\nDescriptive statistics for 'Average Spent on App (INR)':")
print(f" - Mean: {data['Average Spent on App (INR)'].mean()}")
print(f" - Maximum: {data['Average Spent on App (INR)'].max()}")
print(f" - Minimum: {data['Average Spent on App (INR)'].min()}")

"""# **3. Creating scatter plots**"""

# Creating a scatter plot showing the relationship between screen time and spending capacity
figure = px.scatter(data_frame = data, 
                    x="Average Screen Time",
                    y="Average Spent on App (INR)", 
                    size="Average Spent on App (INR)", 
                    color= "Status",
                    title = "Relationship Between Spending Capacity and Screentime",
                    trendline="ols")
figure.show()

# Creating a scatter plot showing the relationship between screen time and user ratings
figure = px.scatter(data_frame = data, 
                    x="Average Screen Time",
                    y="Ratings", 
                    size="Ratings", 
                    color= "Status", 
                    title = "Relationship Between Ratings and Screentime",
                    trendline="ols")
figure.show()

"""# **4. Data segmentation**"""

# Selecting variables for segmentation
clustering_data = data[["Average Screen Time", "Left Review", 
                        "Ratings", "Last Visited Minutes", 
                        "Average Spent on App (INR)", 
                        "New Password Request"]]

# Normalizing data
scaler = MinMaxScaler()
clustering_data_scaled = scaler.fit_transform(clustering_data)

# Running K-means clustering with three clusters, setting n_init=10 explicitly
kmeans = KMeans(n_clusters=3, n_init=10)
clusters = kmeans.fit_predict(clustering_data_scaled)
data["Segments"] = clusters

# Displaying the first 10 rows with segment assignments
print(data.head(10))

# Counting the number of users in each segment
print(data["Segments"].value_counts())

# Mapping segment numbers to descriptive names
data["Segments"] = data["Segments"].map({0: "Retained", 1: 
    "Churn", 2: "Needs Attention"})

"""# **5. Creating scatter plot with segments**"""

# Creating a scatter plot showing the relationship between last visited minutes and average spending, with segments shown in different colors
PLOT = go.Figure()
for i in list(data["Segments"].unique()):
    PLOT.add_trace(go.Scatter(x = data[data["Segments"]== i]['Last Visited Minutes'],
                                y = data[data["Segments"] == i]['Average Spent on App (INR)'],
                                mode = 'markers',marker_size = 6, marker_line_width = 1,
                                name = str(i)))
PLOT.update_traces(hovertemplate='Last Visited Minutes: %{x} <br>Average Spent on App (INR): %{y}')

# Updating the layout of the scatter plot
PLOT.update_layout(width = 800, height = 800, autosize = True, showlegend = True,
                   yaxis_title = 'Average Spent on App (INR)',
                   xaxis_title = 'Last Visited Minutes',
                   scene = dict(xaxis=dict(title = 'Last Visited Minutes', titlefont_color = 'black'),
                                yaxis=dict(title = 'Average Spent on App (INR)', titlefont_color = 'black')))