class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.__pin = 1234

    def deposit(self, amount):
        self._balance += amount
        print(f"Succesfully added {amount} to balance!")
    
    def get_balance(self):
        return self._balance
    
acc1 = BankAccount("Daris",1000)
acc1.deposit(300)
print(acc1._BankAccount__pin)

        