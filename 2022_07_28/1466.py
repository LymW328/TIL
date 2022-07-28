
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         


# class Rectangle(): #??
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2
    
    
    
#     def get_area(Rec):
#         print(Point(1, 3))
#         print(p1)
#         return abs((p1[0] - p2[0]) * (p1[1] - p2[1]))

    
#     def get_primter(Rec):
#         return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))
    
#     def is_square(Rec):
#         if p1[0] != p2[0] and p1[1] != p2[1]:
#             return True
#         else:
#             return False


class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        return abs((self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)) #이중 인스턴스읠 쓴ㄴ 법~!!
        

    
    def get_primeter(self):
        return 2 * (abs(self.p2.x - self.p1.x) + abs(self.p2.y - self.p1.y))
    
    def is_square(self):
       return (abs(self.p2.x - self.p1.x) == abs(self.p2.y - self.p1.y))







p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_primeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_primeter())
print(r2.is_square())
