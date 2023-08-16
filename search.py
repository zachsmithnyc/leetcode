import random


def linear_search_max(list):
    max = list[0]
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
    return max

list = [100, 10, 20 , 40, 200, 33, 43, 11]

print(linear_search_max(list))