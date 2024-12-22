def func(list):
    return list[1]

lst_raw = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
# lst_raw.sort(key=lambda x: x[1])
# print(lst_raw)

lst_raw.sort(key=func)
print(lst_raw)
