#f strings in python
letter = "Hey my name is {} and I am from {}"
country= "India"
name = "Harry"
print(letter.format(name,country))
#f string
print(f"Hey my name is {name} and I am from {country}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
#Docstrings in python: Python docstring are the string literals that appear right after the defination of a function, method, class, or module.
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)    
print(square.__doc__) #to print the docstring
#docstrings are write below the function name or write above the function body