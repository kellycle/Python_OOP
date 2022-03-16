class User:
    def __init__(self,name):
        self.name = name
        self.account = BankAccount(int_rate=0.02,balance=0) 
    # adding the deposit method
    # def make_deposit(self,amount):
    #     self.account.deposit(amount)
    #     return self
    # # adding withdrawal method
    # def make_withdrawal(self,amount):
    #     self.account.withdraw(amount)
    #     return self
    # # adding display method
    # def display_user_balance(self):
    #     print(f"User: {self.name}, Balance: ${self.account.balance}")
    # # adding transfer method
    # def transfer_money(self,other_user,amount):
    #     self.account.balance -= amount
    #     other_user.account_balance += amount
    #     return self
        
class BankAccount:
    def __init__(self,int_rate=.01,balance=0):
        self.int_rate = int_rate
        self.balance = balance
    # adding deposit method 
    def deposit(self,amount):
        self.balance += amount
        return self
    # adding withdraw method
    def withdraw(self,amount):
        if (self.balance - amount) < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    # adding display method
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
    # adding interest
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


kelly = User("Kelly")

kelly.account.deposit(100).deposit(40).display_account_info()
