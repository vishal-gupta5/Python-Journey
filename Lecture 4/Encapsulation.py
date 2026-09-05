# Encapsulation

class BankAccount:
    def __init__(self, name, balance):
        self.name = name #Public
        self.__balance = balance #Private -> Data Mangling

    def get_balance(self): #Getter
        return self.__balance

    def set_balance(self, newBalance): #Setter
        self.__balance = newBalance

        
acc1 = BankAccount("Vishal Gupta", 100000)

acc1.set_balance(200_000)

print(acc1.name, acc1.get_balance())
print(acc1.name, acc1._BankAccount__balance)
        