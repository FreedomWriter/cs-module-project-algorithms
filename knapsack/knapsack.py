#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])



def knapsack_solver(items, capacity):
    # Your code here

    pass

def naive_knapsack(weight_limit, items):
  items.sort(key=lambda x: x.value, reverse=True)
  # could be better if we sorted by value weigth ratio

  sack = []
  cur_weight = 0


  # while there is room in the stack
  for i in range(len(items)):
    # put the next most valuable  item in it (because we sorted the list by value)
    if cur_weight + items[i].weight <= weight_limit:
      sack.append(items[i])
    i += 1
  
  return sack

from itertools import combinations

# PROS- it will find the best combo
# CONS - run time
def brute_knapsack(weight_limit, items):
  all_combos = []
  for i in range(1, len(items)+1):
    list_of_combos = list(combinations(items, i))
    for combo in list_of_combos:
      all_combos.append(combo)

    max_val = -1
    best_combo = None
    for combo in all_combos:
      value = 0
      weight = 0
      for item in combo:
        value += item.value
        weight += item.weight
        if weight <= weight_limit:
          if value > max_val:
            max_val = value
            best_combo = combo

  return best_combo


#faster than brute force
# smarter than niave
#  may not get optimal result
def greedy_knpasack(weight_limit, items):
  for i in items:
    i.efficiency = i.value / i.weight

  items.sort(key= lambda x: x.efficiency, reverse=True)

  sack = []

  weight = 0
  for i in items:
    weight  += i.weight
    if weight > weight_limit:
      return sack
    else:
      sack.append(i)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')


# recursive fib with memeoization

def fib(n):

  if n == 1 or n == 0:
    return 1

  # recursive case
  else:
    return fib(n-1) + fib(n-2)


# by adding cache as an argument, we can make it available to all of the recursive calls
def fib_mem(n, cache = {}):
  
  if n == 1 or n == 0:
    return 1

  # recursive case
  # check to see if we've already made this recursive call first
  elif n in cache.keys():
    return cache[n]
  else:
    value = fib_mem(n-1) + fib_mem(n-2)
    cache[n] = value
    return value