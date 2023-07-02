
def my_function():
    print("Hello I am a function")

val = my_function
val()

def shout(text):
    return text.upper()

def silent(text):
    return text.lower()

# passing function shout to a variable yell
yell = shout

print(yell("We are learning decorators"))


def greeting(func):
    greet_ = func("I am hailing you!!!")
    print(greet_)


greeting(shout)

def sum(a , b):
    return a+b

def do_somthing(func):
    print(f"The sum function returned: {func(10, 23)}")

do_somthing(sum)


def outer_func(): # main function
    def inner_func(): # inner function within my outer function
        print("This is the inner function calling")
    print("The content of the outer function")
    inner_func() # calling my inner function

outer_func()

def outer_function():
    book = "A year of yes by Shonda Rhimes"
    def inner():
        print(f"From inner: {book}")
    return inner() # returning the inner function

outer_function() # call the function

def double(x):
    double = x * 2
    def add_y(y):
        print(double + y)
    return add_y

#passing 20 into function double. double returns function add_y
for_20 = double(20)
for_20(10)



