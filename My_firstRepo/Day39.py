#Kaun Banega Crorepati
questions = [
    [
    "What is the capital of India?", "Delhi","Noida","Meerut","Surat",1
   ],
    [
    "What is the capital of India?", "Delhi","Noida","Meerut","Surat",1
   ],
    [
       "What is the capital of India?", "Delhi","Noida","Meerut","Surat",1
      ],
    [
       "What is the capital of India?", "Delhi","Noida","Meerut","Surat",1
      ],  
] 

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 100000, 370000]
money=0
i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {questions[1]}    b. {questions[2]}")
    print(f"c. {questions[3]}    d. {questions[4]}")
    reply = int(input("Enter your answer (1-4) "))
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i == 1):
           money = 10000
    else:
      print("wrong answer!")      
      break
      