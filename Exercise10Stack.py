class Stack:
    def __init__(self, sz):
        self.maxSize=sz
        self.content=[]
    def __len__(self):
        return len(self.content)
    def __str__(self):
        return f"{len(self.content)}/{self.maxSize} {self.content}"
    def isEmpty(self):
        return len(self.content)==0
    def isFull(self):
        return len(self.content)==self.maxSize
    def pop(self):
        if self.isEmpty():
            print("The stack is empty!!")
            return None
        else:
            return self.content.pop()
    def push(self, obj):
        if self.isFull():
            print("The stack is full!!")
            return None
        else:
            self.content.append(obj)
    
st=Stack(10) # a Stack is a LIFO container with a maximum size of 10 elements
st.push(345)
st.push(567)
st.push(10)
print(st) # 3/10 [345,567,10]
top=st.pop() # 10
print (top)
print(st) # 2/10 [345,567]
top=st.pop() # 567
print (top)
print(st) # 1/10 [345]
top=st.pop() # 345
print(st) # 0/10 []

# Attributes:
#   a list (to hold the stack elements)
#   an int (the maximum size of the stack)
# Methods:
#   isEmpty(), isFull(), push(), pop(), __init__(), __str__(), __len__()
#   in == != 