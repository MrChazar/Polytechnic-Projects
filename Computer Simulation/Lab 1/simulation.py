import scipy.stats

import league_functions as lf
import matplotlib.pyplot as plt
import scipy.stats as stats
import work_statistics as ws
import  cup_functions as cf
import numpy as np

"""
Configuration file for a proper setting up a simulation
"""
# Configuration Parameters
number_of_teams = 4
e = 0.001
number_of_simulations = 31
confidence_level = 0.001


# League  simulation
"""
teams = lf.create_teams(number_of_teams)
temp = []
for a in range(number_of_simulations):
    temp.append(lf.simulation(teams, e))

avg = sum(temp)/len(temp)
"""
# Testing our hypothesis 3n -3
# Ho avg < 3n-3
# Ha avg !< 3n -3
"""

cond = 3*number_of_teams - 3
sd = ws.sd(temp)
t_stat = ws.t(avg,cond,sd)
p_value = 2 * stats.t.sf(abs(t_stat), len(temp)-1)
print(f"Statystyka t: {t_stat}")
print(f"P-wartość: {p_value}")

if p_value > confidence_level:
    print("Nie mamy wystarczających dowodów aby odrzucić H0")
else:
    print("Mamy wystarczający dowód aby odrzucić")

plt.hist(temp, bins=15, color='blue', alpha=0.7)
plt.show()

"""

# Cup Simulation
#"""
teams = lf.create_teams(number_of_teams)
winners = []

for a in range(number_of_simulations):
    winners.append(cf.simulation(teams))

print(teams)
column1 = [row[1] for row in teams]
column2 = [row[2] for row in teams]

print(scipy.stats.pearsonr(column1, column2))


plt.hist(winners, bins=15, color='blue', alpha=0.7)
plt.show()
#"""