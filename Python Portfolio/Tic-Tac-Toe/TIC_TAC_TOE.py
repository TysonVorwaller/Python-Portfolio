#Tyson Vorwaller
#12/18
#Tic_Tac_Toe

# global constants
X ="X"
O ="O"
EMPTY =" "
TIE ="TIE"
NUM_SQUARES = 9

#Functions
#################################################################
#Start Display
def display_instructions():
    """Welcome to TIC-TAC-TOE!"""
    print("""\nTo play choose where you put your X by inputting 0-8
and the computer will choose where to place it's O
if you get three in a row you win!!!""")
    print("""

               """)
    print("Prepare yourself!")
#################################################################
#Yes No Input
def ask_yes_no(question):
          response= None
          while response not in ("y","n"):
              response= input(question+" y or n").lower()
          return response
#################################################################
#Ask player for number
def ask_number(question, low, high):
    """Ask for a number within a range."""
    response= "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                reponse = input(question)
        else:
            print("You must enter a number")
            response = input(question)
    return int(response)

#x=ask_number("Enter a number between 1 and 10",1,11)
#print(x)
################################################################
#pieces
def pieces():
   """Determine if player or computer goes first."""
   go_first = ask_yes_no("Do you require the first move? (y/n): ")
   if go_first == "y":
       print("\nTHen take the first move. You will need it.")
       human = X
       computer = O
   else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer= X
        human= O
   return computer, human
################################################################    
#New Board
def new_board():
    """Create new game board."""
    board= []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
################################################################
#Display Board
def display_board(board):
    """"Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|" , board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")
################################################################
#Legal Moves
def legal_moves():
    """Create list of moves."""
    moves= []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
################################################################
#Winner
def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        
        if EMPTY not in board:
            return TIE
        
        return None
#################################################################
def human_move(board):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_num("Where would you like to place your mark (0 - 8)\n",0 ,NUM_SQUARES)
        if move not in legal:
            print("There is already a mark there. How dumb are you?")
            print("Fine... ")
    return move
############################################################################
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X
############################################################################
def congrats_winner(winner,computer,human):
    the_winner = winner
    if the_winner != TIE:
        print("The winner is "+the_winner)
    else:
        print("You tied.")

    if the_winner == computer:
        print("You suck at this game")
    elif the_winner == human:
        print("I am defeated for now but I will get you another day.")
    if the_winner == TIE:
        print("You couldn't even beat me. Stupid mortal.")
############################################################################
def computer_move(board,computer,human):
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("I shall take square number", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
############################################################################
def main():
    display_instructions()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = computer_move(board, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrats_winner(winner,computer,human)
#############################################################################
main()
input("\n\nPress the Enter key to quit.")













































    
          
          

          
