class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount is: {amount}. \nNew balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

bankAccount = BankAccount("Chard", 1000)
bankAccount.deposit(500)


        
        