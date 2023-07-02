from datetime import datetime
#python runs from top to bottom
# wont run a function until you call it
def simple_decorator(function): #function is the method that the decorator is executing
    def wrapper():
        print("Before function executes")
        function()
        print("after function executes")
    return wrapper

@simple_decorator #decorator
def print_something():
    print("My first decorator, Hurray!!!")

#print_something()

#log the timestamp a function runs

def log_time(func):
    """
         A wrapper to log execution time of a function
    """
    def wrapper():
        print(f'Job {func.__name__} started at {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        func()
        print("Job completed")
    return wrapper

@log_time
def instant_job():
    print("Task of the day")

@log_time
def daily_backup():
    print("Backup successful")


# decorator for validation
def validating_non_negative_numbers(func):
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args):
            raise ValueError("All parameters must be greater than 0")
        return func(*args, **kwargs)
    return wrapper

@validating_non_negative_numbers
def sum_2(a, b):
    return a + be

@validating_non_negative_numbers
def sum_all(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_all(5, 10, 10,23))# will run

print(sum_all(5, 10, -7,23)) # will return error
