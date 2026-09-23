import numpy as np


# Suppose you have a year's worth of daily temperature data in Celsius
temperature_data = np.array([22.3, 23.1, 24.5, 25.8, 23.6, 26.7, 27.9, 29.2, 30.5, 24.7, 23.4, 22.1, 25.3, 26.4, 28.7, 29.8, 31.2, 32.4, 30.7, 29.5, 27.8, 26.6, 23.9, 22.5, 24.1, 25.7, 27.3, 29.6, 31.0, 33.1, 31.9])


# Calculate the mean, median, and standard deviation
mean = np.mean(temperature_data)
median = np.median(temperature_data)
stDev = np.std(temperature_data)

# Print mean, median, standard deviation in an organized manner
print(f'Mean: {}')

# Find days with temperatures above a certain threshold (e.g., 30°C) save in variable 'hot_days'


# Count the number of hot days


# Print number of hot days in an organized manner


# Convert all temperatures to Fahrenheit = (temp * 9/5) +32
temperature_fahrenheit = (temperature_data * 9/5) + 32
print(temperature_fahrenheit) 

## BONUS ##
# Calculate the total cooling degree days for the year
# Cooling degree days represent the cumulative amount of cooling required to maintain a comfortable indoor temperature.
# Amount of degrees to cool. to bring back to base temperature
# In this example, we'll consider a base temperature of 20°C.
base_temperature = 20
cooling_degrees = np.sum(np.maximum)
# Print cooling degree days an organized manner