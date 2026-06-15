class BankAccount:
    """Банковский счёт с базовыми операциями."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Пополняет счёт."""
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        """Снимает деньги, если хватает средств."""
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")

    def show_balance(self):
        """Показывает текущий баланс."""
        print(f"{self.owner}'s balance: {self.balance}")


if __name__ == "__main__":
    account = BankAccount("Dauren", 100)
    account.show_balance()
    account.deposit(50)
    account.withdraw(30)
    account.withdraw(1000)

    account.owner = "Dauren T."
    account.show_balance()

    del account.balance
    print("Has 'balance' attribute:", hasattr(account, "balance"))

    del account
    print("Account deleted.")
