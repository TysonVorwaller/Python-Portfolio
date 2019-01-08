#Tyson Vorwaller
#1/19
#Trivia Game

import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return the next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answer = next_line(the_file)
        answers.append(answer)
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file) 

    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("test_file.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, explanation = next_block(trivia_file)

    test_file.close()

    print("That was the last question!")
    print("You're final score is", score)
 
main()  
input("\n\nPress the enter key to exit.")

##the_file = open_file("test_file.txt", "r")
##category, question, answers, correct, explanation = next_block(the_file)
##print(category)
##print(question)
##print(answers)
##print(correct)
##print(explanation)

##file = open_file("exe_file.txt","w")
##file.write("This/ is/ a/ Test")
##file.close()
##file = open_file("exe_file.txt","r")
##line = next_line(file)
##print(line)
