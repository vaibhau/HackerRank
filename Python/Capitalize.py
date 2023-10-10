#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    ans = []
    for i in s.split(" "):
        if i.isalpha():
            ans.append(i.capitalize())
        else:
            ans.append(i)
    return " ".join(ans)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
