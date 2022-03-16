class User:
    def __init__(self,name,balance):
        self.name = name
        self.account_balance = balance 
    # adding the deposit method
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    # adding withdrawal method
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    # adding display method
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    # adding transfer method
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

kelly = User("Kelly",0)
billie = User("Billie",0)
binx = User("Binx",0)

print(kelly.name)
print(billie.name)
print(binx.name)

kelly.make_deposit(100).make_deposit(40).make_deposit(60).make_withdrawal(30).display_user_balance()

billie.make_deposit(300).make_deposit(20).make_withdrawal(50).make_withdrawal(70).display_user_balance()

binx.make_deposit(60).make_withdrawal(20).make_withdrawal(20).make_withdrawal(30).display_user_balance()

kelly.transfer_money(binx,10).display_user_balance()
binx.display_user_balance()