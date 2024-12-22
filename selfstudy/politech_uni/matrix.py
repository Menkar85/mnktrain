import numpy as np
import numpy.linalg as alg

a = np.array([[3, 4, -2], [-2, -1, 4]])
b = np.array([[1, -3, -2, 1], [2, 4, -2, -1], [5, -2, 0, -2]])
c = np.array([[-1, 0, 2], [2, -2, 3], [0, 5, 1]])

print(np.dot(c, b))