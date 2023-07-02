from datetime import datetime
# decorator for functions that runs between specific hours of the day

def run_between_hours(from_=8, to_=17): # function that returns decorator
    def between_hrs(func): # decorator name
        def wrapper(): # wrapper
            if from_ <= datetime.now().hour < to_:
                func()
        return wrapper
    return between_hrs


@run_between_hours(5,12)
def print_something():
    print("I am here")

# Repetition - call a function multiple times
def repeat(num_of_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_of_times):
                repeat = func(*args, **kwargs)
            return repeat
        return wrapper
    return decorator_repeat


@repeat(4)
def say_hello(name):
    print(f"hello {name}")

say_hello("Dolapo")


