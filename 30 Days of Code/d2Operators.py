
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    tip = (tip_percent*meal_cost)/100
    tax = (tax_percent*meal_cost)/100

    total_cost = round (tip + tax + meal_cost)


    print("The total meal cost is {} dollars.".format(total_cost))


solve(meal_cost, tip_percent, tax_percent)
