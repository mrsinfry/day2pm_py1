
def isPositive(n):
    return n>=0

data=[5,78,78,100,-12,78,-4]


import math

#data=list(filter(isPositive, data))
data=list(filter(lambda n: n>=0, data))
print(data)

result=list(map(math.sqrt, data))

print(result)

