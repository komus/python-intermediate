# Iterators

- Iterable is any object capable of returning its element one at a time. 
- i.e iterators are objects that can be iterated over like we do in a for loop
- they dont do any work until we explicitly ask for the next item
- It allows us not to store all items in memory: not allocating large amount of memory to a large collection. It remembers the item that was generated last and returns the next item based on the previous

- Example of common iterable objects:
1. list
2. Tuples
3. sets
4. dictionaries
5. files
6. strings

# What happens in a for loop
when the `for` loop is executed, python calls the `__iter__` function which returns an iterator which is an object with `__next__` method. `__next__` method is repeatedly called until it see a `StopIteration` exception - there is no more items to iterate over

``` python

for num in nums: 
```

# generators
A generator is a function that returns an iterator that produces a sequence of values when iterated over. it uses the keyword `yield` when it returns a value. `yield` statement turns a function into a generator object


## Why use generators
- easy to implement
- memory efficient
- for representing infinite stream
- efficient for pipelining => A pipeline is basically a series of operations. We can chain generators together
