from math import sqrt


def checkintersect(x1, y1, rad1, x2, y2, rad2):
    dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if dist == (rad1 + rad2) or dist == abs(rad1 - rad2):
        return True
    return False

x_1,y_1=[int(i) for i in input("Enter the x and y coordinates of the center of the first circle: ").split()]
x_2,y_2=[int(i) for i in input("Enter the x and y coordinates of the  center of the second circle: ").split()]
rad_1 = int(input("Enter the radius of the first circle: "))
rad_2 = int(input("Enter the radius of the second circle: "))
if checkintersect(x_1,y_1,rad_1,x_2,y_2,rad_2):
    print("The two circles intersect")
else:
    print("The two circles do not intersect")
