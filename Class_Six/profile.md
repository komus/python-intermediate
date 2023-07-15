# Profiling

- A process that helps you understand the runtime performance of your program

- profiler modules like `cprofile` are designed to provide execution profile not for benchmarking


## Timeit

- measure the execution time of a code snippet
- It does not take into account background processes, it runs the code multiple times making the result statistically significant

```python
import timeit
timeit.timeit(stmt, setup, number)


#OR 
from timeit import timeit
timeit(stmt, setup, number)
```

where:

- stmt is the block of code you want to measure the execution time
- setup things required before executing the statement e.g import statement
- number of times you want the code to run and then compute the avg time