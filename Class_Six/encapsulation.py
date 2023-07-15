"""
ENCAPSULATION
- It describes the idea of wrapping data and underlining methods within one unit
- it basically means data hidding


Access Modifiers:
    public - everyone
    private - within the class only
    protected - within the class and through inheritance

encapsulation is possible in python with name mangling. 
if class attribute is prefixed with double underscore __, python will mangle the obj name to prevent 
    direct access from outside the class

You can modify the private variables through getter and setter
"""

class SimpleClass:
    def __init__(self) -> None:
        self.num1 = 10 # public
        self.__num2 = 20 # private. Accessible only within the class

    def sum(self):
        return self.num1 + self.__num2
    
    def get_num2(self):
        return self.__num2
    
    def set_num2(self, value):
        self.__num2 = value
    

obj = SimpleClass()
obj.num1 = 40
obj.set_num2(30)
# print(f"sum: {obj.sum()}")
# print(f"num 1: {obj.num1}")
# print(f"num 2: {obj.get_num2()}") 


class BankAccount:
    def __init__(self, initial_balance = 0) -> None:
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            print(f"Amount must be greater than 0")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            print(f"Invalid transaction")

    def get_balance(self):
        return self.__balance
    
    def __interest(self, amount):
        self.__balance += amount

account = BankAccount(200)
account.deposit(30) #230
account.withdraw(40) #190
print(account.get_balance())

# print(account.__interest(10000))
# print(account.get_balance())
    

