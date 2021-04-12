# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 11:20:53 2021

@author: ersoy
"""
### KNAPSACK PROBLEMS

class Item(object):
    def __init__(self, n, v, w):
        self._name = n
        self._value = v
        self._weight = w
        
    def get_name(self):
        return self._name
    
    def get_value(self):
        return self._value

    def get_weight(self):
        return self._weight
    
    def __str__(self):
        return f'<{self._name}, {self._value}, {self._weight}>'

def value(item):
    return item.get_value()

def weight_inverse(item):
    return 1.0/item.get_weight()

def density(item):
    return item.get_value()/item.get_weight()

# GREEDY ALGORITHM

def greedy(items, max_weight, key_function):
    
    """Assumes items a list, max_weight >= 0,
        key_function maps elements of items to numbers"""
    
    items_copy = sorted(items, key=key_function, reverse=True) #Order of growth O(nlog(n)), n = len(items)
    result = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(items_copy)): # O(n)
        if (total_weight + items_copy[i].get_weight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    return (result, total_value)

###
### HELPER TESTING CODES
###

def build_items():
    item = {'Clock':175, 'Painting':90, 'Radio':20, 'Vase':50, 'Book':10, 'Computer':200}
    names = list(item.keys())
    values = list(item.values())
    weight = [10, 9, 4, 2, 1, 20]     
    return [Item(names[i], values[i], weight[i]) for i in range(len(values))]

def test_greedy(items, max_weight, key_function):
    taken, val = greedy(items, max_weight, key_function)
    print('\nTotal value of items is', val)
    for item in taken:
        print('  ', item)
        
def test_greedys(max_weight = 20):
    items = build_items()
    print('Use greedy by value to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, value)
    print('\nUse greedy by weight to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, weight_inverse)
    print('\nUse greedy by density to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, density)

# test_greedys()
###
