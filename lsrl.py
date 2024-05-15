import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = np.genfromtxt('./second_sample/parsed_data.csv', delimiter=',', skip_header=1)

lifespan = data[:, 0]
norm_epa = data[:, 1]

slope, intercept, r_value, p_value, std_err = linregress(lifespan, norm_epa)

predicted_norm_epa = slope * lifespan + intercept

plt.figure(figsize=(10, 6))
plt.scatter(lifespan, norm_epa, color='blue', alpha=0.5, label='Data Points')
plt.plot(lifespan, predicted_norm_epa, color='red', label='LSRL')

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

plt.title('Lifespan vs Norm EPA with LSRL')
plt.xlabel('Lifespan')
plt.ylabel('Norm EPA')
plt.legend()
plt.grid(True)
plt.savefig('./second_sample/lifespan_vs_norm_epa_plot.png')
plt.show()