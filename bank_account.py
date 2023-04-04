#Bank Account
class Bank_Account():
  # NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    all_instances =  []


    def __init__(self,int_rate, balance = 0): #balance will default to zero if no amount is given
      self.int_rate = int_rate
      self.balance = balance
      Bank_Account.all_instances.append(self)
    
    def deposit(self, amount):
      self.balance += amount
      return self
    
    def withdraw(self, amount):
      if (self.balance - amount) > 0:
        self.balance -= amount
      else: 
        print(f'Sorry, but you do not have enough funds to withdraw money. Your balance: {self.balance}')
      return self
    
    def display_account_info(self):
      print(f"You have a balance of: ${self.balance}")
      print(f"You have a balance of: ${self.int_rate * 100}%")
      return self
    
    def yield_interest(self):
      if self.balance > 0:
        self.balance += (self.balance * self.int_rate)
      else: 
        print('Your account balance is negative')
      return self


    @classmethod
    def print_instances(cls):
      for i in cls.all_instances:
        print(i.display_account_info())


david = Bank_Account(.5, 10000)
tyler = Bank_Account(0.5, 20000)

Bank_Account.print_instances()


david.deposit(100).deposit(1000).deposit(100).withdraw(200).yield_interest().display_account_info()
tyler.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(20).withdraw(20).yield_interest().display_account_info()
  