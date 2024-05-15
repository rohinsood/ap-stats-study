import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = np.genfromtxt('./second_sample/parsed_data.csv', delimiter=',', skip_header=1)

lifespan = data[:, 0]
norm_epa = data[:, 1]

slope, intercept, r_value, p_value, std_err = linregress(lifespan, norm_epa)

predicted_norm_epa = slope * lifespan + intercept

# Calculate residuals
residuals = norm_epa - predicted_norm_epa

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(lifespan, residuals, color='blue', alpha=0.5)
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residual Plot')
plt.xlabel('Lifespan')
plt.ylabel('Residuals')
plt.grid(True)
plt.savefig('./second_sample/residuals.png')
plt.show()
