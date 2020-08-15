#!/usr/bin/python

#  permutations with replacement ()
# permutation - same values, differnt orders
import sys

poss_plays = [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]


# ~~~~~~~~~~~~~~~~~~~~~ first step ~~~~~~~~~~~~~~~~~~~~~  #

# # began thinking about the problem by solving for n = 1

# def rock_paper_scissors(n):
#   # big array which is the outer array to hold the individual outcomes
#   outcomes = []
#   # possible plays
#   plays = ['rock', 'paper', 'scissors']

#   result = []
#   for play in plays:
#     results.append(play)

#   outcomes.append(results)

# ~~~~~~~~~~~~~~~~~~~~~ second step ~~~~~~~~~~~~~~~~~~~~~  #

# # then moved to recursive solution, but could use some of the code he had written

# def rock_paper_scissors(n):
#   outcomes = []
#   plays = ['rock', 'paper', 'scissors']

#   def find_outcome(rounds_left, result):
#     # the first time this loop runs, result is an empty list, the second time we call it with "paper", the third "scissors", and then each of those runs the same function on itself
#     for play in plays:
#       find_outcome(rounds_left - 1, result + [play]) # `result + [play]` creates a new list

#   find_outcome(n, [])

#   return outcomes

# ~~~~~~~~~~~~~~~~~~~~~ third step ~~~~~~~~~~~~~~~~~~~~~  #

# # but that was infinitely recursive
# # we didn't have a base case

# def rock_paper_scissors(n):
#   outcomes = []
#   plays = ['rock', 'paper', 'scissors']

#   def find_outcome(rounds_left, result):
#     if rounds_left == 0:
#       return
#     for play in plays:
#       find_outcome(rounds_left - 1, result + [play]) 

#   find_outcome(n, [])

#   return outcomes

# ~~~~~~~~~~~~~~~~~~~~~ fourth step ~~~~~~~~~~~~~~~~~~~~~  #

# still not done 
# we are storing our results, but we aren't appending them our outcomes list
# 

def rock_paper_scissors(n):
  outcomes = []
  plays = ['rock', 'paper', 'scissors']

  def find_outcome(rounds_left, result):
    if rounds_left == 0:
      outcomes.append(result)
      return
    for play in plays:
      find_outcome(rounds_left - 1, result + [play]) 

  find_outcome(n, [])

  return outcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


# ~~~~~~~~~~~~~~~~~~~~~ an aside ~~~~~~~~~~~~~~~~~~~~~  #
# #  the behaves the same as a loop, 
# # things that call themselves with n-1 might be a good clue that's what we are dealing with
# rock, paper scissors is not like a simple loop, because it makes three calls to itself (it's in a loop), where hello only makes one call to itself

# def hello(n):
#   if n == 0:
#     return
  
#   print('Hello!')
#   hello(n-1)

# hello(10)

# ~~~~~~~~~~~~~~~~~~~~~ an aside ~~~~~~~~~~~~~~~~~~~~~  #

# this can be seen in functional programming patterns, - in some fpl you can't change the value of variables so you pass them to functions and return a new list
# #  the accumulator pattern
# #  the `results` that we built up along the way wind up garbage collected
# #  this was intentional in this case as we only wanted the final array

# def hello(n, result):
#   if n == 0:
#     return result

#   return hello(n-1, result + [n])
# result = hello(10, [])

# hello(10, [])

# # n   results
# # ============
# # 10    []
# # 9     [10]
# # 8     [10, 9]
# # 7     [10, 9, 8, 7]
# # .
# # .
# # .
# # 0     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 

