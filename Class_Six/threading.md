# Multithreading

- It is a way to concurrently run multiple threads. Threads are smaller unit of a process
- Run different part of code simulteneously
- multithreading in python doesnt actually result in true parallel execution due to Global Interpreter Lock (GIL)
- GIL is a lock that allows only one thread to execute at a time in a single process. Python uses GIL to simplify memory allocation and avoid conflicts among threads
- 

# Multiprocessing
- Multiprocessing is a way to concurrently run task in python
- the module allows us to spawn multiple processes and manage and synchronize their execution
- each python process gets its own python interpreter and memory space so that they can work independently without affecting others. Thus no GIL problem

- Highly CPU intensive, as each process can be assigned to a different CPU core. 
- Heavy weight as it requires duplicating resources between processes
- Data isnt shared directly between processes, thus inter-process communication is difficult


NOTE: MULTIPROCESSING IS NOT A UNIVERSAL SOLUTION TO MAKE THINGS FASTER

    If you have a task that requires I/O or heavy communication, multithreading or asynchronous I/O might be efficient