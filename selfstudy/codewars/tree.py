def review(height, ornaments, tree):
    height = height + 1
    width = (height - 2)*2 + 1
    mid = int(width / 2)
    for i in range(height):
        for j in range(width):
            if i < height-1 and mid-1*i <= j <= mid+1*i and ornaments == "no":
                print("*", end="")
            elif i < height-1 and mid-1*i <= j <= mid+1*i and ornaments == "yes" \
                    and i != 1 and (j != mid - 1 or j != mid + 1):
                print("*", end="")
            elif i == 1 and (j == mid - 1 or j == mid + 1) and ornaments == "yes":
                print("o", end="")
            elif i == 1 and (j == mid) and ornaments == "yes":
                print("*", end="")
            elif i == height-1 and j == mid:
                print("|", end="")
            else:
                print(" ", end="")
        print()


review(5, 'yes', 'tree')
