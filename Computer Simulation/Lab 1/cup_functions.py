import random


def probability_a(rka, rkb):
    return rka / (rka + rkb)


def probability_b(rka, rkb):
    return 1 - probability_a(rka,rkb)

def match(team_a, team_b):
    random_numb = random.random()
    prob_a = probability_a(team_a[1], team_b[1])
    prob_b = probability_b(team_b[1], team_b[1])

    if random_numb < prob_a:
        return team_a
    else:
        return team_b

def simulation(teams):
    while len(teams) != 1:
        temp = []
        print(f"Before match: {teams}")
        for i in range(len(teams) // 2):
            temp.append(match(teams[i], teams[len(teams) - i - 1]))
        teams = temp
        print(f"After match: {teams}")
    return teams[0][1]

