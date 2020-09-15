def linear_search(arr, target):
    # Your code here

    #parse through whole array
    for i in range(len(arr)):
        #if current value is target
        if arr[i] == target:
            #return index of current value
            return i 
    return -1   # not found

#initial state for binary search
# data = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# target = 10

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    #low value is index 0 and high is index of end
    low = 0 
    high = len(arr) - 1

    while low <= high:
        # middle of list is low + high divided by two
        mid = (low + high) // 2
        # if target is middle value
        if target == arr[mid]:
            #return index of middle value
            return mid
        # if target is less than middle value 
        elif target < arr[mid]:
            # make high index one less than middle index
            # to cut top half out at middle index
            high = mid - 1
        # if neither
        else:
           # make low index one greater than middle index
            # to cut bottom half out at middle index           
            low = mid + 1
    return -1  # not found
"""
INDEXES:
target = -8     |target = 10

 0 low          | 0 low
 6 mid          | 6 mid
 13 high        | 13 high
less than       |greater
                |
 0 low          | 7 low
 2 mid          | 10 mid
 5 high         | 13 high
less than       |greater
                |
 0 low          | 11 low
 0 mid          | 12 mid
 1 high         | 13 high
greater         |greater
                |
 1 low          | 13 low
 1 mid          | 13 mid
 1 high         | 13 high
equals          |greater

returns 1       returns -1
# index of -8   #false index
"""
print(binary_search(data, target))