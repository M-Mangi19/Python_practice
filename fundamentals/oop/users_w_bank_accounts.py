class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.amount = amount
        return self

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.amount = amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.int_rate = self.balance * self.int_rate
        self.balance = self.int_rate + self.balance
        return self

    @classmethod
    def account_info(cls):
        for BankAccount in cls.all_accounts:
            print(f"${BankAccount.balance}, ${BankAccount.int_rate}")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    # other methods

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self



user1 = User("Matt", "matt@email.com")

user1.make_deposit(100)
user1.make_withdrawal(50)
user1.display_user_balance()
