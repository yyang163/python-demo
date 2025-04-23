# 银行账户模拟
# 编写一个BankAccount类，要求：
#  使用循环处理多次存取款操作
# 使用断言确保余额不会为负
# 使用异常处理无效的金额输入
# 实现存款、取款和查询余额方法


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance  = amount+self.balance
            print(f"存款为{amount},余额为{self.balance}")
        else:
            print("存款金额需正整数")
    def withdraw(self,amount):
        if amount > 0 and amount<= self.balance:
            self.balance=self.balance-amount
            print(f"取款金额为{amount},余额为{self.balance}")
        else:
            print(f"账户余额不足以支付交易所需的费用，或者提款金额无效")
    def display_balance(self):
        print(f"账户名为{self.owner} 余额为{self.balance}")
if __name__ == '__main__':
    account=BankAccount("张三",500)
    account.display_balance()
    account.deposit(30)
    account.display_balance()
    account.withdraw(2200)
    account.display_balance()



