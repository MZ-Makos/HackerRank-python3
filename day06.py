"""
Day 6: Let's Review
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.
Note: 0 is considered to be an even index.
"""
import math
import os
import random
import re
import sys

def odd_indexes(s,len_s):
    output = ""
    for i in range(0,len_s,2):
        output += s[i]
    return output

def even_indexes(s,len_s):
    output = ""
    for i in range(1,len_s,2):
        output += s[i]
    return output

t = int(input()) #number of cases
for i in range(0,t):
    s = input()
    len_s = len(s)
    print(odd_indexes(s,len_s), even_indexes(s,len_s))