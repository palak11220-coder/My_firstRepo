#exception Handling
a = input("enter the number: ")
print(f"multiplication table of {a} is: ")

try:
   for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*{i}}")
except Exception as e: #or we can write except instead of it
    print(e)

     #exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exceptiom handling deals with these evnts to avoid the program orf system crashing and without this process.exceptions would disrupt the normal operation of a program.
try:
   num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

    #we can use multi except like except IndexError
    