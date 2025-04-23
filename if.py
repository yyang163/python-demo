# 从键盘输入三角形的 三个边长 判断能否构成三角形，如果能 输出能构成三角形 再输出是什么三角形 等边 等腰 直角 普通 如果不能 输出不能构成三角形
while True:
    a = int(input("请输入三角形的变长:"))
    b = int(input("请输入三角形的变长:"))
    c = int(input("请输入三角形的变长:"))
    if a + b > c and b + c > a and a + c > b:
        print("可以构成三角形")
        if a == b == c:
            print("等边三角形")
        elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            print("直角三角形")
        elif a == b != c or a == c != b or b == c != a:
            print("等腰三角形")
        else:
            print("普通三角形")
    else:
        print("不可以构成三角形")
        continue
