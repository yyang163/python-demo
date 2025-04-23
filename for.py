# 打印倒直角三角形
for i in range(1,7):
    for j in range(1,8-i):
        print("*",end="")
    print()

# 打印直角三角形
for x in range(1,8):
    for y in range(1,x+1) :
        print("*",end="")

    print()
# 打印等边三角形

for i in range(1,7):
    for j in range(1,8-i):
        print(" ", end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()


# 、有一些四位数,百位数字都是3,十位数字都是6,并且它们既能被2整除,又能被3整除,求这样的四位数中最大的和最小的两数各是几?

def find_numbers():
    valid_numbers = []
    for a in range(1, 10):  # 千位数：1-9
        for b in range(0, 10, 2):  # 个位数：（因为能被2整除 所以是2的倍数）0, 2, 4, 6, 8
            num = a * 1000 + 3 * 100 + 6 * 10 + b
            if (a + 3 + 6 + b) % 3 == 0:  # 能被3整除
                valid_numbers.append(num)
    return valid_numbers


numbers = find_numbers()
max_num = max(numbers)
min_num = min(numbers)

print("满足条件的四位数：", numbers)
print("最大的数：", max_num)
print("最小的数：", min_num)


