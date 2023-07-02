import functools
# Class-based decorator
"""
We are using a function called wraps, update_wrapper in functools because it ensures that the decorator 
mimics the calling function. i.e it has the same name __name__, docs __doc__ as the wrapper 

"""
# example: count how many times an action/function is called
class CountNumberOfCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0 
    
    def __call__(self, *args, **kwargs): # magic/special method that allows the class instances to be called as a function
        self.calls += 1
        print (f"Call {self.calls} - {self.func.__name__}")
        return self.func(*args, **kwargs)


class LimitNumberOfCalls:
    def __init__(self, max_calls):
        self.max_calls = max_calls
        self.num_of_times = 0
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.num_of_times >= self.max_calls:
                raise Exception (f"{func.__name__} has reached its maximum call")
            self.num_of_times += 1
            return func(*args, **kwargs)
        return wrapper


def limit_calls(max_calls):
    num_calls = {'count': 0}
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if num_calls['count'] >= max_calls:
                raise Exception (f"{func.__name__} has reached its maximum call")
            num_calls['count'] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator


@limit_calls(2)
def say_hello(name):
    print(f"hello {name}")

say_hello("Tammy")
say_hello("fred")
say_hello("Justin")


