# lambda expression

- They are anonymous functions
- They have no name (dont define them with a name) and does not use the keyword `def` like normal functions
- anonymous functions are defined using `lambda` keyword

``` python
def function_name():
    pass
```

## Syntax for defining lambda
``` python
    lambda arguments: expression
```
- lambda keyword
- argument(s) # any number of argument
- colon
- expression # only one expression


## Applications

- map
- filter
- reduce
- any other time you want a function object

### Map
- it applies a given function to each item of an iterable (list, set, tuple etc) 
- returns a list of the result

### Filter

- this constructs a list from elements of an iterable(list, tuple) for which the function condition returns TRUE
- returns elements that the condition holds true

### Reduce
- returns a single value
- It processes the elements of a collection from left to right (cummulatively) taking 2 arguments at a time
For instance taking `[1,2,4,5,6]`, In the first cycle it takes `1` and `2`, performs transformation/action you stated (addition), then it returns the result of the transformation `3`

The second cycle, it takes the result of the previous transformation `3` and `4`, returns `7`
the third cycle, `7` and `5` to return 12

.... continues until the end of the list

## limitation of  lambda
- readability
- lambdas can only evaluate a single expression
- cannot use statements like `assert` or `pass` in lambda
- does not allow docstrings 
- limited traceback information during debugging