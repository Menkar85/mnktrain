import numpy as np

a = np.array([100, 200, 300], dtype=int)
b = np.where(a > 100)[0]
print(b)