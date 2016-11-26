'''
Created on Sep 1, 2016

@author: galeotti
'''

def array_max(int_sequence):
    max_value = None
    
    for i in int_sequence:
        if (max_value == None or max_value < i):
            max_value = i
            
    return max_value

def array_min(int_sequence):
    min_value = None
    
    for i in int_sequence:
        if (min_value == None or min_value > i):
            min_value = i
            
    return min_value

def array_sum(int_sequence):
    sum_value = 0 
    
    for i in int_sequence:
        sum_value += i
            
    return sum_value

def array_avg(int_sequence):
    sum_value = array_sum(int_sequence)
    avg_value = sum_value / len(int_sequence)
    return avg_value

def __typeHints():
    array_max([0])
    array_min([0])
    array_sum([0])
    array_avg([0])
