#from math import Classification

# try: # run this and if no error continue
#     num1 = int(input("Enter a number"))
#     num2 = int(input("Enter a number"))
#     print(num1 / num2)
# except ValueError: # oops there is an error, this is how I handle the error. 
#     #Nest to catch error that occur in try block
#     print("Expected numbers")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except Exception as err:
#     print(f"Error occured: {err}") 
# finally:
#     print("It ran!!!")

# You can have more than one except with a try block

# print("name")
# raise ValueError("Just raising error for fun!!!")

class ValidationError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

#super is the proxy for access the base class 
#i.e the class you are inheriting from

try:
    raise ValidationError("Invalid data passed",
                         {"error1": "integer allowed",
                         "error2": "string allowed"})

except ValidationError as e:
    print(e)
    print(e.errors)

