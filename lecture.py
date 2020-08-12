import math
from itertools import combinations

radius = 3
area = math.pi * radius * radius

print(f"The area of the circle is {area:.3f}")

# return the area with max three decimal places

# Too general -------------- sweet spot ---------------- Too Specific
# Too general Python forat numbers

# Too specific
## Python how to get the area of a circle to three decimal places

# sweet spot
# Python how to format numbers to three decimal places in f-strings?


def divides_self(num):
    # copy num
    digits_left = num
    #loop through all digits in num
    while digits_left> 0:
        # num % 10 to GET the digit on the RHS
        digit = digits_left % 10
        # if tht result is 0, return false
        if digit == 0:
            return False
        # if num % result is Not 0, return false
        if num % digit != 0:
            return False
        # //10 to chop off the digit on RHS
        digits_left//=10 # digits_left // 10

import random
import time


def brute_knapsack(sack, items):
    '''Try every combination to find the best'''
    combos = []

    for i in range(1, len(items) + 1):
        # calculate the value of all combinations
        list_of_combos = list(combinations(items, i))
        for combo in list_of_combos:
            combos.append(list(combo))

    best_value = -1
    # for each combo, add up all the wieght and value of the items and save the best one
    for combo in combos:
        value = 0
        weight = 0
        for item in combo:
            value += item.value
            weight += item.weight
        if weight <= 50 and value > best_value:
            best_value = value
            # this is the combo that is the best we have seen so far, set the sack to this combo
            sack = combo
    return sack




class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.efficiency = 0

    def __str__(self):
        return f'{self.name}, {self.weight} lbs, ${self.value}'

def naive_fill_knapsack(sack, items):
    '''# Put highest value items in knapsack until full (other basic, naive approaches exist)'''
    # TODO - sort items by value

    # TODO put most valuable items into nknapsack until full