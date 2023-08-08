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

account1 = BankAccount(0.01, 0)
account2 = BankAccount(0.01, 0)

account1.deposit(100.00).deposit(100.00).deposit(100.00).withdraw(50.00).yield_interest().display_account_info()
account2.deposit(200.00).deposit(500.00).withdraw(82.00).withdraw(42.00).withdraw(76.00).withdraw(200.00).yield_interest().display_account_info()

BankAccount.account_info()



# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)