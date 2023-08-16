import random


def linear_search_max(list, target):
    max = list[0]
    for i in range(0, len(list)):
        if list[i] > max:
            max = i
    return max

list = []
for i in random.rangrange(1, 20):
    list.append(i)

linear_search_max(list)