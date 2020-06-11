#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    b = arr[n-1]
    #print(b)
    for i in range (0,(len(arr)-1)):
        if arr[n-2] > b:
            arr[n-1] = arr[n-2]
        else:
            arr[n-1] = b
            print(" ".join([str(x) for x in arr]))
            break
        
        print(" ".join([str(x) for x in arr]))
        
        n = n-1
    if b < min(arr):
        arr[0] = b
        print(" ".join([str(x) for x in arr]))
    


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    

    insertionSort1(n, arr)
