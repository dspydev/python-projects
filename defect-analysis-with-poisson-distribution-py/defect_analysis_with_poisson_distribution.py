import numpy as np
from scipy import stats

# Set the rate parameter lambda for the Poisson distribution
lam = 7

# Calculate the probability of observing exactly 7 defects on a given day
prob_7 = round(stats.poisson.pmf(7, lam), 3)
print("Probabilities:")
print("- Probability of observing exactly 7 defects on a given day:", prob_7)

# Calculate the probability of having 4 or fewer defects on a given day
prob_4_or_less = round(stats.poisson.cdf(4, lam), 3)
print("- Probability of having 4 or fewer defects on a given day:", prob_4_or_less)

# Calculate the probability of having more than 9 defects on any given day
prob_9_or_more = round(1 - stats.poisson.cdf(9, lam), 4)
print("- Probability of having more than 9 defects on any given day:", prob_9_or_more)

# Generate a dataset of 365 days of defect counts
year_defects = stats.poisson.rvs(lam, size=365)

# Print the first 20 values in the dataset
print("\nDataset:")
print("- First 20 values in the dataset:\n", year_defects[:20])

# Calculate summary statistics for the dataset
total_expected_defects = round(lam * 365, 0)
total_actual_defects = np.sum(year_defects)
avg_defects_per_day = round(np.mean(year_defects), 4)
max_defects_in_a_day = np.max(year_defects)
prob_max_or_more = round(1 - stats.poisson.cdf(max_defects_in_a_day - 1, lam), 3)
percentile_90 = stats.poisson.ppf(0.9, lam)
proportion_above_90 = round(sum(year_defects >= percentile_90) / len(year_defects), 3)

# Print the summary statistics
print("\nSummary Statistics:")
print("- Total number of expected defects over 365 days:", total_expected_defects)
print("- Total number of actual defects observed over 365 days:", total_actual_defects)
print("- Average number of defects per day:", avg_defects_per_day)
print("- Maximum number of defects observed in a single day:", max_defects_in_a_day)
print("- Probability of observing", max_defects_in_a_day, "or more defects in a single day:", prob_max_or_more)
print("- Number of defects that would put us in the 90th percentile for a given day:", percentile_90)
print("- Proportion of days with the number of defects greater than or equal to the 90th percentile value:", proportion_above_90)
