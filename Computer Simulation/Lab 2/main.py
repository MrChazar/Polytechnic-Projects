import math
import functions as f
import matplotlib.pyplot as plt
import work_statistics as ws
import scipy.stats as stats

"""
Configuration file for a proper setting up a simulation
"""

# creating shield
shield = f.generate_shield()
# setting number of simulations
number_of_simulations = 31
# confidence level
confidence_level = 0.01


# shoot A
avg_a = []
for a in range(number_of_simulations):
    avg_a.append(f.simulation(shield,'A'))


# shoot B
avg_b = []
for b in range(number_of_simulations):
    avg_b.append(f.simulation(shield, type_of_shoot='B'))


# Creating Plots to compare both shootings methods
fig, axs = plt.subplots(1, 2)

axs[0].hist(avg_a, bins=15, color='blue', alpha=0.7)
axs[0].set_title("Shooting Range A")

axs[1].hist(avg_b, bins=15, color='red', alpha=0.7)
axs[1].set_title("Shooting Range B")

plt.tight_layout()
plt.show()

# Statistical Test Z
# Testing our hypothesis avg_a=avg_b
# Ho avg_a=avg_b
# Ha avg!=avg_b

t_stat, p_value = stats.kstest(avg_a, avg_b)
print(f"Statystyka t: {t_stat}")
print(f"P-wartość: {p_value}")

if p_value > confidence_level:
    print("Nie mamy wystarczających dowodów aby odrzucić H0")
else:
    print("Mamy wystarczający dowód aby odrzucić H0 przyjmujemy hipotezę alternatywną Ha czyli avg_a != avg_b")


