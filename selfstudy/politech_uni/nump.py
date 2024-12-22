"""Programm for calculating average speed, time and distance
from parameters from the parts of the way.
k and p is begining and end of the parts.
"""

import numpy as np


in_s = input("Enter length: ").split()
in_v = input("Enter speeds: ").split()
k = int(input("k = "))
p = int(input("p = "))


length = np.array(in_s, dtype=int)
speed = np.array(in_v, dtype=int)
time = length / speed

i_0 = k 
i_1 = p + 1

s = np.sum(length[i_0:i_1])
t = np.sum(time[i_0:i_1])
avg_speed = s / t

print("S = ", round(s, 2), "km; T = ", round(t, 2), "hrs; V = ",
      round(avg_speed, 2), "km/h")
