# Задан список lst = [4, '5', '6', 8]. Используя метод join,
# необходимо несколькими способами получить строку вида '4568'.

lst = [4, '5', '6', 8]
lst_str = [str(i) for i in lst]

final_1 = ''.join(lst_str)
print(final_1)

final_lst = []
for i in lst:
    final_lst.append(str(i))
final2 = ''.join(final_lst)

print(final2)
