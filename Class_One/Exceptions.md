# Exceptions in Python

## Types of error
- logical error
- syntax error
- runtime error

## Handling exceptions
try - except block

- ZeroDivisionError: divide by zero
- KeyError: When you try to get a get that doesnt exist in a dictionary
``` python
        val = {
        "word": 2,
        "family": 8
    }

    print(val["word"])
    print(val["sun"])
```

- IndexError: out of range of available subscripts
``` python
list1 = [2,2,45,5,6,7,8]
print(list1[3])
print(list1[9])
```
- ImportError: from `<module>` import `<method>` has a name that cannot be found. You can find the module but not the name
- ModuleNotFoundError: You cannot find the module of your import

- NameError: trying to access a variable that isnt defined

## Raising Exceptions
You want to force a specific exception to occur

## Finally in Try/Except block
Finally is executed regardless if an error occured. i.e it is run after the try or except block has been executed. Examples
  1. Open a file for operation, regardless of the outcome, you want to close the file
  2. Open a database connect for operation, and close it

## Guidelines
- Specify the type of Exception to be handled in your Except
- Ensure clear error messages
- You dont want too many try/except block in your code, only use when necessary. Ensure you handle outliers appropriately

## Custom Exception
``` python
class MyExceptionClass(Exception):
    pass

try:
    raise MyExceptionClass("Custom Exception")
except MyExceptionClass as err:
    print(err)
```
