#Finally Keyword in Python
#Finally Clause
#The finally code block is also a part of exception handling. When we handle exception using the try and accept block. we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding  tasks like closing thw resources or closing databases connection or may be ending the program execution with a delightful message.
try:
  l = [1,5,6,7]
  l = int(input("Enter the index: "))
  print(l[i])
except:
  print("some error occurred")  

finally:
    print("I am always executed")
#but there is a difference between direct print and finally
#If we define a function whether the error occured or not it prints the except and finally case
#if we give true value it gives the return text but if we give false value it gives output only by printing the line.