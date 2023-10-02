#!/usr/bin/bash

"""we are in search of the median of two sorted arrays
so we first merge them to one array to get one array first"""

def median(arr1, arr2)
new_arr = []
i = j = 0
middle

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
	new_arr.append(arr1[i])
            i += 1
    else:
        new_arr.append(arr2[j])
            j += 1

"""incase there are others"""
new_arr.extend[i:]
new_arr.extend[j:]

"""total lenght"""
total = len(new_arr)
middle = total // 2
if total % 2 == 0:
    median = (new_arr[middle] + new_arr[middle - 1]) / 2
    """check for the median"""
else:
    median = (new_arr[middle])

return median
