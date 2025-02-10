# def sum(a,b):
#     return a+b

# print(sum(2,5))


# mysum = lambda a,b: a+b
# print(mysum(7,8))

# print((lambda a,b: a+b)(2,4))

#example of a lambda function on another function

def power(x):
    return lambda n : x**n

print(power(5)(2))