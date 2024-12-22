# def y(x):
#     y = pow(x, 2) + 3
#     return y

# sum = 0

# for i in range(10, 31, 2):
#     sum = sum + y(i)

# print(sum)

y_list = [x ** 2 + 3 for x in range(10, 31, 2)]
print(sum(y_list))