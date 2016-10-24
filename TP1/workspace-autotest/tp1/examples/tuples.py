# Ideas:

# Check capability of creating tuples

def vectorAdd(a, b):
    if len(a)!=3 or len(b)!=3:
        raise ValueError("Illegal Input: Both vectors should have the dimension 3")
    (a1, a2, a3) = a
    (b1, b2, b3) = b
    return (a1 + b1, a2 + b2, a3 + b3)

# Check tuples with various types

def addToList(t):
    if len(t)!=2:
        raise ValueError("addToList() expects a tuple of size 2")
    n, l = t
    return [x + n for x in l]

# Check polymorphism in tuples

# Check usage of tuple components

def binom(a, b):
    return (a, b, a * a + 2 * a * b + b * b)

def checkBinom(a, b, c):
    if c == a * a + 2 * a * b + b * b:
        return True
    else:
        return False

def _typeHint():
    vectorAdd((0, 0, 0), (0, 0, 0))
    addToList((0, [0]))
    binom(0, 0)
    checkBinom(0, 0, 0)
