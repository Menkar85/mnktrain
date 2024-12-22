n = 9
for i in range(0, n):
    for j in range(0, n):
        if (i == 0 or i == n-1 or j == i or j == n-i-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = 5
num = 0
for i in range(n):
    for j in range(n):
        if (i+j) % 2 != 0:
            print(num+1, end="  ")
            num += 1
        else:
            print("*", end="  ")
    print()
