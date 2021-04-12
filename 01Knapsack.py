# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:29:26 2021

@author: ersoy
"""
from Greedy import *


def get_binary_rep(n, num_digits):
    """Assumes n and numDigits are non-negative ints
       Returns a str of length numDigits that is a binary
       representation of n"""
    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n // 2
    if len(result) > num_digits:
        raise ValueError('not enough digits')
    for i in range(num_digits - len(result)):
        result = '0' + result
    return result

def gen_powerset(L): # O(2^n)
    """Assumes L is a list
       Returns a list of lists that contains all possible
       combinations of the elements of L. E.g., if
       L is [1, 2], it will return a list with elements
       [], [1], [2] and [1, 2]."""
    
    powerset = []
    for i in range(0, 2**len(L)):
        bin_str = get_binary_rep(i, len(L))
        subset = [L[j] for j in range(len(L)) if bin_str[j] == '1']
        powerset.append(subset)
    return powerset

### 0/1 KNAPSACK ALGORITHM
def choose_best(pset, max_weight, get_val, get_weight):
    
    best_val, best_set = 0.0, None
    
    for items in pset: # O(2^n) --> gen_powerset(n)
        items_val, items_weight = 0.0, 0.0
        
        for item in items: # O(n), n = len(items)
            items_val += get_val(item)
            items_weight += get_weight(item)
        
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items
    
    return (best_set, best_val)

###
### HELPER TESTING CODES
###

def test_best(max_weight = 20):
    items = build_items()
    pset = gen_powerset(items)
    taken, val = choose_best(pset, max_weight, Item.get_value, Item.get_weight)
    print('\nTotal value of items taken is', val)
    for item in taken:
        print(item)

test_best()

###

