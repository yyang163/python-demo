# 编写函数test(password, earning, age)用于检测输入错误。要求输入密码password第一个符号不能是数字，工资earnings的范围是0—20000，工作年龄的范围是18—70。若三项检查都通过则返回True。
#方法一：

# def test(password, earning, age):
#
#     assert password[0] not in[0,1,2,3,4,5,6,7,8,9]
#     assert earning >= 0 and earning <= 20000
#     assert age >= 18 and age <=70
#     return True
# password = input("请输入密码")
# earning = int(input("请输入工资"))
# age = int(input("请输入年龄"))
#     # print(password)
#     # print(earning)
#     # print(age)
#
# print(test(password, earning, age))

#方法二：
# def test(password,earning,age):
#     try:
#         assert not password[0].isdigit()
#         assert 0<=earning<=2000
#         assert  18<=age<=70
#         return True
#     except (AssertionError, TypeError, IndexError) as e:
#         print(f"验证失败: {e}")
#         return False
# print(test("1we",22,17))


# 验证年龄是否在合理范围内(0-120岁)

# def validate_age(age):
#     try:
#         assert isinstance(age,int)
#         if age <0:
#             raise ValueError("年龄不能为负数")
#         if age > 120:
#             raise ValueError("年龄输入不合理")
#         return True
#     except ValueError as e:
#         print(f"验证失败:{e}")
#         return False
#     except AssertionError as e:
#         print(f"断言失败:{e}")
#         return False
# assert validate_age(25) is True
# assert validate_age(-5) is False
# assert validate_age(150) is False
# assert validate_age("25") is False
# print(validate_age("aa"))

#实现一个安全的除法函数，当除数为0时返回None并打印警告

# def safe_divide(a, b):
#
#     try:
#         assert isinstance(a, (int, float)), "被除数必须是数字"
#         assert isinstance(b, (int, float)), "除数必须是数字"
#         return a / b
#     except ZeroDivisionError:
#         print("警告: 除数不能为零")
#         return None
#     except AssertionError as e:
#         print(f"断言错误: {e}")
#         return None
#     except TypeError:
#         print("错误: 输入必须是数字")
#         return None
#
#
# assert safe_divide(10, 2) == 5
# assert safe_divide(10, 0) is None
# assert safe_divide("10", 2) is None







