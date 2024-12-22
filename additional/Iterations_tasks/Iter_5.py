# Напишите программу, которая проверяет, являются ли все элементы списка
# палиндромами. Например, для списка ['aaccwccaa', 'aoa', 32323]
# результатом будет ответ True.

lst = ['aaccwccaa', 'aoa', 32323]

poly_lst = []

for item in lst:
    word = str(item)
    revd = list(reversed(word))
    poly_lst.append(word.endswith(''.join(revd)))

print(all(poly_lst))
