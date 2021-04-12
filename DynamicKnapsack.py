# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:30:49 2021

@author: ersoy
"""
import random
from Greedy import *
#Using a decision tree to solve a knapsack problem

def max_val(to_consider, avail):
    """
    Assumes to_consider a list of items, avail a weight
    Returns a tuple of the total value of a solution to the
    0/1 Knapsack problem and the items of that solution
    """
    
    if to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        result = max_val(to_consider[1:], avail)
    else:
        next_item = to_consider[0]
        print(f'This next_item: {next_item}.')
        
        #Explore left branch
        with_val, with_to_take = max_val(to_consider[1:], avail - next_item.get_weight())
        with_val += next_item.get_value()
        
        #Explore right branch
        without_val, without_to_take = max_val(to_consider[1:], avail)
        
        #Choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
            if with_to_take != ():
                print(with_val, with_to_take[0].get_name(), (next_item,)[0].get_name())
            else:
                 print(with_val, with_to_take, (next_item,)[0].get_name())
        else:
            result = (without_val, without_to_take) 

    return result

# Dynamic programming solution to knapsack problem

def fast_max_val(to_consider, avail, memo = {}):
    """
    Assumes to_consider a list of items, avail a weight
    Returns a tuple of the total value of a solution to the
    0/1 Knapsack problem and the items of that solution
    """
    
    if (len(to_consider), avail) in memo:
        result = memo[(len(to_consider), avail)]
    elif to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        #Explore right branch only
        result = fast_max_val(to_consider[1:], avail, memo)
    
    else: 
        next_item = to_consider[0]
        
        #Explore left branch
        with_val, with_to_take = fast_max_val(to_consider[1:], avail - next_item.get_weight(), memo)
        with_val += next_item.get_value()
        
        #Explore right branch
        without_val, without_to_take = fast_max_val(to_consider[1:], avail, memo)
        
        #Choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    
    memo[(len(to_consider), avail)] = result
    return result

###
### HELPER TESTING CODES
###


def small_text():
    
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    
    val, taken = max_val(Items, 5)
    
    # for item in taken:
    #     print(item)
    # print('Total value of items taken =', val)

def Burglar():
    Items = build_items()
    val, taken = fast_max_val(Items, 20)
    for item in taken:
        print(item)
    print('\nTotal value of items taken =', val)
    
def build_many_items(num_items, max_val, max_weight):
    
    items = []
    for i in range(num_items):
        items.append(Item(str(i), random.randint(1, max_val), random.randint(1, max_weight)))
    return items

def big_test(num_items, avail_weight):
    
    items = build_many_items(num_items, 10, 10)
    val, taken = max_val(items, avail_weight)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken =', val)

def big_test2(num_items, avail_weight):
    
    items = build_many_items(num_items, 10, 10)
    val, taken = fast_max_val(items, avail_weight)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken =', val)

###

# small_text()