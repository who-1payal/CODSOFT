#Rock, Paper and Scissor Game

import random
ch="x"
print("Welcome to rock,paper,scissor game!!")
c = 0
p = 0
t = 0
while ch=="x":
    game_options = ("rock","paper","scissor")
    player = None
    
    #Generating a random choice(rock, paper, scissor)for the computer
    computer = random.choice(game_options)

    while player not in game_options:
        
        #Prompting the user to choose rock, paper or scissor
        player = input("Enter your choice (rock,paper,scissor):")
        
        if player not in game_options:
            print("Please enter a valid choice(rock,paper or scissor)")

    #Showing player's and the computer's choice        
    print(f"Player choice:{player}")
    print(f"Computer choice:{computer}")
    
    #Game logic and displaying result
    if player==computer:
        print("This is a tie")
        t+=1
    elif player=="rock" and computer=="scissor":
        print("Congrats!!You win")
        p+=1
    elif player=="paper" and computer=="rock":
        print("Congrats!!You win")
        p+=1
    elif player=="scissor" and computer=="paper":
        print("Congrats!!You win")
        p+=1
    else:
        print("Alas!You lost")
        c+=1
    
    #Asking user if they want to play again
    if not input("Do you want to play again? (y/n):").lower() == "y":
        break
        
#Score tracking
print("Total number of matches:\n",p+c+t)
print("Player's score:\n",p)
print("Computer's score:\n",c)
print("Number of tie matches:\n",t)

print("Thanks for Playing!!")

