class Point:
    # def __init__(self, *args):
    #     if len(args) == 0:
    #         self.x=self.y=0
    #     elif len(args) == 2:
    #         self.x=args[0]
    #         self.y=args[1]
    #     else:
    #         print("Wrong number of parameters")
    def __init__(self, a=0, b=0):
        self.x=a # x is a data attribute
        self.y=b # y is a data attribute
    def __str__(self):
        return f"<{self.x},{self.y}>"
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def distance(self, other):
        import math
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2 )
        
center=Point(2,45) # c=complex(45,67.8) l=dict()
print(center)
print(center.x, center.y)
# 1) center=Point.__new__()
# 2) center.__init__(2,3)
# 3) __init__(center, 2, 3)

other=Point() # <0,0>
print(other.x, other.y)
# 1) center=Point.__new__()
# 2) center.__init__()
# 3) __init__(center)

other.x=8
other.y=78

print(other) # <8,78>
# 1) print(str(other))
# 2) print(other.__str__())

print(other)
print(center)
if other == center:
    # if other.__eq__(center):
    print("Equal")
else:
    print("Different")
    
result = other.distance(center)

print(result)


