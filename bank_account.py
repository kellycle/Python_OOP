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

kelly = BankAccount(.05,100)
binx = BankAccount(.03,400)

kelly.deposit(100).deposit(40).deposit(60).withdraw(30).yield_interest().display_account_info()
binx.deposit(60).deposit(200).withdraw(20).withdraw(30).withdraw(70).withdraw(80).yield_interest().display_account_info()