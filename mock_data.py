import numpy as np
import matplotlib.pyplot as plt

# Generate data for the linear regression
np.random.seed(0)  # for reproducibility
x = np.linspace(0, 10, 20)  # 20 data points evenly spaced between 0 and 10
slope = 2  # slope of the regression line
intercept = 1  # y-intercept of the regression line
y_true = slope * x + intercept  # true y values without noise

# Introduce random noise to simulate deviations
mean_noise = 0  # mean of the noise
std_dev_noise = 1  # standard deviation of the noise
noise = np.random.normal(mean_noise, std_dev_noise, size=len(x))

# Generate y values with added noise
y_with_noise = y_true + noise

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(x, y_with_noise, label='Data Points')
plt.plot(x, y_true, color='red', label='True Regression Line')
plt.xlabel('Lifespan of a Robotics Team')
plt.ylabel('EPA')
plt.title('EPA vs. Lifespan of a Robotics Team')
plt.legend()
plt.grid(True)
plt.show()
