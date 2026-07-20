def factorial(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

print(factorial(4))
print(factorial(9))

#Day31
s={2,4,2,6} #unordered collection of data sets
print(s)
