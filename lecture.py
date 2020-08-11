import math

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
        digiit = digits_left % 10
        # if tht result is 0, return false
        if digit == 0:
            return False
        # if num % result is Not 0, return false
        if num % digit != 0:
            return False
        # //10 to chop off the digit on RHS
        digits_left//=10 # digits_left // 10

import randomimport time
from intertools import combinations

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