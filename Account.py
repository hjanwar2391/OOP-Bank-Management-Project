class Account:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Bank is bankrupt"
        self.balance -= amount
        self.transaction_history.append(f"Withdrawn: {amount}")

    def transfer(self, recipient, amount):
        if amount > self.balance:
            return "Bank is bankrupt"
        self.balance -= amount
        recipient.balance += amount
        self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
        recipient.transaction_history.append(f"Received: {amount} from {self.name}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history
