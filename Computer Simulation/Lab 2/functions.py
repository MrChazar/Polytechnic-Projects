import random
import math


def determine_score(distance):
    if distance < 0.1:
        return 6
    elif distance < 0.2:
        return 5
    elif distance < 0.3:
        return 4
    elif distance < 0.4:
        return 3
    elif distance < 0.5:
        return 2
    elif distance < 0.6:
        return 1
    else:
        return 0


def generate_shield():
    array = []
    for y in range(20, -21, -1):
        row = []
        for x in range(-20, 21):
            distance = math.sqrt((x / 20) ** 2 + (y / 20) ** 2)
            score = determine_score(distance)
            row.append(score)
        array.append(row)
    for row in array:
        print(row)
    return array


def shoot_a():
    x = random.uniform(-0.75, 0.75)
    y = random.uniform(-0.75, 0.75)
    return [x, y]


def shoot_b():
    r = random.uniform(0, 0.75)
    phi = random.uniform(-3.14, 3.14)
    x = r*math.cos(phi)
    y = r*math.sin(phi)
    return [x,y]


def simulation(shield, type_of_shoot):
    temp = 0
    for _ in range(10):
        if type_of_shoot == "A":
            x, y = shoot_a()
        elif type_of_shoot == "B":
            x, y = shoot_b()
        # Normalization to -1 to 1
        x_norm = int(20 * x)
        y_norm = int(20 * y)
        # checking score
        if -20 <= x_norm <= 20 and -20 <= y_norm <= 20:
            score = shield[20 - y_norm][x_norm + 20]
            print(f"Hit at coordinate ({x_norm / 20}, {y_norm / 20}) score: {score}")
            temp += score
        else:
            print("beyond shooting shield")
    return temp/10
