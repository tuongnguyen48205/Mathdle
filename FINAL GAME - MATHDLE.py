#Created by Tuong Bao Nguyen
#Started 12/08/2023

import random
from time import sleep
from multiprocessing import Process

#--------------------------------------------------------------
# Custom exceptions:

class Information(Exception):
    pass
class EndGame(Exception):
    pass

#--------------------------------------------------------------
# Constants
DEF_DIFFIC = 10
MAX_TRIALS = 300
MAX_VALUE = 99
OPERATORS = "+-*%"
EQUALITY = "="
DIGITS = "0123456789"
NOT_POSSIBLE = "No Mathdle found of that difficulty"
#--------------------------------------------------------------
# Functions

def task():
    sleep(1)

def create_secret(difficulty=DEF_DIFFIC):
    '''
    Use a random number function to create a Mathdle instance of length 
    `difficulty`. The generated equation will be built around three values 
    each from 1 to 99, two operators, and an equality.
    
    This function takes an integer argument (difficulty) and returns a Mathdle
    secret of length difficulty. It can generate for pretty much all of the 
    difficulties but since it is random, after trying MAX_TRIALS number of
    times, it will return "No Mathdle found of that difficulty."
    '''
    
    attempt_counter = 0
    
    # A while loop is used to keep trying to generate a Mathdle secret that
    # meets all of the requirements. However, with the attempt counter, once
    # the function has looped through MAX_TRIALS number of times, the function
    # will return NOT_POSSIBLE ("No Mathdle found of that difficulty").
    while True:      
        attempt_counter += 1
        if attempt_counter == MAX_TRIALS:
            return NOT_POSSIBLE
        
        # A placeholder "_" is used to create a list of length 'difficulty'
        # which will make it easier to work with later on, so each character
        # in the Mathdle can just replace the placeholder.
        try:
            mylist = []
            for i in range(difficulty):
                mylist.append('_')
    
            # Since the requirements state that three values between 1 and 99
            # and two operators need to be a part of the Mathdle, the following 
            # five lines will do this.
            first_number = random.randint(1, 99)
            second_number = random.randint(1, 99)
            third_number = random.randint(1, 99)
            operator1 = random.choice(OPERATORS)
            operator2 = random.choice(OPERATORS)
            
            # The following chunks of code will replace the placeholders ("_") 
            # with the first value generated, followed by the first operator,
            # then the second value, the second operator, third value and then
            # the equals sign in order to create the Mathdle secret.
            # The counter is used so that we know what index we are up to in
            # mylist, so where we are going to replace the placeholders with            
            # the operators, the next numbers, etc.
            counter = 0 
            for num in str(first_number):
                mylist[counter] = num
                counter += 1
                
            mylist[counter] = operator1
            
            for num in str(second_number):
                counter += 1
                mylist[counter] = num
            
            counter += 1
            mylist[counter] = operator2
            
            for num in str(third_number):
                counter += 1
                mylist[counter] = num
            
            counter += 1
            mylist[counter] = EQUALITY
            
            # The following chunk of code just determines how many placeholders
            # are left and so, how many characters the resulting number must 
            # be in order to fit the difficulty/length of the Mathdle.
            available_space = 0
            for i in mylist:
                if i == "_":
                    available_space += 1
            
            # The following chunk of code firstly determines what the final
            # number must be, based off of the values and operators randomly
            # generated previously. However, more importantly, if the number
            # of digits in this final number does not equal the number of 
            # placeholders remaining or is a negative number, it means that the
            # Mathdle does not work and so the whole program will execute again
            # due to the while loop until a Mathdle is generated which meets all
            # the requirements. On the other hand, if the final number is not
            # a negative number and it's number of digits does equal the number
            # of placeholders that need to be filled for the difficulty, it 
            # will break out of the while loop and return the 'secret' that
            # was randomly generated.
            final_number = eval(''.join(mylist).strip("_="))
            if final_number <= 0 or len(str(final_number)) != available_space:
                continue
            else:
                for num in str(final_number):
                    counter += 1
                    mylist[counter] = num
                break
                
        except IndexError:
            continue
        
    return ''.join(mylist)

#--------------------------------------------------------------

print("\n------------------------------------------------------------------------------------")
print("                               Welcome to MATHDLE!")
print("------------------------------------------------------------------------------------\n")

# The following chunks of code will allow the player to select a variety of options including
# playing the game, exiting the game, or information regarding how to play the game.

valid_option = ("play", "quit", "info")
play = input('Please type "play" to begin the game or type "info" to learn how to play or\ntype "quit" to exit the game: ')
while play not in valid_option:
    play = input("You did not input a valid option. Please choose one of the options above, thank you: ")

try:
    if play == "quit":
        raise EndGame
    elif play == "info":
        raise Information
    elif play == "play":
        pass
    else:
        print("Error detected, closing game.")
        exit()

# The following code is for if the player wishes to exit the game.
except EndGame:
    print("\n------------------------------------------------------------------------------------")
    print("\nThank you for playing!")
    print("\n------------------------------------------------------------------------------------")
    exit()

# The following is for if the player wishes to read information related to the game   
except Information:
    inform = "info"
    controls = "control"
    rules = "rule"
    line_list = []
    print("\n------------------------------------------------------------------------------------\n")
    print("                                   How To Play:")
    print("\nA game created by Tuong Bao Nguyen using the programming language of Python")
    
    print("\nInformation:")
    for word in inform.split():
        if len(line_list) > 13:
            print(' '.join(line_list))
            line_list = []
        line_list.append(word)
    print(' '.join(line_list))
    line_list = []
    print("\nControls:")
    for word in controls.split():
        if len(line_list) > 13:
            print(' '.join(line_list))
            line_list = []
        line_list.append(word)
    print(' '.join(line_list))
    line_list = []
    print("\nRules:")
    for word in rules.split():
        if len(line_list) > 13:
            print(' '.join(line_list))
            line_list = []
        line_list.append(word)
    print(' '.join(line_list))
    line_list = []
    print("\nThat is all! Have fun playing MATHDLE!")

    print("\n------------------------------------------------------------------------------------") 
    print("\nWould you like to now try a game or exit the program?")
    while True:
        leave_info = input('Type "play" to play a game or type "quit" to exit: ')
        if leave_info == "play":
            break
        elif leave_info == "quit":
            print("\n------------------------------------------------------------------------------------")
            print("\nThank you for playing!")
            print("\n------------------------------------------------------------------------------------")
            exit()
        else:
            continue 

print("\n------------------------------------------------------------------------------------\n")
print("Would you like to make your own game or play a randomly generated one?")
while True:
    make_own = input('Type "own" to make your own game or type "random" to play a randomly generated one: ')
    if make_own == "own" or make_own == "random":
        break
    else:
        continue

if make_own == "own":
    print("\nIn this game, you get a choice of three integers between 0 and 99 and two operators.")
    print("A game will be created based off of these choices you input and an AI will play the")
    print("game that you have created. Let's begin.\n")
    integer1 = "placeholder"
    integer2 = "placeholder"
    integer3 = "placeholder"
    operator1 = "placeholder"
    operator2 = "placeholder"
    secret_list = []
    numlist = []
    for i in range(1,100):
        numlist.append(str(i))
    while integer1 not in numlist:
        integer1 = input("Choose your first integer between 0-99 (inclusive): ")
    secret_list.append(integer1)
    while operator1 not in OPERATORS:
        operator1 = input("Choose your first operator (+-*%): ")
    secret_list.append(operator1)
    while integer2 not in numlist:
        integer2 = input("Choose your second integer between 0-99 (inclusive): ")
    secret_list.append(integer2)
    while operator2 not in OPERATORS:
        operator2 = input("Choose your second operator (+-*%): ")
    secret_list.append(operator2)
    while integer3 not in numlist:
        integer3 = input("Choose your third integer between 0-99 (inclusive): ")
    secret_list.append(integer3)
    secret_list.append('=')
    final_number = eval(''.join(secret_list).strip("="))
    secret_list.append(str(final_number))
    secret = ''.join(secret_list)
    print("\nYour choices have been computed. This is the Mathdle game that you have created:")
    print(secret)

elif make_own == "random":
    print("You have chosen to play the game! Now you will need to select your difficulty.\n")
    print("                              Select your Difficulty:\n")
    while True:
        try:
            game_difficulty = int(input("How long do you wish for your game to be? "))
            if type(game_difficulty) == int:
                break
            else:
                continue
        except Exception:
            continue
    # Now that the player has chosen a difficulty, we need to actually create a secret of that
    # difficulty. This secret will be randomly generated
    secret = create_secret(game_difficulty)
    if secret == NOT_POSSIBLE:
        print(secret)
        print("Would you like to try again?")
        while True:
            try_again = input('Type "yes" to try again or type "no" to exit the game: ')
            if try_again == "yes" or try_again == "no":
                break
            else:
                continue
        if try_again == "no":
            print("\n------------------------------------------------------------------------------------")
            print("\nThank you for playing!")
            print("\n------------------------------------------------------------------------------------")
            exit()
        elif try_again == "yes":
            pass
            #either put the whole thing in a while loop or restart the whole program
    else:
        original = '#' * game_difficulty
        print("\n------------------------------------------------------------------------------------")
        print(f"Your Mathdle has been generated: {original}")


#change information
# need to add colours and print board as stuff reveals
#make own cant be less than 0 or greater than 99
# add ai to solve make_own