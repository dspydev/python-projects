# Introduction

The purpose of this case study is to analyze the defect patterns in a manufacturing process, using the Poisson distribution to model the number of defects occurring in a fixed interval of time. 

The Poisson distribution is a mathematical model used to predict the number of events happening in a fixed time or space. It's helpful when events are rare, separate, and happen at a constant rate. It's named after the French mathematician Siméon Denis Poisson.

Based on the available information and assumptions, I will examine the probabilities of different defect scenarios, generate a dataset of defect counts, and calculate summary statistics for the dataset.

# Problems

The major problems I identified are:

- Understanding the probability of observing specific numbers of defects, such as exactly 7 defects or 4 or fewer defects on a given day.
- Estimating the likelihood of observing more than 9 defects on any given day.
- Assessing the distribution of defects across days and determining the characteristics of days with high defect counts.

Below is a bar chart of defect scenarios probabilities:

<p align="center">
  <img src="https://user-images.githubusercontent.com/115745200/225316010-28ae62db-443a-491c-814c-78fb11496e39.png" alt="image">
</p>

The bar chart has three bars, each representing a specific scenario:

- Exactly 7 defects: The first bar is colored royal blue and represents the probability of finding exactly 7 defects in the process. This probability is 0.149 or 14.9%.
- 4 or fewer defects: The second bar is colored forest green and represents the probability of finding 4 or fewer defects in the process. This probability is 0.173 or 17.3%.
- More than 9 defects: The third bar is colored firebrick red and represents the probability of finding more than 9 defects in the process. This probability is 0.1695 or 16.95%.

Each bar's height corresponds to the probability of the respective scenario occurring. The chart also has labels for each bar showing the exact probability value, along with a title, an x-axis label indicating "Defect Scenarios," and a y-axis label indicating "Probability."

# Solutions

To address these problems, I performed the following analyses:

- Calculated the probabilities of different defect scenarios using the Poisson distribution, considering the rate parameter lambda (7 defects per day on average).
- Generated a dataset of 365 days of defect counts based on the Poisson distribution.
- Calculated summary statistics for the dataset, including the total number of expected and actual defects, average defects per day, maximum defects in a single day, the 90th percentile value, and the proportion of days with defects greater than or equal to the 90th percentile value.

Below is a pie chart of the proportion of days with defects greater than or equal to the 90th percentile:

<p align="center">
  <img src="https://user-images.githubusercontent.com/115745200/225316071-3767065b-9a49-4cea-b974-77296b5ad6f4.png" alt="image">
</p>

The pie chart has two sections:

- Days with defects >= 90th percentile: This section is colored seagreen and represents the proportion of days where the number of defects is equal to or greater than the 90th percentile. The 90th percentile value indicates that 90% of the days have that number of defects or fewer, and 10% of the days have more defects. This helps us understand how often we see a high number of defects.
- Other days: This section is colored light gray and represents the remaining days where the number of defects is below the 90th percentile.

The chart also displays the percentage of each section, which is automatically calculated using the autopct parameter. It starts drawing the sections from a 90-degree angle and slightly separates the seagreen section from the light gray section by using the explode parameter.

# Conclusion

The analysis revealed that the Poisson distribution is a useful tool for modeling defect patterns in the manufacturing process. By examining the probabilities of different defect scenarios, generating a dataset, and calculating summary statistics, I was able to gain insights into the characteristics of high-defect days and the distribution of defects across days.

# Next steps

Based on the findings, I recommend the following actions:

- Monitor the manufacturing process closely on days with defect counts greater than or equal to the 90th percentile value, as these days represent the top 10% of high-defect days.
- Investigate the underlying causes of high-defect days and identify any common factors or patterns.
- Implement targeted improvements to address the root causes of high-defect days, such as equipment maintenance, employee training, or changes to the production process.
- Continuously track and analyze defect patterns, updating the Poisson model as needed to reflect any changes in the manufacturing process or environment. This will help to assess the effectiveness of implemented improvements and inform future decision-making.
