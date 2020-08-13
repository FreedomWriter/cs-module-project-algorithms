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

  def greedy_knpasack():
    for i in items:
      i.efficiency = i.value / i.weight

    items.sort(key= lambda x: x.efficiency, reverse=True)

    sack = []

    weight = 0
    for i in items:
      weight = += i.weight
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