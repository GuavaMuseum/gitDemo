#
#
#
#
#

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def abs_sub(a, b):
    if a > b:
        return a - b
    return b - a


class MyClass():
    def __init__(self, _name=""):
        self.name = _name
