'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n, cache ={}):
#     # Your code here
#     #
#     # no or negative cookies return 0
#     # base case
 
#     if n == 0:
#         return 1

#     if n < 0: 
#         return 0
    
#     if n == 1:
#         return 1
#     elif n in cache.keys():
#         return cache[n]

#     else:
#         # make 3 recurive calls with caching
#         value = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
#         cache[n] = value
#         return value

    

def eating_cookies(n, cache=None):
    # setup
    if cache == None:
        cache = [0 for x in range(n+1)]
    # base cases
    if n == 0:
        return 1
    elif n <= 0:
        return 0
    # if value is already in cache
    if cache[n] > 0:
        return cache[n]
    # if value is not in cache
    elif cache[n] == 0:
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
