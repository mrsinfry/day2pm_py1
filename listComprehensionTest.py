

data=(45,6, 67,-5,-7,45, 78,90,6)

result=[]
for e in data:
    result.append(e**2)
print(result) 

result=list(map(lambda e: e**2, data)) 

print(result)

result=[e**2 for e in data] # a list comprehension
print(result)

result=[e**2 for e in data if e > 0] # a list comprehension
print(result)

result={e**2 for e in data if e > 0} # a set comprehension
print(result)

