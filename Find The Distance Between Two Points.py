from math import sqrt

def distance(x1, y1, x2, y2):
    # Your code here
    return float('{:.2f}'.format(sqrt((x2 - x1)**2 + (y2 - y1)**2)))

print(distance(1, 1, 0, 0))