class BancAccount:
    def __init__(self,balance,owner):
        self.__balance = balance
        self.__owner = owner
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount > self.__balance: return 'error 01'
        else: self.__balance -= amount
    @property
    def balance(self):
        return self.__balance
    def __str__(self):
        return f'owner: {self.__owner},balance: {self.__balance}'
class SavingAccount(BancAccount):
    def __init__(self,balance,owner,interest):
        super().__init__(balance,owner)
        self.interest = interest
