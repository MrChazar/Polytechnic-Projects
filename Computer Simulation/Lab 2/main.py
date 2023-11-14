import functions as f
import matplotlib.pyplot as plt
import scipy.stats as stats

"""
Configuration file for a proper setting up a simulation
"""

# setting number of simulations
number_of_simulations = 31
# confidence level
confidence_level = 0.05


# shoot A
avg_a = []
x_a = []
y_a = []
for a in range(number_of_simulations):
    score, x_temp, y_temp = f.simulation(type_of_shoot='A')
    avg_a.append(score)
    x_a += x_temp
    y_a += y_temp
f.generate_shield((0,0), x=x_a, y=y_a, type="single_a")

# shoot B
avg_b = []
x_b = []
y_b = []
for b in range(number_of_simulations):
    score, x_temp, y_temp = f.simulation(type_of_shoot='B')
    avg_b.append(score)
    x_b += x_temp
    y_b += y_temp
f.generate_shield((0,0), x=x_b, y=y_b, type="single_b")

# Plot with combined Shot A and B
f.generate_shield((0,0), x=x_a, y=y_a, x_1=x_b, y_1=y_b, type="multiple")

# Creating Plots to compare both shootings methods
f.generate_histogram(avg_a, avg_b)

# Statistical Test
# Testing our hypothesis avg_a=avg_b
# Ho avg_a=avg_b
# Ha avg!=avg_b

print(f"Średnia Strzelnicy a { sum(avg_a)/ len(avg_a) }")
print(f"Średnia Strzelnicy b { sum(avg_b)/ len(avg_b) }")


t_stat, p_value = stats.ttest_ind(avg_a, avg_b)
print(f"Statystyka t: {t_stat}")
print(f"P-wartość: {p_value}")

if p_value > confidence_level:
    print("Nie mamy wystarczających dowodów aby odrzucić H0")
else:
    print("Mamy wystarczający dowód aby odrzucić H0 przyjmujemy hipotezę alternatywną Ha czyli avg_a != avg_b")


