'''
Created on Sep 1, 2016

@author: galeotti
'''

def set_max(int_set):
    max_value = None
    
    for i in int_set:
        if (max_value == None or max_value < i):
            max_value = i
            
    return max_value

def set_min(int_set):
    min_value = None
    
    for i in int_set:
        if (min_value == None or min_value > i):
            min_value = i
            
    return min_value

def set_sum(int_set):
    sum_value = 0 
    
    for i in int_set:
        sum_value += i
            
    return sum_value

def set_avg(int_set):
    sum_value = set_sum(int_set)
    avg_value = sum_value / len(int_set)
    return avg_value

def __typeHints():
    set_max(set([0,1,2]))
    set_min(set([0,1,2]))
    set_sum(set([0,1,2]))
    set_avg(set([0,1,2]))
