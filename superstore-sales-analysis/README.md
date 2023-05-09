# Introduction

I recently came across a dataset on Kaggle (https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) containing information about a superstore's sales transactions. In this case study, I will examine the sales and profit data across different categories and subcategories, identify potential areas of improvement, and propose solutions to enhance the store's overall performance.

# Problems

To begin, I first explored the dataset, performing a preliminary analysis to identify any issues or inconsistencies. After importing the necessary libraries and loading the data into a pandas DataFrame, I noticed that the dataset contained information such as order dates, ship dates, categories, subcategories, sales, and profits. I then checked for any missing values, converted the date columns to datetime objects, and extracted additional information, such as the order month, year, and day of the week.

# Solutions

To better understand the dataset, I developed several visualization functions using the Plotly library. Here is a detailed explanation of each of the 8 visualizations

- **Total Sales by Category (Bar Chart):** This bar chart shows the total sales for each category, such as furniture, office supplies, and technology. The height of the bars represents the total sales, making it easy to compare the performance of each category.

![Total Sales by Category](https://github.com/dspydev/python-projects/assets/115745200/499ad901-ce17-438c-bbf8-5e79ae2b568f)

- **Total Profits by Category (Bar Chart):** Similar to the sales bar chart, this visualization shows the total profits for each category using bars. The height of the bars represents the total profits, allowing for a quick comparison of the profitability of each category.

![Total Profits by Category](https://github.com/dspydev/python-projects/assets/115745200/ef5ddb5b-e313-4453-b5e4-b80c2588c56b)

- **Sales Analysis by Category (Pie Chart):** This pie chart represents the proportion of total sales contributed by each category. Each category is represented as a slice of the pie, with the size of the slice corresponding to the proportion of total sales. This visualization highlights the most significant contributors to the store's sales.

![Sales Analysis by Category](https://github.com/dspydev/python-projects/assets/115745200/db765879-be3c-4bb8-9e14-afe57b919601)

- **Sales Analysis by Sub-Category (Bar Chart):** This bar chart displays the total sales for each subcategory within the main categories. The height of the bars represents the total sales, enabling a comparison of the performance of each subcategory.

![Sales Analysis by Sub-Category](https://github.com/dspydev/python-projects/assets/115745200/92e05517-728e-4ce7-aa2a-29b83455b1d8)

- **Profit Analysis by Sub-Category (Bar Chart):** Like the sales bar chart for subcategories, this visualization shows the total profits for each subcategory using bars. The height of the bars represents the total profits, allowing for an easy comparison of the profitability of each subcategory.

![Profit Analysis by Sub-Category](https://github.com/dspydev/python-projects/assets/115745200/0845078e-c5d5-4d47-8096-6f1c47effebd)

- **Profit Analysis by Category (Pie Chart):** Similar to the sales pie chart, this visualization shows the proportion of total profits contributed by each category. Each category is represented as a slice of the pie, with the size of the slice indicating the proportion of total profits. This chart helps identify the most profitable categories.

![Profit Analysis by Category](https://github.com/dspydev/python-projects/assets/115745200/6ea32d24-aa6f-4435-9b6b-e54f22247e8a)

- **Sales vs. Profit by Category (Scatter Plot):** This scatter plot displays the relationship between sales and profits for each category. Each data point represents a category, with its position on the horizontal axis indicating sales and its position on the vertical axis indicating profits. This visualization helps identify trends and patterns between sales and profits, revealing areas where sales are high but profits are low, as well as areas where both sales and profits are high.

![Sales vs  Profit by Category](https://github.com/dspydev/python-projects/assets/115745200/679e91b7-9729-48c3-a02b-18735a27c15f)

- **Monthly Sales Trend (Line Plot):** This line plot shows the sales trend over time on a monthly basis. The horizontal axis represents time, and the vertical axis represents total sales for each month. The line connecting the data points helps identify seasonal patterns and fluctuations in sales, providing valuable information on when the store experienced high and low sales periods.

![Monthly Sales Trend](https://github.com/dspydev/python-projects/assets/115745200/eca53301-f4a3-4faf-b1b1-5e6c6741a932)

By analyzing these visualizations, I identified specific areas where the store was performing well, as well as those where improvements could be made. For instance, certain categories and subcategories were generating high sales but low profits, indicating a potential issue with pricing or cost management. Additionally, the monthly sales trend revealed seasonal fluctuations, suggesting opportunities to capitalize on high-demand periods and develop strategies to increase sales during slower months.

# Conclusion

This case study demonstrates the power of data visualization in extracting valuable insights from sales data. By analyzing the performance of different categories, subcategories, and sales trends over time, I was able to identify areas of strong performance, potential weaknesses, and opportunities for growth. The insights gained from this analysis can be used to inform decision-making and help the store improve its overall performance.

# Next Steps

Based on the findings, I recommend the following actions:

- Reassess the pricing and cost structure of categories and subcategories with high sales but low profits to increase profitability.
- Implement targeted marketing campaigns to boost sales during slow months and leverage high-demand periods.
- Conduct regular performance reviews using these visualizations to monitor the store's progress and identify emerging trends or challenges.

I believe that by taking these steps, the store can improve its performance, increase profitability, and ultimately, achieve sustainable growth. The key to success will be in continuously analyzing and adapting to the changing market conditions and customer preferences.
