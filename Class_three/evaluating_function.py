import functools
import tracemalloc
from time import perf_counter
# performance measure
# - computes the memory consumed by a function
# - speed of the function

# Balance tradeoff between memory and speed

def performance_measure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        end_time = perf_counter()

        print(f"Function: {func.__name__}")
        print(f"Docs: {func.__doc__}")
        print(f"Memory Usage: \t\t {current / 10**6:.7f} MB")
        print(f"Peak Memory Usage: \t\t {peak / 10**6:.7f} MB")
        print(f"Elapsed time: \t\t {end_time - start_time:.7f}")
        print(f"_" * 20)
    return wrapper

# returns list of numbers from 0 to 1000
@performance_measure
def using_range():
    ''' using range '''
    list_val = list(range(100000))

@performance_measure
def using_comprehension():
    '''using list comprehension'''
    list_val = [x for x in range(100000)]

@performance_measure
def using_list_append():
    ''' using list append'''
    list_val = []
    for x in range(100000):
        list_val.append(x)

using_range()
using_comprehension()
using_list_append()

