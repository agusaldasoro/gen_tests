'''
Created on Sep 1, 2016

@author: galeotti
'''

def youngest(ages):
    if len(ages) == 0:
        return None
    
    min_age = None
    for name in ages.keys():
        age = ages[name]
        if age < min_age:
            min_age = age
    
    return min_age


def oldest(ages):
    if len(ages) == 0:
        return None
    
    max_age = None
    for name in ages.keys():
        age = ages[name]
        if age > max_age:
            max_age = age
    
    return max_age

def _typeHint():
    youngest({"Michael": 12, "John":10})
    oldest({"Michael": 12, "John":10})
