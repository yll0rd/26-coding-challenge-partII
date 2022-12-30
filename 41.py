from math import sqrt


def disbtwpoints(x1, x2, y1, y2):
    return sqrt(((x1-x2)**2)+((y1-y2)**2))

x_1, y_1 = [eval(i) for i in input("Enter the x and y coordinates of the first point: ").split()]
x_2, y_2 = [eval(i) for i in input("Enter the x and y coordinates of the second point: ").split()]
print(f"The distance between ({x_1},{y_1}) and ({x_2},{y_2}) is {disbtwpoints(x_1, x_2, y_1, y_2)}")
