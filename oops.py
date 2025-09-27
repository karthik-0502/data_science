#create a point 
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def get_coordinates(self):
        return (self.x , self.y)




my_point = point(10,15)
print( my_point.get_coordinates())
    