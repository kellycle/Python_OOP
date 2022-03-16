class User:
    def __init__(self,name,balance):
        self.name = name
        self.account_balance = balance 
    # adding the deposit method
    def make_deposit(self,amount):
        self.account_balance += amount
    # adding withdrawal method
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    # adding display method
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    # adding transfer method
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

kelly = User("Kelly", 0)
billie = User("Billie", 0)
binx = User("Binx", 0)

print(kelly.name)
print(billie.name)
print(binx.name)

kelly.make_deposit(100)
kelly.make_deposit(40)
kelly.make_deposit(60)
kelly.make_withdrawal(30)
kelly.display_user_balance()

billie.make_deposit(300)
billie.make_deposit(20)
billie.make_withdrawal(50)
billie.make_withdrawal(70)
billie.display_user_balance()

binx.make_deposit(60)
binx.make_withdrawal(20)
binx.make_withdrawal(20)
binx.make_withdrawal(30)
binx.display_user_balance()

kelly.transfer_money(binx,10)
kelly.display_user_balance()
binx.display_user_balance()