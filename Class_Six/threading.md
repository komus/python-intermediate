# Multithreading

- It is a way to concurrently run multiple threads. Threads are smaller unit of a process
- Run different part of code simulteneously
- multithreading in python doesnt actually result in true parallel execution due to Global Interpreter Lock (GIL)
- GIL is a lock that allows only one thread to execute at a time in a single process. Python uses GIL to simplify memory allocation and avoid conflicts among threads