import random

top_of_range =input("Type a number: ")
if top_of_range.isdigit():
    top_of_range=int (top_of_range)

    if  top_of_range  <=0:
        print("Please Type a number Greater than zero next Time .")
        quit()

else:
    print("Please print a Number next time")
    quit()
 

random_number =random.randint(0,top_of_range) 
 

guesses=0
while True:
    guesses +=1   
    user_guess=input("Please make a Guess ! :")
    
    if user_guess.isdigit():  
       user_guess=int (user_guess)

 
    else:
       print("Please Enter a Number next time")
       continue 
    if user_guess ==random_number:
            print("You guessed pretty well")
            break
         
    elif user_guess > random_number:
            print("Your guess was Higher than the number! :")
    else:
            print("Your Guess was below the number !")

print("You got it in" , guesses,"Guesses")
        
    
  