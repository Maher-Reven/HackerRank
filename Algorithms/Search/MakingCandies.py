#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(machines, workers, price, target):
    iter = 0
    coins = 0

    def new_infra(n_items):
        new_machines = machines
        new_workers = workers
        
        delta = max(new_machines, new_workers) - min(new_machines, new_workers)
        # delta is bounded by number of items we can afford
        delta = min(delta, n_items)
        
        rest = n_items - delta
        a,b = rest // 2, rest // 2
        #f rest of items to distribute is odd, add extra 1 (since 7//2 is 3) to any item
        if rest & 1: b += 1
        
        if new_machines < new_workers: 
            new_machines += delta
        else:
            new_workers += delta
            
        new_machines += a
        new_workers += b
        
        return new_machines, new_workers
    
    def items_worth_buying():
        n_items = coins // price
        rest_coins = coins - n_items * price
        
        new_machines, new_workers = new_infra(n_items)
        rem_days_if_buying = math.ceil(float(target - rest_coins) / (new_machines * new_workers))
        rem_days_if_not_buying = math.ceil(float(target - coins) / (machines * workers))

        # always prefer buying rather than saving
        # by saving to improvement can be achieved
        return n_items if rem_days_if_buying <= rem_days_if_not_buying else -1

    while True:
        speed = machines * workers
        next_improv_iter = int(math.ceil(float(price - coins) / speed))
        rem_iter_till_finish = int(math.ceil(float(target - coins) / speed))

        if next_improv_iter >= rem_iter_till_finish:
            return iter + rem_iter_till_finish
        
        ## improvement will happen earlier than finish
        n_items = items_worth_buying()
        if n_items == -1:
            ## -1 indicates that if we are buying new items, we are still not faster 
            ## if that's the case, we already know the end date
            return iter + rem_iter_till_finish
        
        coins_prod_till_next_improv_iter = next_improv_iter * speed
        coins += coins_prod_till_next_improv_iter

        machines, workers = new_infra(n_items)
        coins -= price * n_items

        iter += next_improv_iter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
