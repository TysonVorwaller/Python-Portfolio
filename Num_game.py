#Tyson Vorwaller & Logan Nelson
#11/2
#Project 4
#Guess My Number Game

import random
answer= random.randrange(0,101)

coin= random.randrange(0,3)

def menu():
    
    menu_choice= int(input(""""1 Number Guess Game
2 Coin Flip
3 Credits
4 Quit
Enter 1, 2, 3, or 4."""))

    if menu_choice == 1:
        num_guess()

    elif menu_choice == 2:
        coin_flip()

    elif menu_choice == 3:
        print("""This game was made by
Logan Nelson
&
Tyson Vorwaller
in Broadbent's Python Class.""")
        menu()

    elif menu_choice == 4:
        exit()
        

    else:
        print("Invalid entry enter 1,2, or 3.")
        menu()

def num_guess():
    attempts= 5

    print("You have ",attempts,"left")
    
    guess= int(input("Enter a number between 1 and 100."))

    if attempts == 0:
        print("You ran out of attempts. Thanks for Playing!")
        menu()
    
    elif guess == answer:
        print("YOU WIN!!!!")
        menu()

    elif guess > answer:
        print("You guessed too high.")
        attempts -= attempts
        num_guess()

    elif guess < answer:
        print("You guessed too low.")
        attempts= attempts - 1
        num_guess()

    else:
        print("Only guess a number between 1 and 100.")
        num_guess()

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
        

    

    
