import random
#it is easier to import modules at the top of the program
user_wins=0
computer_wins=0
options =["Rock" ,"Paper" ,"Scissors"]

while True:
    user_input =input("Type rock /Paper/Scissors or Q to quit :  ").lower()
    if user_input =="q":
        break
    
    if user_input not  in options:
        #keep asking the user to type something valid
        continue 
    
    random_number = random.randint(0,2)
    #rock:0,paper:1,Scissors:2 
    computer_pick = options[random_number]
    print("The computer picked" ,computer_pick + ".")

    if user_input =="rock" and computer_pick =="Scissors":
        print("You won !")
        user_wins += 1 
         
    elif user_input =="Paper" and computer_pick =="rock":
        print("You won !")    
        user_wins += 1
        
    elif user_input =="Scissors" and computer_pick =="paper":
        print("You won !")
        user_wins += 1 

    else:
        print("You Lost!") 
        computer_wins +=1
        break
       




print("Siku ingine Bro  !")



