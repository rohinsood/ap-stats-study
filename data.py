import statbotics
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

sb = statbotics.Statbotics()

random_team_numbers = [random.randint(4, 9000) for _ in range(50)]

parsed_data = {
  "lifespan": [],
  "mean_epa": []
}

for index, team_number in enumerate(random_team_numbers):
  
  try:
    data = sb.get_team(team_number, ["rookie_year", "active", "norm_epa"])
  except UserWarning:
    continue  
  
  if data["active"] == "False":
    continue
  
  lifespan = 2024 - int(data["rookie_year"])
    
  parsed_data["lifespan"].append(lifespan)
  parsed_data["mean_epa"].append(data["norm_epa"])

lifespan = np.array(parsed_data["lifespan"])
mean_epa = np.array(parsed_data["mean_epa"])

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

plt.title('Lifespan vs Mean EPA with LSRL')
plt.xlabel('Lifespan')
plt.ylabel('Mean EPA')
plt.legend()
plt.grid(True)
plt.show()

# Calculate residuals
residuals = mean_epa - predicted_mean_epa

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(lifespan, residuals, color='blue', alpha=0.5)
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residual Plot')
plt.xlabel('Lifespan')
plt.ylabel('Residuals')
plt.grid(True)
plt.show()
