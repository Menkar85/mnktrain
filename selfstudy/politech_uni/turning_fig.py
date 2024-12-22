import numpy as np
import numpy.linalg as alg
from math import cos, sin, radians


n = int(input("n = "))
coordinates = []

for i in range(n):
    point_str = input('Enter point coordinates: ').split()
    point_int = [float(point_str[l]) for l in range(2)]
    coordinates.append(point_int)

coord_array = np.array(coordinates)

angle = radians(float(input("Enter turn angle in deg: ")))

rotate = np.array([[cos(angle), sin(angle)], [-sin(angle), cos(angle)]])

final_coords = np.dot(coord_array, rotate)
print(np.round(final_coords,3))
