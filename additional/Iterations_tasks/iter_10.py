# Создайте матрицу со случайными данными и замените в ней все
# положительные значения на 2, а все отрицательные — на –2.
import numpy as np

# 2 итерации, чтобы соханить 0. Можно обойтись одной итерацией
# если 0 не критичен, он и так выпадает очень редко.
arr_rand = np.round(np.random.randn(5, 5), 3)
arr_rand = np.where(arr_rand < 0, -2, arr_rand)
new_arr = np.where(arr_rand > 0, 2, arr_rand)

print(new_arr)
