def square(x):
    return x**2

def cube(a):
    return a**3

def absolute(b):
    if b >= 0:
        return b
    else:
        return -(b)

def hof(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    else:
        return absolute

res = hof('square')
print(res(10))