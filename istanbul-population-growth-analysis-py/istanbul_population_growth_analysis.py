# Define constants
CITY_NAME = "Istanbul, Turkey"
POP_1927 = 691_000
POP_1950 = 983_000
POP_2000 = 8_831_800
POP_2017 = 15_029_231
YEAR_1927 = 1927
YEAR_1950 = 1950
YEAR_2000 = 2000
YEAR_2017 = 2017

# Calculate the change in population between 1927 and 2017
pop_change = POP_2017 - POP_1927

# Calculate the annual growth rate between 1927 and 2017
percentage_gr = ((POP_2017 - POP_1927) / POP_1927) * 100
time_elapsed = YEAR_2017 - YEAR_1927
annual_gr_1927_to_2017 = percentage_gr / time_elapsed

# Define a function to calculate the annual growth rate between two years
def population_growth(year_one, year_two, population_one, population_two):
    growth_rate = (((population_two - population_one) / population_one) * 100) / (year_two - year_one)
    return growth_rate

# Calculate the annual growth rates between different periods
growth_rate_1927_to_2017 = population_growth(YEAR_1927, YEAR_2017, POP_1927, POP_2017)
growth_rate_1950_to_2000 = population_growth(YEAR_1950, YEAR_2000, POP_1950, POP_2000)

# Create a report summarizing the population growth of Istanbul
report = f"Istanbul, Turkey Population Growth Report\n\n"\
         f"1. Population Growth Overview\n"\
         f"• The population of {CITY_NAME} grew from {POP_1927:,} in {YEAR_1927} to {POP_2017:,} in {YEAR_2017}, a change of {pop_change:,}.\n"\
         f"• The annual growth rate between {YEAR_1927} and {YEAR_2017} was {annual_gr_1927_to_2017:.2f}%.\n"\
         f"• Between {YEAR_1950} and {YEAR_2000}, the annual growth rate was {growth_rate_1950_to_2000:.2f}%.\n\n"\
         f"2. Additional Information\n"\
         f"• {CITY_NAME} is the largest city in Turkey and the fifth largest city in the world.\n"\
         f"• It has experienced enormous growth over the past 50 years and is one of the world's 10 fastest growing metropolitan areas."

# Print the report to the console
print(report)
