# Introduction

My goal was to create a model that could predict sales based on advertising spending across different channels, such as TV, Newspaper, and Radio. I chose to use the linear regression algorithm for this task, although there are other algorithms that might be suitable as well. The dataset I used can be found at this link: https://raw.githubusercontent.com/amankharwal/Website-data/master/advertising.csv

# Problems

The main problem I faced was determining which advertising channels had the most significant impact on sales. To analyze the problem, I first explored the data by visualizing the relationship between sales and each advertising channel using scatter plots. I also calculated the correlations between each variable and sales to understand the strength of their relationships. This analysis helped me identify the most relevant advertising channels and provided insights into their potential effectiveness.

# Solutions

I decided to use the linear regression algorithm as my primary solution, as it is a simple yet powerful method to model the relationship between a dependent variable (sales) and one or more independent variables (advertising channels). However, there are alternative algorithms that could also be considered, such as:

- **Decision Trees or Random Forests:** These algorithms can capture complex relationships between features and the target variable. They are particularly useful when dealing with nonlinear relationships.
- **Support Vector Machines (SVM):** SVMs are effective in high-dimensional spaces and can be used for regression tasks with the right kernel function.
- **Neural Networks:** Deep learning techniques can capture complex patterns in data and can be applied to regression tasks as well.

While each algorithm has its pros and cons, the choice depends on the specific use case and the nature of the data. In this case, I found linear regression to be a suitable choice due to its simplicity and interpretability.

During my analysis, I created scatter plots for each advertising channel against sales, with a trendline added to visualize the relationship. These visualizations revealed the following:

- **Sales vs. TV:** A strong positive relationship was observed, indicating that as TV advertising spending increased, so did sales. The trendline showed an upward slope, highlighting the direct relationship between the two variables.

![sales_vs_tv](https://user-images.githubusercontent.com/115745200/234044258-f68618ce-ac63-4220-bd0f-282ba9dfdd86.png)

- **Sales vs. Newspaper:** A weaker positive relationship was observed compared to TV advertising. The data points were more dispersed, but the trendline still showed a slight upward slope.

![sales_vs_newspaper](https://user-images.githubusercontent.com/115745200/234045487-25ce93c2-1e44-45e2-ab91-b3ccfad44548.png)

- **Sales vs. Radio:** A moderate positive relationship was observed, with the data points less dispersed than in the Newspaper vs. Sales plot. The trendline also had an upward slope.

![sales_vs_radio](https://user-images.githubusercontent.com/115745200/234045757-f306fc74-fe41-4474-9c08-581be02ced96.png)

These visualizations helped me understand which advertising channels had the most significant impact on sales and provided valuable insights for further analysis.

# Conclusion

After conducting the analysis and comparing different algorithms, I concluded that linear regression was the most suitable choice for this case study. I successfully built a model that predicted sales based on advertising spending across different channels, with the strongest relationship observed between TV advertising and sales. The visualizations I created provided valuable insights into the effectiveness of each advertising channel and the strength of their relationships with sales.

# Next Steps

I recommend that the business invests more in the channels with the strongest relationships to sales, primarily TV advertising, and to a lesser extent, radio advertising. Based on the linear regression model, these investments are likely to yield higher sales compared to investing in newspaper advertising. To implement this strategy, the marketing team should allocate budgets accordingly and monitor the results over time to evaluate the effectiveness of the new advertising mix.
