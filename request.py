import csv
import datetime
import random
from types import NoneType
import statbotics

sb = statbotics.Statbotics()

file_name = "parsed_data.csv"

num_teams = 60

# List to store selected teams
selected_teams = []
selected_team_numbers = set()

# Counters for each age category
count_less_than_10 = 0
count_between_10_and_20 = 0
count_exceed_20 = 0


current_year = datetime.datetime.now().year
# Keep looping until we have gathered 100 active teams
while len(selected_teams) < 100:
    # Generate a random team number
    team_number = random.randint(1, 10000)
    
    # Check if the team number has already been selected
    if team_number in selected_team_numbers:
        continue
    
    try:
        # Get team data
        data = sb.get_team(team_number, ["rookie_year", "active", "norm_epa"])
    except UserWarning:
        continue  
    
    print(data)
    
    if not data["active"]:
        continue
    
    if data["rookie_year"] == None:
        continue
    
    age = current_year - data["rookie_year"]
    
    if age < 10 and count_less_than_10 < 50:
        selected_teams.append(data)
        selected_team_numbers.add(team_number)
        count_less_than_10 += 1
    elif 10 <= age < 20 and count_between_10_and_20 < 50:
        selected_teams.append(data)
        selected_team_numbers.add(team_number)
        count_between_10_and_20 += 1

# Write the data to the CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["age", "norm_epa"])  # Write header
    for team in selected_teams:
        age = current_year - team["rookie_year"]
        writer.writerow([age, team["norm_epa"]])

print(f"Data saved to '{file_name}'")

print("Selected Teams:", selected_teams)

