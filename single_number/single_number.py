'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# # ## Works but not with tests (because of random.shuffle) - time complexity is trash
# def single_number(arr):
#     # Your code here
#     # if len(arr):
#     #     return arr[0]

#     #loop through the arr - get index
#     for i in range(len(arr) - 1):
#         # print(arr)
#         # store curr_num
#         cur_num = arr[i]
#         arr.pop(i)
#         #loop through arr again, skip cur_num, 
#         for _ in range(len(arr) ):
#         # if cur_num is not present, return cur_num 
#             if cur_num not in arr:
#                 return cur_num
            

# passes tests but doesn't meet space complexity            
def single_number(arr):
     
    temp_list = []
    # loop through arr
    for num in arr:
        # if the num has not yet been added, add it to the temp_list
        if num not in temp_list:
            temp_list.append(num)
        else:
            # if the num is in the temp list, remove it 
            temp_list.remove(num)
    return temp_list.pop()





if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 555, 0, 0, 10, 10, 11, 11, 12,12, 14, 14]

    print(f"The odd-number-out is {single_number(arr)}")