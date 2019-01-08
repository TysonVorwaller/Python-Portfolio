#Tyson Vorwaller & Logan Nelson
#11/2
#Project 4
#Guess My Number Game

import random
answer= random.randrange(0,101)

coin= random.randrange(0,3)
attempts= 5
def menu():
    global attempts
    attempts = 5
    
    menu_choice= int(input("""1 Number Guess Game
2 Coin Flip
3 Credits
4 Quit
Enter 1, 2, 3, or 4."""))
#Num Guess
    if menu_choice == 1:
        num_guess()
#Coin Game
    elif menu_choice == 2:
        coin_flip()
#Credits
    elif menu_choice == 3:
        print("""This game was made by
Logan Nelson
&
Tyson Vorwaller
in Broadbent's Python Class.""")
        menu()
#Exit
    elif menu_choice == 4:
        exit()
        

    else:
        print("Invalid entry enter 1,2, or 3.")
        menu()
#Num Guess
def num_guess():
    global attempts
   

    
    
    guess= int(input("Enter a number between 1 and 100."))

    if attempts == 1:
        print("You ran out of attempts. Thanks for Playing!")
        menu()
    
    elif guess == answer:
        print("YOU WIN!!!!")
        menu()

    elif guess > answer:
        print("You guessed too high.")
        attempts -= attempts
        print("You have ",attempts,"left")
        num_guess()

    elif guess < answer:
        print("You guessed too low.")
        attempts= attempts - 1
        print("You have ",attempts,"left")
        num_guess()

    else:
        print("Only guess a number between 1 and 100.")
        num_guess()
#Coin Game
def coin_flip():

    coin_choice= int(input("""1 Heads
2 Tails
Enter 1 or 2."""))

    if coin_choice == coin:
        print("YOU WIN!!!")
        menu()

    elif coin_choice != coin:
        print("You Lose! :(")
        menu()

    else:
        print("Please choose 1 or 2.")
        coin_flip()

 
menu()   
        

    

    
