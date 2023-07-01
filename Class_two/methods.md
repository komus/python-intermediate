# Methods

## Instance Method
- This is the most common type of method
- First parameter of the method in the class is `self`. `self` is a reference to the instance of the class. 
- Instance method can access and modify instance state  - data stored in an instance variable
## Class Method
- Class method is one that is called for the whole class, not an instance of it
- It can access data that belongs to the class itself
- it is marked with @classmethod decorator
- The first parameter is `cls`
- It is useful when you need a method that is not specific to an instance but involves the class somehow
- To call a class method, use class.methodname. You dont create an object of the class

## Static method
- It cannot access instance or class data, it is only bound to the class - it is within a class
- Has no idea about the instance or the class they are called on
- marked with @staticmethod decorator
- does not a specific first parameter
- It is usually used as a utility method that is related to the class


# Class Ordering
- Class definition
- class variables
- constructor
- methods   