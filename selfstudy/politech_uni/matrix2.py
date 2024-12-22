import numpy as np
import numpy.linalg as alg

a = np.array([[1, 1, 1], [1 / 3, -1, 0], [0, 1 / 3, -1]])
b = np.array([2970, -180, -130])

a_inv = alg.inv(a)
x = np.round(np.dot(a_inv, b), 2)
print("First worker got: ", x[0],"rub")
print("Second worker got: ", x[1],"rub")
print("Third worker got: ", x[2],"rub")