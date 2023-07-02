def decorator1(func):
    def wrapper():
        print("Decorator 1 before function")
        func()
        print("Decorator 1 after function")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 before function")
        func()
        print("Decorator 2 after function")
    return wrapper

@decorator1
@decorator2
def hello():
    print ("hello")

"""
    *****************
    Try again
    ****************
"""

def print_star(func):
    def wrapper(*args, **kwargs):
        print("*" * 10) # before action
        func(*args, **kwargs)
        print("*" * 10) # after action
    return wrapper

def print_Hash(func):
    def wrapper(*args, **kwargs):
        print("#" * 10) # before action
        func(*args, **kwargs)
        print("#" * 10) # after action
    return wrapper

@print_Hash
@print_star
def print_something(message, name):
    print(f"{name}: {message}")

"""
print_Hash(print_star(print_something()))

= print hash accepts print_star(print_something())
###########
run function then runs function print star: which accepts print_something
*************
yipeee
************
##########

"""
print_something("Yipeee", "andy")
