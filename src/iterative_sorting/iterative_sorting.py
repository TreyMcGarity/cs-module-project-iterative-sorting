# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        for j in range(cur_index, len(arr)):
            #if value is smaller than minimum value
            if arr[j] < arr[smallest_index]:
                #set value to new minimum
                smallest_index = j

        # TO-DO: swap
        # Your code here

        #save current value
        temp = arr[cur_index]
        #switch current and mininmum values
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    length = len(arr)
  
    # traverse through all array elements 
    for i in range(length):   
        # traverse until second from last 
        for j in range(0, length-1): 
            # if the value is greater than right value
            if arr[j] > arr[j+1]:
                #save current value
                temp = arr[j]
                # switch current and right of current
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    #if length is zero
    if len(arr) == 0:
        # throw back empty input
        return arr
    #if no max
    if maximum is None:
        #set max
        maximum = max(arr)
    buckets = [0 for i in range(maximum+1)]

    #loop through our arr
    for value in arr:
        #if a negative number is found
        if value < 0:
            # throw error
            return "Error, negative numbers not allowed in Count Sort"
        # for each distinct arr value, increment arr[value] by 1
        buckets[value] += 1
        # buckets holds array of counts of every distinct value in input array

    output = []
    # loop through our buckets array
    for index, bucket in enumerate(buckets):
        # for the current count
        output.extend([index for i in range(bucket)])
        # add that many values to an output array

    return output