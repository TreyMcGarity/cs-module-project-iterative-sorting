def linear_search(arr, target):
    # Your code here

    #parse through whole array
    for i in range(len(arr)):
        #if current value is target
        if arr[i] == target:
            #return index of current value
            return i 
    return -1   # not found


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
            #set index of high to index of middle - 1
            high = mid - 1
        # if neither
        else:
            #set index of low to index of middle + 1
            low = mid + 1
    return -1  # not found
