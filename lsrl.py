import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = np.genfromtxt('./second_sample/parsed_data.csv', delimiter=',', skip_header=1)

lifespan = data[:, 0]
mean_epa = data[:, 1]

slope, intercept, r_value, p_value, std_err = linregress(lifespan, mean_epa)

predicted_mean_epa = slope * lifespan + intercept

plt.figure(figsize=(10, 6))
plt.scatter(lifespan, mean_epa, color='blue', alpha=0.5, label='Data Points')
plt.plot(lifespan, predicted_mean_epa, color='red', label='LSRL')

print("Summary Statistics:")
print("Slope (m):", slope)
print("Intercept (b):", intercept)
print("Correlation Coefficient (r):", r_value)
print("Coefficient of Determination (r^2):", r_value ** 2)
print("Standard Error of the Estimate (SEE):", std_err)
print("Standard Deviation of Lifespan:", np.std(lifespan))
print("Standard Deviation of Mean EPA:", np.std(mean_epa))
print("P-Value:", p_value)

plt.title('Lifespan vs Mean EPA with LSRL')
plt.xlabel('Lifespan')
plt.ylabel('Mean EPA')
plt.legend()
plt.grid(True)
plt.savefig('./second_sample/lifespan_vs_mean_epa_plot.png')
plt.show()