from collections import Counter
from math import sqrt
# Solution to Exercise

# Question One
class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, number):
        self.memory += number
        return self.memory

    def subtraction(self, number):
        pass

    def multiply(self, number):
        pass

    def division(self, number):
        pass
    
    def squareroot(self):
        self.memory = sqrt(self.memory)
        return self.memory

    def reset(self):
        self.memory = 0

calc = Calculator()
print(calc.add(10))
print(calc.add(5.63))
print(calc.squareroot())
calc.reset() # memory = 0
print(calc.add(2))

# Question 2
s1 = "Hellok"
s2 = "vufigsaHudesdflelio"

#soln
def string_creation(s1, s2):
    counter = 0
    for ch in s1.lower():
        if ch in s2.lower():
            counter += 1 # counter = counter + 1

    if counter == len(s1):
        return True
    else:
        return False

string_creation(s1, s2)



# Question 3
nums = [1, 2,3,4,5,4,2,-9999, 8.9, 7,9,10]

def sum_num_list(nums:list):
    sum = 0
    for x in nums:
        if x != -9999:
            sum += x # sum = sum + x
        else:
            break
    return sum

print(sum_num_list(nums))
        
def sum_num_args(*args):
    sum = 0
    for x in args:
        if x != -9999:
            sum += x # sum = sum + x
        else:
            break
    return sum
print(sum_num_args(2,3,4,6,7, 9.08,-9999, 13, 34))