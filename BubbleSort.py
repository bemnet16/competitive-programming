#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'countSwaps' function below.
# The function accepts INTEGER_ARRAY a as parameter.


def countSwaps(a):
    numSwaps = 0
    for i in range(len(a) - 1):
        isSwaps = 0
        for j in range(len(a) - i -1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwaps += 1
                isSwaps += 1
        if isSwaps == 0:
            break
            
    firstElement = a[0]
    lastElement = a[len(a) - 1]
    
    print("Array is sorted in", numSwaps, "swaps.")
    print("First Element:", firstElement)
    print("Last Element:", lastElement)
    
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
