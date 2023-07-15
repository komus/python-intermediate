import cProfile
import timeit

# uses the stats 

def decrease():
    start = 10000
    end = 5000
    while start >= end:
        start -= 1


decrease()
print(cProfile.run('decrease()'))


# FOr benchmarking use Timeit

def string_join():
    return "-".join(str(n) for n in range(100))

if __name__ == "__main__":

    setup = "from __main__ import string_join"
    stmt = 'string_join()'

    print(timeit.timeit(stmt=stmt, setup=setup, number=1000))


"""
Timer class is used to create a timer object where each object 
can be started and stopped multiple times e.g StopClock
"""

t = timeit.Timer(lambda: "-".join(str(n) for n in range(100)))
print(t.timeit(1000))