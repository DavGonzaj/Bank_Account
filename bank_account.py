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
  
  
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [Bank_Account(int_rate=0.02, balance=0)]  # added this line

    @classmethod
    def account(self):
        return self.accounts[0]

    def make_deposit(self, amount):
        if len(self.accounts) == 1:
            self.account.deposit(amount)
        else:
            for account in self.accounts:
                print("{:<30}${:>30}".format(account.name, account.balance))
            index = False
            while index is False:
                selector = input("Please type the name of the account you'd like to deposit to:\n")
                try:
                    index = [account.name for account in self.accounts].index(selector)
                except ValueError:
                    print("try again")

            return self.accounts[index].deposit(amount)

    def make_withdrawal(self, amount):
        self.accounts[0].withdraw(amount)


samuel = User(name='Samuel L Jackson', email="lebromt@yuh.com")
samuel.make_deposit(55)
samuel.accounts.append(Bank_Account(int_rate=7.8, balance=77, name="Hector"))
samuel.make_deposit(33)
