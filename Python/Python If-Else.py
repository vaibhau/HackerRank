#!/bin/python3

import math
import os
import random
import re
import sys

n=int(input())
if n%2 != 0:
    print("Weird")
elif n%2==0:
    if 2<=n and n<=5:
        print("Not Weird")
    elif 6<=n and n<=20:
        print("Weird")
    elif n>=20:
        print("Not Weird")
    else:
        print("Not Weird")
