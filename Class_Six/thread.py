import threading
import timeit

def iterate_a_concept(iter):
    for item in iter:
        print(item)


# thread1 = threading.Thread(target=iterate_a_concept, args=("python Inter",))
# thread2 = threading.Thread(target=iterate_a_concept, args=(range(7),))

# thread1.start()
# thread2.start()

# # after execution, threads needs to be exited and join the parent process

# thread1.join()
# thread2.join()

# print("Done")


"""
Compare multithreading and procedural - 

Example:  Decrease a number from the starting position to the end
10, 9, 8, 7, 6,5,....... end
"""

def decrease(start, end):
    while start >= end:
        start -= 1

def count_without_thread():
    decrease(10000, 0)


def count_with_threading():
    t1 = threading.Thread(target=decrease, args=(10000, 0))
    t2 = threading.Thread(target=decrease, args=(20000, 10000))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":

    thread_function = "count_with_threading()"
    no_thread_function = "count_without_thread()"
    setup = "from __main__ import count_with_threading, count_without_thread"

    print("Without thread: ", timeit.timeit(stmt=no_thread_function, setup=setup, number=500))
    print("With thread: ", timeit.timeit(stmt=thread_function, setup=setup, number=500))

"""
Threads time is higher than procedural because of Global Interpreter Lock (GIL) 
which allows only one thread to run in a process at a time
"""