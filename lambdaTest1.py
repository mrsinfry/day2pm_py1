
def power(n, p):
    return n**p

data=[5,78,78,100,-12,78,-4]


import functools
square=functools.partial(power, p=2)

result=list(map(square, data))

print(result)

nb=square(10)
print(nb)