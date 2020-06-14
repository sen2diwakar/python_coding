#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    while True:
        Flag = False
        for i in range (0,(len(a)-1)):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                count = count +1
                Flag = True
                print(a)
        if not Flag:
            break
    print("Array is sorted in", count, "swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[len(a)-1])

#complete swap in one go    
def countSwapsSorted(a):
    a = sorted(a)
    print(a)


a = [3,2,1]

countSwaps(a)
countSwapsSorted(a)
