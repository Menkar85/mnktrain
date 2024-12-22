# Перепишите следующий код с использованием спискового включения:

# >>> res = []
# >>> for x in range(5):
#         if x%2 == 0:
#             for y in range(5):
#               if y%2 == 1:
#                   res.append((x, y))
# >>> res
# [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
import itertools


res = [(x, y) for x, y in itertools.product(range(5), range(5)) 
       if (x%2 == 0 and y%2 == 1)]
print(res)
