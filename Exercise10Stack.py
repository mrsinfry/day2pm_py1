class Stack:
    pass


st=Stack(10) # a Stack is a LIFO container with a maximum size of 10 elements
st.push(345)
st.push(567)
st.push(10)
print(st) # 3/10 [345,567,10]
top=st.pop() # 10
print(st) # 2/10 [345,567]
top=st.pop() # 567
print(st) # 1/10 [345]
top=st.pop() # 345
print(st) # 0/10 []

# Attributes:
#   a list (to hold the stack elements)
#   an int (the maximum size of the stack)
# Methods:
#   isEmpty(), isFull(), push(), pop(), __init__(), __str__(), __len__()