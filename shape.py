import math
'''Importing math module to find the sqaure root'''
class Shape:
    '''creating class'''
    def __init__(self, side):
        self.side = side
    def triangle(self, breath, height):
        '''calculate the area of traingle'''
        self.breath = breath
        self.height = height
        area = 0.5* self.breath*self.height
        return area
    def square(self, area):
        '''calculate the area of square'''
        area = area* area
        return area
    def pentagon(self, area):
        '''calculate the area of pentagon'''
        area = 1.72* area*area
        return area
    def hexagon(self, area):
        '''calculate the area of hexagon'''
        area = (math.sqrt(3))*1.5*area*area
        return area
    def heptagon(self, area):
        '''calculate the area of heptagon'''
        area = 3.64*self.area*self.area
        return area
    def octagon(self, area):
        '''calculate the area of octagon'''
        area = 2*(1+math.sqrt(2))*area*area
        return area
    def nonagon(self, area):
        '''calculate the area of nonagon'''
        area = 6.18183*area*area
        return area
    def decagon(self, area):
        '''calculate the area of decagon'''
        area = area*area*7.694
SIDE = int(input("enter the no side"))
OBJ = Shape(SIDE)
if SIDE == 3:
    print("It is a triangle")
    B = int(input("Enter the value of base"))
    H = int(input("Enter the value of height"))
    C = OBJ.triangle(B, H)
    print("The area of the triangle ", C)
elif SIDE == 4:
    print("It is a square")
    VAL = int(input("Enter the value of side"))
    C = OBJ.square(VAL)
    print("The area of the square ", C)
elif SIDE == 5:
    print("It is a pentagon")
    VAL = int(input("Enter the value of side"))
    C = OBJ.pentagon(VAL)
    print("The area of the pentagon ", C)
elif SIDE == 6:
    print("It is a hexagon")
    VAL = int(input("Enter the value of side"))
    C = OBJ.hexagon(VAL)
    print("The area of the hexagon", C)
elif SIDE == 7:
    print("It is a heptagon")
    VAL = int(input("Enter the value of side"))
    C = OBJ.heptagon(VAL)
    print("The area of the heptagon", C)
elif SIDE == 8:
    print("It is octagon")
    VAL = int(input("Enter the value of side"))
    C = OBJ.octagon(VAL)
    print("The area of the octagon", C)
elif SIDE == 9:
    print("It is a nonagon")
    VAL = int(input("Enter the value of side"))
    C = OBJ.nonagon(VAL)
    print("The area of the nonagon", C)
elif SIDE == 10:
    print("It is a decagon")
    VAL = int(input("Enter the value of side"))
    C = OBJ.decagon(VAL)
    print("The area of the decagon", C)
else:
    print("Thankyou")
