# Methods

# Instance Method

class DoSomething:
    default_name = "Zuriel"
    
    def __init__(self, name:str):
        self.name = name

    """
        This is an instance method. first parameter is self
    """
    def say_hello(self):
        return f"Hi {self.name}, enchante"

    @classmethod
    def class_example(cls):
        print("This is a class method")

# val = DoSomething("Dolapo")
# print(val.say_hello())
# print(val.default_name)

# val2 = DoSomething("Fred")
# print(val2.say_hello())

# DoSomething.class_example()
# print(DoSomething.default_name)


class Weight:
    def __init__(self, kilos, height):
        self.kilos = kilos
        self.height = height

    def bmi(self):
        return self.kilos / (self.height * self.height)

    @classmethod
    def convert_to_pounds(cls, kilos):
        return kilos * 2.205

    @classmethod
    def convert_to_kilos(cls, pounds):
        return pounds / 2.205

d_weight = Weight(70, 1.5)
print(d_weight.bmi())

k_weight = Weight(55, 1.7)
print(k_weight.bmi())

print(Weight.convert_to_pounds(70))

