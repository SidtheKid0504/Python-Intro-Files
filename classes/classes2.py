from classes import Polygon

class Triangle(Polygon):

    def __init__(self):
        Polygon.__init__(self, 3)
    
    def findSemiPerimeterOfTriangle(self):
        a, b, c = self.sides
        semiPerimeter = (a + b + c) / 2

        return semiPerimeter

    def findTriangleArea(self, s):
        a, b, c = self.sides
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(area)
        return area
    
triangle = Triangle()

triangle.inputSides()
# triangle.displaySides()
semiPerimeter = triangle.findSemiPerimeterOfTriangle()
print(semiPerimeter)

area = triangle.findTriangleArea(semiPerimeter)
print("Area: " + str(area))