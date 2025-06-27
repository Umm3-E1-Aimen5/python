class Polygon:
    def __init__(self,sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight line")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A trinagle is a polygon with 3 edge")

class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadtrilateral is a polygon with 4 edge")        


p1 = Polygon([3,4,5])
p1.display_info()
perimeter = p1.get_perimeter()
print(f'perimeter of polygon is = {perimeter}')  

t1 = Triangle([5,6,7])
perimeter_of_tri = t1.get_perimeter()
t1.display_info()
print(f'perimeter of trinagle is = {perimeter_of_tri}')

q1 = Quadrilateral([1,2,3,4])
perimeter_of_quad = q1.get_perimeter()
q1.display_info()
print(f'perimeter of quadrilateral is = {perimeter_of_quad}')