class point :
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        x=self.x+other.x
        y=self.x+other.y
        return point(x,y)
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __lt__(self,other):
        if self.x<other.x:
           print("object1>object2") 
        else:
             print("object2>object1")
            
p1=point(12,12)
p2=point(12,12)
p3=p1+p2
print(p3)
