import math


def sd(array):
    mean = sum(array)/len(array)
    result = 0
    for a in array:
        result += (a-mean)**2
    result = math.sqrt(result/len(array))
    return result

def t(mean_p, mean_h, sd):
    return (mean_p-mean_h)/sd