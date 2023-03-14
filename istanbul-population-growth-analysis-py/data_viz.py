import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Create a figure with two subplots: one for the line chart, one for the bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Create the line chart
years = [YEAR_1927, YEAR_1950, YEAR_2000, YEAR_2017]
populations = [POP_1927, POP_1950, POP_2000, POP_2017]
ax1.plot(years, populations, marker='o')
ax1.set_title(f"Population of {CITY_NAME}")
ax1.set_xlabel("Year")
ax1.set_ylabel("Population")
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x/1e6:g}M'))

# Create the bar chart
growth_rates = [annual_gr_1927_to_2017, growth_rate_1950_to_2000]
periods = ["1927-2017", "1950-2000"]
ax2.bar(periods, growth_rates)
ax2.set_title(f"Population Growth Rate of {CITY_NAME}")
ax2.set_xlabel("Time Period")
ax2.set_ylabel("Annual Growth Rate (%)")

# Display the charts
plt.show()
