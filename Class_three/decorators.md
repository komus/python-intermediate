# Decorators

- It allows programmers to modify the behaviour of a function or a class without modifying the function itself. 
- Allows us to wrap a function with another function in order to extend the behaviour of the wrapped function

- Eg logging, test performance, cache, verify permissions, decimal places of floating numbers

## building blocks for decorator
- A funtion is an instance of the object type i.e a function is an object because we can store a function in a variable
- A function can be passed as an argument to another function
- A function can be nested within another function
- A nested function can be returned


## syntax for a decorator

```python
    def decorator_function_name(func):
        def wrapper_func():
            /// Do something(s)

        return wrapper_func
```

To use the decorator syntax
``` python
    @decorator_function_name
    def my_function():
        pass
```

# Decorators with arguments
To create a decorator that gets an arguments, you need to create a function that returns a decorator, rather than writing the decorator directly

```python
    def function_that_returns_decorator(**arguments):
        def decorator_function_name(func):
            def wrapper_func():
                /// Do something(s)

            return wrapper_func
        return decorator_function_name
```

# Chaining Decorators
- can apply more than 1 decorator to a function
- Apply it from bottom to top - most inner decorator is applied first

```python
@docorator1
@decorator2
def function():
    pass


function()
```

This means `decorator1(decorator2(function))`