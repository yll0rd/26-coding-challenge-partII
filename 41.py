from math import sqrt


def disbtwpoints(x1, x2, y1, y2):
    return sqrt(((x1-x2)**2)+((y1-y2)**2))

x_1 = eval(input("Enter x1: "))
x_2 = eval(input("Enter x2: "))
y_1 = eval(input("Enter y1: "))
y_2 = eval(input("Enter y2: "))
print(f"The distance between ({x_1},{y_1}) and ({x_2},{y_2}) is {disbtwpoints(x_1, x_2, y_1, y_2)}")