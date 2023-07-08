import math
from functools import reduce
# adding 15 to a number passed in an argument

def add_15(x):
    return x+15

print(add_15(20))

'''
Here:
    a+15 is the expression
    a is the argument
'''
sum_15 = lambda a: a+15 
print(sum_15(10))


# Get products/multiplication of numbers
products = lambda x,y,z : x * y * z
print(products(3,5,4))

# lambda functions inside normal/other functions

def multiply_result(n):
    return lambda a: a * n

tripler = multiply_result(3)
print(tripler(10))


# get the even numbers in a list
# 5 % 3 = 2 

def get_even(nums):
    even = []
    for item in nums:
        if int(item) % 2 == 0:
            even.append(item)
    return even

my_list = [2,3,5,6,7,8]
print(get_even(my_list))

even = list(filter(lambda x: x % 2 == 0, my_list))
print(even)

# string actions
def yell(x):
    return x.upper()


yell_l = lambda x: x.upper()


# Square the content of a list
list_c = [3,5,6,7,8,9,2]
squared = list(map(lambda x: x**2, list_c)) # calling map to squeare each item of the list
#, and converting/casting the map object to a list
print(squared)

# Determine whether a number is odd/even. if even, return true
'''
map syntax

map(lambda/function, iterable/list/set/tuple etc) => map object that needs to be converted to a list
'''
even_odd = map(lambda x: x % 2 == 0, list_c)
print(list(even_odd))

# Example: get the length of each string in a list

words = ["thankful", "bonne nuit", "devant", "pres du"]
word_list = list(map(lambda x: len(x), words))
print(word_list)


def word_length(word):
    return len(word)

word_list_b = list(map(word_length, words))
print(word_list_b)


## FILTERS

numbers = [12,23,4,2,2,3,21,45,32]
greater_than_20 = list(filter(lambda x: x > 20, numbers))
print(greater_than_20)

# return prime numbers
'''
Prime number is a number divisible by 1 and itself onnly
2, 3, 5, 7, 11, 13, 17, 23 .....

11 sqrt = 3
2  4
'''
def valid_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

prime = list(filter(valid_prime_number, range(1, 100)))
print(prime)

# Palindrome
'''
A palindrome word is one which the words are the same when you read it 
forward (left to right) and backword (right to left)
e.g Hannah, madam, tunde ednut, racecar, aha
'''

def check_if_palindrome(x):
    reverse = "".join(reversed(x))
    return x.lower() == reverse.lower()


words_p = ['gunter', 'Aha', 'Friday', 'Tunde Ednut', 'Threads', 'Twitter', 'Madam']
print(list(filter(check_if_palindrome, words_p)))

# reduce

numbers = [1,2,4,5,6]
data = reduce(lambda x, y: x + y, numbers)
print(data)

# get maximum number in a list

num_list = [122,32,4334,545,656,3214]
'''
a if (a > b) else b
return a if a > b
return b if a < b

'''
max_num = reduce(lambda a, b: a if (a > b) else b, num_list )
print(max_num)

def product(x, y):
    return x * y

rst = reduce(product, [3,4,5,6,7])
print(rst)


# filter then reduce
# Extract the even numbers in a list, then sum all even numbers
# 

def sum_even(nums):
    '''
    explain what it does
    '''
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
    return sum

list_sum = [12,4,21,5,7,8,21,9]
print(sum_even(list_sum))

even_numbers = list(filter(lambda x: x % 2 == 0, list_sum))
sum_even_n = reduce(lambda a, b: a + b, even_numbers)
print(sum_even_n)

combined_ = reduce(lambda a, b: a + b, filter(lambda x: x % 2 == 0, list_sum))
print(combined_)

# Get the total cost in a dictionary
grocery = [
    {'item':'bread', 'cost': 12.89},
    {'item':'pommes', 'cost': 5 },
    {'item':'chewing gum', 'cost': 1.5 },
    {'item':'kiwi', 'cost': 8.99 }]

'''
 x = accumulated value
 y = current dictionary value
 third parameter is the initializer which servers as a default value 
    if the second parameter y is an empty sequence. 

    => if the second argument is an empty sequence, 
        the third argument (initializer) serves as the default
'''
total_cost = reduce(lambda x,y: x + y['cost'], grocery, 0)
print(total_cost)

