from Account import Account


class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True

    def create_account(self, name):
        account = Account(name)
        self.accounts.append(account)

    def get_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature = True

    def disable_loan_feature(self):
        self.loan_feature = False
