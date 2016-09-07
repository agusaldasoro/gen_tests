'''
Created on Sep 1, 2016

@author: galeotti
'''
NOT_A_TRIANGLE = -1
EQUILATERAL_TRIANGLE = 0
ISOSCELES_TRIANGLE = 1
SCALENE_TRIANGLE = 2

def triang(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return NOT_A_TRIANGLE 
    elif a == b == c:
        return EQUILATERAL_TRIANGLE 
    elif a == b or b == c or a == c:
        return ISOSCELES_TRIANGLE 
    else:
        return SCALENE_TRIANGLE

def __typeHints():
    triang(0,0,0)