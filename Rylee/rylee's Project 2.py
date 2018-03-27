#This part of the program provides the reader with instructions on how to use the gamprint("Hello! Welcome to the 10 question Python quiz!")

print("Directions-Read and answer the questions to the best of your ability. At the end of the Python quiz type in getName(); for a very special message :)!")

print("Have Fun!")
    
#This is the first question in the program, the if allows the program to match the  answers together to see if the answer is correct 

print("In Python what can you change or record?")
answer = raw_input().lower()
if answer == "list":
    print("Good job! :)")
else:
    print("Good try the answer was list.")
     

#This is the second question in the program, .lower() is used to make the letters in the user's answer lowercase so the computer can read it incase they typed in uppercase
print("What defines the level of visibilty to the rest of the program of a line of code?")
answer = raw_input().lower()
if answer == "scope":
    print("Awsome!")
else:
    print("Good Try The Answer Was scope!")

#This is the third question in the program,else is used in the program if the user inputs another answer it will tell them the right answer and say somthing like good try
print("What do you call a programming conditional statement that, if proved true,will preform some action?")
answer = raw_input().lower()
if answer == "if statement":
    print("Your Good at this!")
else:
    print("It was if statement!")
    


#This is the fourth question in the program,raw_input() is used for the user to input their own answer to the question
print("What do you call a piece of code that checks if a condition is proven to be true or false?")

answer = raw_input().lower()
if answer == "conditional statement":
    print("Excelent!")

else:
    print("Its conditional statement!")

#This is the fifth question in the program
print("What is a block of code that is invoked by a calling program,best used to provide an autonomous service or calcalaton?")
print("A:list,B:init,or C:function.")
answer = raw_input().lower()
if answer =="c":
      print("Great job!")
else:
      print("Good try it was c.")

      
#This is the sixth question in the program,answer == is used to again match the user's answer with the correct answer and if it matchs it will go non if not it will go to else
print("What is a container class that holds and manipulates multiple sprites?")
answer=raw_input().lower()
    
if answer =="sprite group":
      print("Awesome!")
else:
      print("Almost!It was a sprite group.")

      
#This is the seventh question in the program
print("What is taking the information from a Model or Sprite and drawing it on the screen called?")
print("Is it A:Python or B:Render?")
answer = raw_input().lower()
if answer =="b":
      print("Yay you got it!")
else:
      print("Soooo close! It was b!")

#This the eighth question in the program
print("True or False:An event is a programming device that allows developers keep track of when particular actions occur within the code?")
print("True or False?")
answer = raw_input().lower()
if answer =="true":
      print("Woo Whoo!You got it.")
else:
      print("Almost got it! It is true.")


      
#This is the ninth question in the program,sencond to last.True or False choice
print("Almost last one,True or False?:blits def. is a method used to draw an object on the screen?")
print("True or False?")
answer = raw_input().lower()
if answer =="true":
      print("Yay you have one left!")
else:
      print("Close it was True.")
      


#This is the tenth and last question in the program
print("In Python what repeats things over and over?")
answer = raw_input().lower()
if answer == "while loop":
    print("Good Job you finished the quiz!")
else:
    print("You Finished the quiz!The Answer is while loop.")

#Function for getting user's name and delivers a suprise note at the end.+ name adds name on to the words in the parons
def getName():
    name = raw_input("What is your name?")

    print("Great job on the quiz! " + name)
    print("Come back soon :)!")




















