import threading
import timeit
import multiprocessing

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

def count_with_multiprocessing():
    p1 = multiprocessing.Process(target=decrease, args=(10000,0))
    p2 = multiprocessing.Process(target=decrease, args=(20000, 10000))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":

    thread_function = "count_with_threading()"
    no_thread_function = "count_without_thread()"
    multi = "count_with_multiprocessing()"
    setup = "from __main__ import count_with_threading, count_without_thread, count_with_multiprocessing"

    print("Without thread: ", timeit.timeit(stmt=no_thread_function, setup=setup, number=100))
    print("With thread: ", timeit.timeit(stmt=thread_function, setup=setup, number=100))
    print("With multiprocessing: ", timeit.timeit(stmt=multi, setup=setup, number=100))