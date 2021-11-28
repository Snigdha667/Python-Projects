print("Welcome! to my quiz on COMPUTERS!!")
s=input("Do you want to play?? (answer: yes/no) :: ")
if s.lower() != "yes":
    print("Thank You for reaching us, may meet some other time! :)")
    quit()
print("____________________________________________________________________________________________________________________________________")
print("BASIC INSTRUCTIONS: 1. You will be given 5 questions to answer. \n 2.If you skip a question, it would be considered incorrect. \n"
      +"3.Every question contains 1 marks for correct answer and -0.25 for incorrect. \n 4.At last you will given a quick summary of your performance and result.")
print("____________________________________________________________________________________________________________________________________")
a= input("So! ARE YOU READY TO PLAY!!! (answer :: yes/no) :: ")
if a.lower() != "yes":
    print("May be not ready this time.. Thank You for reaching us, may meet some other time when you are fully prepared! BEST OF LUCK FOR PREPARATION!! :)")
    quit()
score =0
print("So! Let's begin !!!! ")
print()
a1 = input("QUESTION 1 :: What is full form of CPU ? (ANSWER ::) ")
if a1.lower() == "central processing unit":
    print("Congratulations! You got this answer CORRECT!! ")
    score +=1
else:
    print("Sorry! You got this answer INCORRECT!! ")
    score -=0.25
print()
a2 = input("QUESTION 2 :: What is full form of RAM ? (ANSWER ::) ")
if a2.lower() == "random access memory":
    print("Congratulations! You got this answer CORRECT!! ")
    score +=1
else:
    print("Sorry! You got this answer INCORRECT!! ")
    score -=0.25
print()
a3 = input("QUESTION 3 :: What is full form of ROM ? (ANSWER ::) ")
if a3.lower() == "read only memory":
    print("Congratulations! You got this answer CORRECT!! ")
    score +=1
else:
    print("Sorry! You got this answer INCORRECT!! ")
    score -=0.25
print()
a4 = input("QUESTION 4 :: What is full form of IP ? (ANSWER ::) ")
if a4.lower() == "internet protocol":
    print("Congratulations! You got this answer CORRECT!! ")
    score +=1
else:
    print("Sorry! You got this answer INCORRECT!! ")
    score -=0.25
print()
a5 = input("QUESTION 5 :: What is full form of ALU ? (ANSWER ::) ")
if a5.lower() == "arithmetic logical unit":
    print("Congratulations! You got this answer CORRECT!! ")
    score +=1
else:
    print("Sorry! You got this answer INCORRECT!! ")
    score -=0.25
print()
print("CONGRATULATIONS!! YOU FINISHED THE QUIZ !!!!")
print("You got " + str(score) + "/ 5 marks!!")
print("Your percentage gained :: "+ str((score*100)/5.0))
print("...........................................................................................................................")
print("Thanks for taking our quiz !!! Hope it helps!")