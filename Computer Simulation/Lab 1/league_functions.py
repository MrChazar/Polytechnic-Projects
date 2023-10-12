
import random


def create_teams(number):
    teams = []
    while len(teams) < number:
        team_sign = chr(random.randint(65, 91))
        if team_sign not in [row[0] for row in teams]:
            teams.append([team_sign, random.random(), 0])
    return teams

def probability_a(rka, rkb, e):
    return rka / (rka + rkb + (1 / 3) * ((rka + rkb) / (abs(rka - rkb) + e)))


def probability_b(rka, rkb, e):
    return rkb / (rka + rkb + (1 / 3) * ((rka + rkb) / (abs(rka - rkb) + e)))


def probability_ab(prob_a, prob_b):
    return 1-prob_b-prob_a


def match(teamA, teamB, e):

    random_numb = random.random()
    prob_a = probability_a(teamA[1], teamB[1], e)
    prob_b = probability_b(teamA[1], teamB[1], e)
    prob_ab = probability_ab(prob_a,prob_b)
    """
    print("Losowa liczba:", random_numb)
    print("Wartość prawdopodobieństwa A:", prob_a)
    print("Wartość prawdopodobieństwa B:", prob_b)
    print("Wartość prawdopodobieństwa AB:", prob_ab)
    """

    if random_numb > prob_a:
        teamA[2] += 3
    elif random_numb > prob_b:
        teamB[2] += 3
    else:
        teamA[2] += 1
        teamB[2] += 1





def simulation(teams, e):
    for a in range(0, len(teams)):
        teamA = teams[a]
        for b in range(a+1, len(teams)):
            teamB = teams[b]
            if teamA[0] == teamB[0]:
                continue
            for i in range(2):
                match(teamA,teamB,e)
    points = 0
    print("After game")
    for a in teams:
        print(a)
        points += a[2]
    print(f"avg: {points/len(teams)}")
    for a in teams:
        a[2] = 0
    random.shuffle(teams)
    return points/len(teams)


