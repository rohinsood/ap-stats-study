import statbotics
import random

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
  
  
parsed_data