#class to calculate area  and perimeter of a rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length + self.width)

r=Rectangle(6,4)
    
print(r.area())
print(r.perimeter())
    

