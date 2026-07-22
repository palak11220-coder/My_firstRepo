#Raising Custom Errors
#In python we can raise custom error by using the raise keyword
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
#Defining Custom exceptions
#In Python we can define custom exceptions by creating a new class that is derived from the built in Exception class.


#syntax to define custom exceptions:

class CustomError(Exception):
    #code
    pass
try:
    #code
    pass

except CustomError:
    #code
    pass