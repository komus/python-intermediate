#from lambdaex import valid_prime_number
# with open('readme.txt') as f:
#     for line in f:
#         print(line)


cities = ["Vancoucer", "Vilnius", "Klaipeda", "Halifax"]
cities_iter = iter(cities)
print(f"first {next(cities_iter)}")
print(f"second {next(cities_iter)}")
print(f"third {next(cities_iter)}")
print(f"fourth {next(cities_iter)}")
#print(f"doesnt exist {next(cities_iter)}")

'''
creating an iterable: 
- __init__
- __iter__
- __next__
'''
class MyIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end: # start = 10, end = 15
            raise StopIteration
        
        current = self.start # = 10
        self.start += 1 # = 11
        return current #= 10
    
for i in MyIterable(10, 15):
    print(i)

# hello 
# return h, e,l,l,o,h,e,l,l,o
class CycleIterable:
    def __init__(self, val) -> None:
        self.val = iter(val)
        self.iterable = val

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
                next_obj = next(self.val)
                return next_obj
            except StopIteration:
                self.val = iter(self.iterable)


c = CycleIterable("Hello")

# for i in range(15):
#     print(next(c))

# get primenumbers in a range
import math
def valid_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def get_n_prime_numbers(n):
    prime = []
    for counter in range(2, n):
        if valid_prime_number(counter):
            prime.append(counter)
    return prime

values = get_n_prime_numbers(25) # assume you want to run for 5000000000
print(values)

class PrimeIterator:
    def __init__(self, n) -> None:
        self.n = n
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.num += 1
        if self.num >= self.n:
            raise StopIteration
        
        elif valid_prime_number(self.num):
            return self.num
        
        #default else, not a prime number
        return self.__next__()
    
val = PrimeIterator(25)
for v in val:
    print(v)


def prime_generator(n):
    for i in range(n):
        if valid_prime_number(i):
            yield i

gen = prime_generator(25)
# for ele in gen:
#     print(ele, ", ")


"""
Fibonacci Series
0 1 1 2 3 5 8 13
"""

def fibonacci(n):
    a,b = 0, 1
    counter = 0
    while True:
        if (counter >= n):
            return
        yield a
        a,b = b, b+a # === a = b b = a+b
        counter += 1

fib = fibonacci(20)
for x in fib:
    print(x)

def fibonacci_con(n):
    a,b = 0, 1
    for _ in range(n):
        a,b = b, b+a
        yield a

def square(n):
    for num in n:
        yield num ** 2

chained = square(fibonacci_con(10))
for c in chained:
    print(c)
