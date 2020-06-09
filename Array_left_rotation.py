#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    def leftRotate(a, n, d): 
        # To get the starting point of rotated array 
        mod = d % n 
        
  
    # Prints the rotated array from start position 
        for i in range(n): 
            print (str(a[(mod + i) % n]), end = ' ')
(leftRotate(a, n, d))
