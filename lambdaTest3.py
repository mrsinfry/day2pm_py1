
# def fct(a, b):
#     return a+b

data=[5,6,77,77,9,9,10]


import functools

plus=lambda a,b: a+b

data=functools.reduce(plus, data, 0)
print(data)


