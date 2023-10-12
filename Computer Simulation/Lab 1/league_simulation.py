import league_functions as lf
import matplotlib.pyplot as plt

"""
Configuration file for a proper setting up a simulation
"""
# Configuration Parameters
number_of_teams = 16
e = 0.001
number_of_simulations = 31
teams = lf.create_teams(number_of_teams)
print(f"Dlugosc druzyn {len(teams)}")

# simulation
temp = []
for a in range(number_of_simulations):
    temp.append(lf.simulation(teams, e))

all = sum(temp)/len(temp)
if all < (3*number_of_teams - 3):
    print("Warunek zachowany")
else:
    print("Warunek niezachowany")
plt.hist(temp, bins=5, color='blue', alpha=0.7)

plt.show()