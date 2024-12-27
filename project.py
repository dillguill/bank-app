class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction("Deposit", amount)
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._log_transaction("Withdrawal", amount)
            return True
        return False

    def _log_transaction(self, transaction_type, amount):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_type}: ${amount} | Balance: ${self.balance}\n")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"

if __name__ == "__main__":
    account = BankAccount("Dillon")

    while True:
        action = input("Enter 'd' to deposit, 'w' to withdraw, or 'q' to quit: ").lower()
        if action == 'q':
            break
        elif action in ('d', 'w'):
            amount = float(input("Enter amount: "))
            if action == 'd':
                if account.deposit(amount):
                    print(f"Deposited ${amount}. New balance: ${account.balance}")
                else:
                    print("Invalid deposit amount.")
            elif action == 'w':
                if account.withdraw(amount):
                    print(f"Withdrew ${amount}. New balance: ${account.balance}")
                else:
                    print("Invalid withdrawal amount or insufficient funds.")
        else:
            print("Invalid action. Please enter 'd', 'w', or 'q'.")