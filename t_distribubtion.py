import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress, t

# Load data
data = np.genfromtxt('./second_sample/parsed_data.csv', delimiter=',', skip_header=1)

# Extract columns
lifespan = data[:, 0]
norm_epa = data[:, 1]

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(lifespan, norm_epa)

# Calculate predicted norm_epa
predicted_norm_epa = slope * lifespan + intercept

# Print summary statistics
print("Summary Statistics:")
print("Slope (m):", slope)
print("Intercept (b):", intercept)
print("Correlation Coefficient (r):", r_value)
print("Coefficient of Determination (r^2):", r_value ** 2)
print("Standard Error of the Estimate (SEE):", std_err)
print("Standard Deviation of Lifespan:", np.std(lifespan))
print("Standard Deviation of Norm EPA:", np.std(norm_epa))
print("P-Value:", p_value)

# Number of observations
n = len(lifespan)

# Mean of lifespan
x_bar = np.mean(lifespan)

# Calculate the standard error of the slope
numerator = np.sum((norm_epa - predicted_norm_epa) ** 2)
denominator = np.sum((lifespan - x_bar) ** 2)
standard_error_slope = np.sqrt((1 / (n - 2)) * (numerator / denominator))

# Print the calculated standard error of the slope
print("Standard Error of the Slope (s(b1)):", standard_error_slope)

df = n - 2  # degrees of freedom
t_stat = t.ppf(1 - p_value / 2, df)

# Define the t-distribution range
t_values = np.linspace(-4, 4, 1000)
t_dist = t.pdf(t_values, df)

# Plot the t-distribution
plt.figure(figsize=(10, 6))
plt.plot(t_values, t_dist, color='blue', label=f't-distribution (df={df})')
plt.fill_between(t_values, 0, t_dist, where=t_values >= t_stat, color='red', alpha=0.5, label=f'Critical region (p={p_value})')
plt.axvline(t_stat, color='red', linestyle='dashed', label=f'Critical t-value: {t_stat:.2f}')
plt.title(f'T-distribution with {df} degrees of freedom')
plt.xlabel('t-value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.savefig('./second_sample/t_distribution_plot.png')
plt.show()