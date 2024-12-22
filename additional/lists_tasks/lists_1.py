L = [3, 6, 7, 4, -5, 4, 3, -1]

elem_sum = sum(L)

if elem_sum > 2:
    print(len(L))

abs_diff = abs(sorted(L)[0] - sorted(L)[-1])

if abs_diff > 10:
    print(sorted(L, reverse=True))
else:
    print("Difference is less than 10")