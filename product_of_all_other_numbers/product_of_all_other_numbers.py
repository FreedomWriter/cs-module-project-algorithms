'''
Input: a List of integers
Returns: a List of integers
'''

from operator import mul
from functools import reduce
## DIVIDES - NOT A VIABLE ANSWER, BUT IT'S NEAT!!
# def product_of_all_other_numbers(arr):
#     answer = reduce(mul, arr, 1)
#     return [answer // i for i in arr]

def product_of_all_other_numbers(arr):
    saved = 1
    cur_index = 0
    answer = []
    for i in range(len(arr)):
        # print(f"i:{i}") 
        while cur_index <= len(arr) -1 :
            # if the cur_index is the same as the i we are at, skip that item
            if cur_index == i:
                pass
            # if the cur_index is not equal to i then update saved by multiplying it by the number in the arr at the cur_index
            else:
                saved *= arr[cur_index]
            # increment the cur_index
            cur_index +=1
        # reset the cur_index holder
        cur_index = 0
        # add the saved values to the 
        answer.append(saved)
        saved = 1
    return answer

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
