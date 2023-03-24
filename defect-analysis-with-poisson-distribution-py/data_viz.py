'''Bar chart of defect scenarios probabilities'''

!pip install matplotlib

import matplotlib.pyplot as plt

# Probabilities
prob_7 = 0.149
prob_4_or_less = 0.173
prob_9_or_more = 0.1695

# Create bar chart for probabilities
plt.figure(figsize=(10, 6))
bars = plt.bar(['Exactly 7 defects', '4 or fewer defects', 'More than 9 defects'],
               [prob_7, prob_4_or_less, prob_9_or_more],
               color=['royalblue', 'forestgreen', 'firebrick'])

# Add labels and title to the chart
plt.xlabel('Defect Scenarios')
plt.ylabel('Probability')
plt.title('Probability of Different Defect Scenarios')

# Annotate probabilities on the bars
bar_labels = ['Exactly 7 defects', '4 or fewer defects', 'More than 9 defects']
bar_probs = [prob_7, prob_4_or_less, prob_9_or_more]

for i, (label, prob) in enumerate(zip(bar_labels, bar_probs)):
    plt.text(i, prob + 0.005, f'{prob:.3f}', ha='center', va='bottom', fontsize=12)

# Adjust y-axis limits to provide more space above the bars
plt.ylim(0, max(bar_probs) + 0.03)

# Add legend to the chart
legend = plt.legend(bars, bar_labels, title='Defect Scenarios', fontsize=12, title_fontsize=14, loc='upper left', bbox_to_anchor=(1, 1), borderpad=1, labelspacing=1)

# Remove the border from the legend box
legend.get_frame().set_edgecolor('none')

# Display the chart
plt.show()

'''Pie chart of the proportion of days with defects greater than or equal to the 90th percentile'''

import matplotlib.pyplot as plt

# Pie chart data
pie_labels = ['Days with defects >= 90th percentile', 'Other days']
pie_values = [proportion_above_90, 1 - proportion_above_90]
pie_colors = ['seagreen', 'lightgray']
explode = (0.1, 0)

fig, ax = plt.subplots(figsize=(10, 6))

# Pie chart
ax.pie(pie_values, labels=None, colors=pie_colors, autopct='%1.1f%%', startangle=90, explode=explode, textprops={'fontsize': 12})
ax.axis('equal')
ax.set_title('Proportion of Days with Defects\nGreater than or Equal to the 90th Percentile')

# Add legend with explanation to the right side
explanation = f"""The 90th percentile value is the number of defects at which 
90% of the days have that amount or fewer defects, and 
10% of the days have more defects. It helps us understand 
how often we see high or low numbers of defects."""

ax.legend(pie_labels, title='Defect Days', fontsize=12, title_fontsize=14, loc='upper left', bbox_to_anchor=(0.9, 1), borderpad=1, labelspacing=1)
ax.text(1.2, -0.4, explanation, fontsize=12, bbox=dict(facecolor='none', edgecolor='none', pad=5))

plt.show()
