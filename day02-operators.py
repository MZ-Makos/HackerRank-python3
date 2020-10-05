"""
Given the meal price (base cost of a meal), 
tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) for a meal, 
find and print the meal's total cost.

Print the total meal cost, where it is the rounded integer result of the entire bill ( with added tax and tip).

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = 12.00
    tip_percent = 20
    tax_percent = 8
    
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

tip = meal_cost * tip_percent /100
tax = meal_cost * tax_percent /100
totalCost = meal_cost + tip + tax
print(round(totalCost))

solve(meal_cost, tip_percent, tax_percent)
