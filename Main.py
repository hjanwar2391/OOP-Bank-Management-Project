from Bank import Bank
from Account import Account

# creat user
account = Account
# Create a Bank
bank = Bank()

# Create user accounts
bank.create_account("KalaCan", "kalacan@gmail.com")
bank.create_account("DolaCan", "dolacan@gamil.com")

# Deposit and withdraw amounts
KalaCan_account = bank.get_account("KalaCan")
KalaCan_account.deposit(5500)
KalaCan_account.withdraw(500)

# Check available balance
print(KalaCan_account.get_balance())

# Transfer amount to another user account
DolaCan_account = bank.get_account("DolaCan")
KalaCan_account.transfer(DolaCan_account, 100)

# Check transaction history
print(KalaCan_account.get_transaction_history())
print(DolaCan_account.get_transaction_history())

# Check total balance and total loan amount
print(bank.get_total_balance())
print(bank.get_total_loan_amount())

# Enable loan feature
bank.enable_loan_feature()

# Take a loan from the bank
KalaCan_account.deposit(1000)
loan_amount = KalaCan_account.get_balance() * 2
bank.total_loan_amount += loan_amount
KalaCan_account.withdraw(loan_amount)

# Check total loan amount
print(bank.get_total_loan_amount())
