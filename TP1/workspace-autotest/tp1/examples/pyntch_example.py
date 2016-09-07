'''
Created on Sep 1, 2016

@author: galeotti
'''
def int_example(a, b):
    if (a > b):
        return a
    else:
        return b

def int_set_example(int_set):
    min_value = None
    for i in int_set:
        if min_value == None or i < min_value:
            min_value = i
    return min_value

def int_tuple_example(t0,t1):
    a0,b0 = t0
    a1,b1 = t1
    return a0+a1,b0+b1

def int_list_example(myList):
    return len(myList)

def int_map_example(myMap):
    return len(myMap.keys())

def str_example(myString):
    return len(myString)

def __typeHints():
    int_example(0, 0)
    int_set_example(set([0,1,2,3]))
    int_tuple_example((0,0),(0,0))
    int_list_example([0,1,2,3,4,5,6])
    int_map_example({0:0})
    str_example("Hello World")