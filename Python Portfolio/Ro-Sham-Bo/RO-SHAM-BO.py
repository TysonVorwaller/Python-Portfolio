#Tyson Vorwaller
#2/5/19
#Rock Paper Scissors

#Menu
def menu():
    menuchoice = input("Welcome to RO-SHAM-BO!!!!! \n 1: Play the Game \n 2: Credits \n 3: Quit \n Enter an option: ")
    menuchoice
    #Quit Option
    if menuchoice == "3":
        quit
    #Credits Option
    elif menuchoice == "2":
        print("This program was created by Tyson Vorwaller.\n\n\n")
        menu()
    #Game Option
    elif menuchoice == "1":
        game()
    #Invalid Option
    else:
        print("That is not a valid input.\n\n\n")
        menu()

    #Game
def game():
    #Importing Random
    from random import randint 

    #Moves 
    m = ["Rock", "Paper", "Scissors"]

    #random play to the com
    computer = m[randint(0,2)]

    #set player to False
    player = False

    while player == False:
    #Possible Player Comp Move Interactions
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "crushes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "crushes", player)
            else:
                print("You win!", player, "cut", computer)
    else:
        print("Game End or (Enter a Valid Input)\n\n\n")
        menu()
    
    player = False
    computer = m[randint(0,2)]

menu()
