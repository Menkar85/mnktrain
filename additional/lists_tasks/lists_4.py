L = [3, 'hello', 7, 4, 'privet', 4, 3, -1]

if 'privet' in L:
    L.remove('privet')
else:
    L.append('privet')

print(L)

n = L.count(4)
if n > 1:
    L.clear()

print(n)
print(L)
