import secrets
from secrets import choice


while True:
    a=int(input("请输入第一个数:"))
    b=int(input("请输入另一个数:"))
    c = str(input("请输入+ - * / %  // ** 中任意一个运算符:"))

    if c=="+":
        print("计算两个数的和为：%s"%(a+b))
    elif c=="-":
        print(f"计算两个数的差为:{a-b}")
    elif c == "*":
        print(f"计算两个数的积为:{a * b}")

#修改后 判断变量a/b为整数
while True:
    try:
        a = int(input("请输入第一个数:"))
        b = int(input("请输入另一个数:"))
        c = str(input("请输入+ - * / %  // ** 中任意一个运算符:"))

        if c=="+":
            print("计算两个数的和为：%s"%(a+b))
        elif c=="-":
            print(f"计算两个数的差为:{a-b}")
        elif c == "*":
            print(f"计算两个数的积为:{a * b}")
    except ValueError:
        print("输入的变量类型为非整数 请重新输入")
        continue



