'''
Created on Sep 1, 2016

@author: galeotti
'''
from math import sqrt

def euclidean_dist(p,q):
    if not len(p) == len(q):
        raise ValueError("Illegal Input: Both vectors should have the same dimension")
    
    sum_value = 0
    for i in range(0, len(p)):
        dist = q[i] - p[i]
        sum_value = sum_value + dist * dist 
        
    return sqrt(sum_value)


def __typeHints():
    euclidean_dist((0),(0))
    euclidean_dist((0,0),(0,0))
    euclidean_dist((0,0,0),(0,0,0))