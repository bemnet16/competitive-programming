#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'insertionSort1' function below.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr

def insertionSort1(n, arr):
    
    #Check if the length is valid or not
    if n < 1 or n > 1000:
        return "Invalid list"
    
    for i in range((n - 1),0,-1):
        count = 0
        for j in range((n - 1),(n - i - 1),-1):
            val = 0
            
            #check the value is valid or not
            if arr[j] > 10000 or arr[j] < -10000:
                return "Invalid value"
            elif arr[j] < arr[j - 1]:
                val = arr[j]
                arr[j] = arr[j - 1]
                print(*arr)
                arr[j - 1] = val
    print(*arr)
    
          #To check if the array is already sorted or not we can include this to the code
                # arr[j], arr[j - 1] = arr[j - 1], arr[j]
                # count += 1
        # if count == 0:
        #     break
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
