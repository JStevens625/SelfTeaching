class Point():
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y
        self.coordinates = (self.x,self.y)
    
    def move(self,x,y):
        self.x += x
        self.y += y

    def __add__(self,point):
        return Point(self.x + point.x, self.y + point.y)
    
    def __sub__(self,point):
        return Point(self.x - point.x, self.y - point.y)
    
    def __mul__(self,point):
        return Point(self.x * point.x + self.y * point.y)
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


point1 = Point(3,4)
point2 = Point(3,2)
point3 = Point(1,3)
point4 = Point(0,1)

point5 = point1 + point2
point6 = point4 - point1
point7 = point2 * point3
print(f"point 5: {point5}\npoint 6: {point6}\npoint 7: {point7}")