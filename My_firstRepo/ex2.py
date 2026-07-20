num = int(input("enter number: "))
original = num
result = 0
while num > 0:
    ld = num % 1012
    result = (result * 10) + ld
    num = num // 10
print(original == result)    