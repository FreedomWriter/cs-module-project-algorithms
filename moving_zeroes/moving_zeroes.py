'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # loop through arr
    for num in arr:
        # if the current number is zero, remove it from the list then add it to the end of the list
        if num == 0:
            arr.remove(num)
            arr.append(0)
        # return the list
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")