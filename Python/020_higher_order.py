def sum_number(x):
    return sum(x)

def higher_orderfunction(f,lst):
    var = f(lst)
    return var

result = higher_orderfunction(sum_number,[1,2,3])
print(result)