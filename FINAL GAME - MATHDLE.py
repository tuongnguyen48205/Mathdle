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
class Endturn(Exception):
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
GREEN = "green"
YELLO = "yellow"
GREYY = "grey"
POSSIBLE_CHARACTER = "+-*%0123456789="
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

def set_colors(secret, guess):
    '''
    Compares the latest `guess` equation against the unknown `secret` one. 
    Returns a list of three-item tuples, one tuple for each character position 
    in the two equations:
        -- a position number within the `guess`, counting from zero;
        -- the character at that position of `guess`;
        -- one of "green", "yellow", or "grey", to indicate the status of
           the `guess` at that position, relative to `secret`.
    The return list is sorted by position.
    '''
    
    # 'mylist' is used to store all the information such as position, character
    # and their corresponding status of 'green', 'yellow', or 'grey'.
    mylist = []
    secret_tuple = tuple(secret)
    guess_tuple = tuple(guess)
    
    # The following chunk of code is used to count the number of times each
    # character in the secret is present in the secret.
    secret_dict = {}
    for item in secret_tuple:
        if item in secret_dict:
            secret_dict[item] += 1
        else:
            secret_dict[item] = 1
    
    # Similar to before, the following chunk of code is used to count the
    # number of times each character in the guess is present in the guess.
    guess_dict = {}
    for item in guess_tuple:
        if item in guess_dict:
            guess_dict[item] += 1
        else:
            guess_dict[item] = 1
    
    # The following chunk of code goes through each of the dictionaries and 
    # determines if the same characters are present in both the secret and the
    # guess as well as if they appear the same number of times, and places it
    # into a list. This is done due to the fact that if they do appear the same
    # number of times, the resulting status should either be 'green' or
    # 'yellow'. It is not possible for it to be 'grey'.
    similar = []
    for (keys1, values1) in secret_dict.items():
        for (keys2, values2) in guess_dict.items():
            if keys1 == keys2 and values1 == values2:
                similar.append(keys1)

    # The following chunk of code goes through each character in both the 
    # secret and the guess. If they have the same index and are the same
    # character, it means that the resulting status should be 'green'.
    # Additionally, since that character has been 'dealt' with, the number of 
    # times that character appears in the secret dictionary is reduced by one
    # which will be useful later on.
    countlist = []
    for j in range(len(secret)):
        if guess_tuple[j] == secret_tuple[j]:
            countlist.append(j)
            mylist.append((j, guess_tuple[j], GREEN))
            secret_dict[guess_tuple[j]] -= 1
        
    for i in range(len(secret)):
        # 'countlist' was used in order to determine which characters have 
        # been 'dealt' with. Therefore, if i is in countlist, it means that
        # at that index, the colour was 'green' and was already handled so it
        # just passes.
        if i in countlist:
            pass
        # As stated before, if a character is in 'similar', it appears in both
        # the guess and the secret the same number of times. Since all the 
        # 'green' characters are already dealt with, it means that this certain
        # character must be 'yellow'. Finally, since this character has been
        # 'dealt' with, the number of times that character appears in the
        # secret dictionary is reduced by one.
        elif guess_tuple[i] in similar:
            mylist.append((i, guess_tuple[i], YELLO))
            secret_dict[guess_tuple[i]] -= 1
        # The following elif statement are for the remaining characters in
        # the secret. If the number of times the character appears in the 
        # secret_dict is less than or equal to 0, it means that the character
        # although the character itself is present in the secret, the number of
        # times it is present in the guess is greater than the number of times
        # it is present in the secret. For example, if in the guess there are
        # three '*' and in the secret there are only two, only the first two
        # will either be 'green' or 'yellow' while the third one will be 
        # 'grey' and so for such characters, it's status is 'grey'. Otherwise,
        # it means that the character is still in the secret somewhere so its
        # status is 'yellow'. Finally, since the character has been 'dealt'
        # with, the number of times taht character appears in the secret
        # dictionary is now reduced by one.
        elif guess_tuple[i] in secret_tuple:
            if secret_dict[guess_tuple[i]] <= 0:
                mylist.append((i, guess_tuple[i], GREYY))
            else:
                mylist.append((i, guess_tuple[i], YELLO))
            secret_dict[guess_tuple[i]] -= 1
        # This else statement means that the character is not present in the 
        # secret at all and so its status is 'grey'
        else:
            mylist.append((i, guess_tuple[i], GREYY))
       
    return sorted(mylist)

def create_guess(all_info, difficulty=DEF_DIFFIC):
    '''
    Takes information built up from past guesses that is stored in `all_info`, 
    and uses it as guidance to generate a new guess of length `difficulty`.
    '''
    
    # A placeholder "_" is used to create a list of length 'difficulty'
    # which will make it easier to work with later on, so each character
    # in the Mathdle can just replace the placeholder.
    mylist = []
    for i in range(difficulty):
        mylist.append("_")
              
    # The following chunk of code goes through all the information. If the 
    # information has the tag, 'green', the function will use the position
    # of the information in order to place the character directly where it 
    # should be within the guess, replacing the placeholder "_".
    for info in all_info:
        for item in info:
            if item[2] == GREEN:
                mylist[item[0]] = item[1]
    
    # The following chunk of code uses a while loop which continues until all
    # the placeholder "_" are replaced with a possible Mathdle character
    while "_" in mylist:
        try:
            counter = -1  # Counts the position of the character  
            for character in mylist:
                counter += 1
                # Only "_" characters need to be replaced. Other filled spaces
                # can be ignored.
                if character == "_":
                    # A random character needs to be chosen in order to fill
                    # the "_" placeholder slot.
                    possible = random.choice(POSSIBLE_CHARACTER)
                    # The following if statement is for the first time, when
                    # the all_info list is still an empty list and there is no
                    # information.
                    if all_info == []:
                        mylist[counter] = possible
                    else:
                        for info in all_info:
                            for item in info:
                                # The following bit of code checks if the 
                                # randomly chosen character is already in 
                                # all_info with the same position. If the 
                                # status is 'grey' or 'yellow' it would not 
                                # make sense to make this guess since this has
                                # already been tried and failed and so an
                                # error is raised after putting the placeholder
                                # back in. Otherwise, if it is not already in 
                                # all_info or if it does not have a 'grey' or 
                                # 'yellow' tag, the possible character replaces 
                                # the placeholder "_".
                                if item[1] == possible and item[0] == counter:
                                    if item[2] == GREYY or item[2] == YELLO:
                                        mylist[counter] = "_"
                                        raise ValueError
                                    else:
                                        mylist[counter] = possible
                                else:
                                    mylist[counter] = possible
                                    
        # The error raised previously leads to this exception below which is 
        # used to instantly break out of the nested loop and since there are 
        # still placeholder "_" present in the list, the while loop starts
        # again until there are no  placeholders left.
        except ValueError:
            pass          

    return "".join(mylist)

def passes_restrictions(guess, all_info):
    '''
    Tests a `guess` equation against `all_info`, a list of known restrictions, 
    one entry in that list from each previous call to set_colors(). Returns 
    True if that `guess` complies with the collective evidence imposed by 
    `all_info`; returns False if any violation is detected. Does not check the 
    mathematical accuracy of the proposed candidate equation.
    '''
  
    move_info = []  # Stores all the statuses and positions of the character.
    greenlist = []  # Stores all the info of the moves with 'green' status
    counter = -1  # To keep track of index in the guess
    
    # The following chunk of code is used to create a list with every move,
    # including the position ('counter'), the actual character and a  
    # placeholder 'colour', based off of the guess.
    for character in guess:
        counter += 1
        move_info.append((counter, character, 'colour'))
    
    # The following is for the positional constraint.
    
    # The following chunk of code goes through each character in the guess
    # and compares it to all the information gathered thus far. If the
    # guess character is present in all the information and has the same 
    # position and has the status 'grey' or 'yellow', the function returns 
    # False as that does not pass restrictions. However, if the function has
    # status 'green', it is placed into the 'greenlist' where it is handled
    # later.
    for move in move_info:
        for info in all_info:
            for item in info:
                if item[0] == move[0] and item[1] == move[1]:
                    if item[2] == GREYY:
                        return False
                    elif item[2] == YELLO:
                        return False
                    elif item[2] == GREEN:
                        greenlist.append(item)
                        
    # This goes through all the information available. If not all 'green' 
    # status moves are present in the guess, the function returns False 
    # as it does not pass restrictions.
    for info in all_info:
        for item in info:
            if item[2] == GREEN:
                if item not in greenlist:
                    return False
    
    # The following is for distributional constraint.
        
    guess_tracker = []  # This keeps track of the guesses
    greytags = 0  # This is the number of 'grey' status characters in all_info
    
    # The following chunk of code goes through all possible FoCdle characters.
    # It tracks the status of the previous guess in all_info, counting the 
    # number  of 'grey', 'green', and 'yellow' tags it has, before placing
    # all this info into the guess_tracker.
    for character in "0123456789+-*%=":
        greencount = 0
        yellowcount = 0
        greycount = 0
        try:
            for item in all_info[-1]:
                if item[2] == GREYY:
                    greytags += 1
                if character in item and item[2] == GREEN:
                    greencount += 1
                if character in item and item[2] == YELLO:
                    yellowcount += 1
                if character in item and item[2] == GREYY:
                    greycount += 1  
        except IndexError:
            continue
        guess_tracker.append((character, greencount, yellowcount, greycount))
    
    # The following tally is used to count the number of times each character
    # appears in the guess.
    tally = {}
    for character in guess:
        if character in tally:
            tally[character] += 1
        else:
            tally[character] = 1
    
    # The following chunk of code is the actual distributional constraint.
    # Essentially, the function will return False if the the number of times
    # a character in the guess is less than the sum of that character's 'green'
    # and 'yellow' counts in the information or if the number of times a 
    # character in the guess is greater than the sum of that character's 
    # 'green' and 'yellow' counts in the information if that character has one
    # or more 'grey' tags in the information. It will also return False if the
    # number of times a character in the guess is less than the sum of that
    # character's 'green' and 'yellow' counts in the information plus the total
    # number of 'grey' tags in the information if that character doesn't have
    # any 'grey' tags in the information.
    for keys, values in tally.items():
        for possible_char in guess_tracker:
            if keys in possible_char:
                if values < possible_char[1] + possible_char[2]:
                    return False
                if possible_char[3] >= 1:
                    if values > possible_char[1] + possible_char[2]:
                        return False
                if possible_char[3] == 0:
                    if values > possible_char[1] + possible_char[2] + greytags:
                        return False
     
    # If all the conditions are met, it means that guess passes restrictions
    # and so the function returns True.
    return True

#--------------------------------------------------------------

all_info = []
guess_counter = 0

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
    inform = 'With the increased popularity of short daily puzzle games like Wordle during the pandemic, Mathdle is a similar game inspired like the previously mentioned Wordle, except coded by a solo programmer from the ground up. The objective of Wordle is to deduce a secret word by accumulation of evidence, lodging one guess at a time and being given information about how many matching characters you had, and whether they were in the right positions. There is also a well-known physical game called Mastermind that require similar deductive skills. The primary difference between this game and Wordle is that Wordle is a game in which a player guesses a random word, Mathdle is a game in which the player guesses a randomly generated equation, targeted towards people who prefer numbers over words. This game has a target string as a simple math equation of a known length (measured in characters), whereas in Wordle, the target string is a word, and each of the guesses must also be math equations of the same length.\n\nThe player will be given an option to either play the game themself and guess a randomly generated secret or they can input values to create their own secret and watch an AI solve the secret that they have created. If the player wishes to play the game themselves, they will be prompted to choose a difficulty where the number inputted corresponds to the length of the secret and therefore a greater value corresponds to a larger secret and therefore difficulty.\n\nEach cell in the Mathdle contains a single digit, or one of four possible operators “+-*%” or an “=” relationship; and the format of the Mathdle is always {value operator value operator value = result}. That is, each Mathdle always has exactly two operators, one equality, three values, and one result. Each value is an integer between 1 and 99 inclusive, expressed in the minimum number of digits (no leading zeros); and the result is an integer also expressed without any leading zeros. The four operators are “+”, “-”, “*”, “%”, all with exactly the same interpretation as in Python, and with the same precedence as in Python (“*” and “%” are carried out before either of “+” or “-”). The difficulty of a Mathdle game is measured by its length in total characters.\n\nAs you make guesses, your guess will be compared to the hidden randomly generated secret if you choose to play the game. Your guess will be printed and directly underneath the result, the information regarding the guess will be printed as well. Directly underneath each cell of your guess, there will either be a “G” representing the colour green, “g” representing the colour grey, or “Y” representing the colour yellow. If underneath the cell you see a “G”, this means that the character in that cell is correct and is a part of the secret. If underneath the cell you see a “Y”, this means that the character occupying that cell is a part of the secret at some location but not at the location that it is currently occupying. Additionally, if the same character appears again in the guess made and has the tag “g”, it means that there is only one instance of that specific character present in the secret.  If there is a “g” underneath the cell, it means that that character is not present within the secret at all. A good guess is one that makes use of all this information that is revealed from your previous guesses.\n\nYour guess does not have to be a valid equation. However, the solution to the Mathdle will always be a valid equation. For example, for a Mathdle of length five, even 12345 or +-=%* would be considered valid inputs even though they will never be the secret.\n\nAt any point throughout the game, you have a few options. You can type “quit” to exit the game at any time, type “info” to display all this information, type “guesses” to show all the guesses that you have made so far or even “guess_info” to show all the information related to the guesses that you have made so far for each individual cell or type “restart” to restart the game. Also, a normal game of Wordle will allow the player to make six guesses before the game is over and the secret is revealed. In Mathdle however, after six guesses, the play will be prompted whether or not they wish to end the game. If they wish to end the game, the secret will be revealed, otherwise they are allowed to keep guessing until they get the right answer.\n'
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

# The following is for if the player wishes to make their own game and watch an AI solve their game
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

    # The following makes the secret that the AI will solve for
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
    print("\n------------------------------------------------------------------------------------\n")
    print(f"Your choices have been computed. This is the Mathdle game that you have created: {secret}")
    print("\nThe AI will now guess the Mathdle that you have made!")
    
    # The following makes guesses, progressively getting closer to the secret each time
    AI_counter = 0
    AI_guess = "placeholder"
    AI_guesses_made = []
    print("\n------------------------------------------------------------------------------------")
    while AI_guess != secret:
        AI_guess = create_guess(all_info, difficulty=len(secret))
        AI_guesses_made.append(AI_guess)
        AI_counter += 1
        all_info.append(set_colors(secret, AI_guess))
    
    print(f"\nYour Matdhle has been solved after {AI_counter} guesses: {AI_guess}\n")
    print("Would you like to see all the guesses that the AI made?")
    while True:
        show_AI_guesses = input('Type "yes" to see or "no" to move on: ')
        if show_AI_guesses == "yes":
            print("\nHere are all the guesses that the AI made:\n")
            for i in AI_guesses_made:
                print(i)
            print("\nWould you like to play another game?")
            while True:
                end = input('Type "new" to play again or type "quit" to exit: ')
                if end == "new":
                    process = Process(target=task)
                    process.start()
                    process.join()
                    process.start()
                elif end == "quit":
                    print("\n------------------------------------------------------------------------------------")
                    print("\nThank you for playing!")
                    print("\n------------------------------------------------------------------------------------")
                    exit()
                else:
                    continue
        if show_AI_guesses == "no":
            print("\nWould you like to play another game?")
            while True:
                end = input('Type "new" to play again or type "quit" to exit: ')
                if end == "new":
                    process = Process(target=task)
                    process.start()
                    process.join()
                    process.start()
                elif end == "quit":
                    print("\n------------------------------------------------------------------------------------")
                    print("\nThank you for playing!")
                    print("\n------------------------------------------------------------------------------------")
                    exit()
                else:
                    continue
        else:
            continue

elif make_own == "random":
    print("\n------------------------------------------------------------------------------------")
    print("\nYou have chosen to play the game! Now you will need to select your difficulty.\n")
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
            process = Process(target=task)
            process.start()
            process.join()
            process.start()
    else:
        original = '#' * game_difficulty
        print("\n------------------------------------------------------------------------------------")
        print(f"\nYour Mathdle has been generated: {original}")

print('\nYou can type "quit" at any time to exit, "info" for all informtation or')
print('"guesses" to show all guesses you have made so far or even "guess_info" to')
print("show all the information related to the guesses you have made so far,")
print('or "restart" to restart the game.')

guesses_made = []
similarity_list = []
while True:
    # The following line is for if the player guessed the secret correctly
    if set(similarity_list) == {"G"}:
        break

    # If they make 6 guesses, they will be given a choice of continueing or revealing the secret.
    if guess_counter == 6:
        print("\n------------------------------------------------------------------------------------")
        print("\nYou have made six guesses. You have a choice of ending the game right now and revealing")
        print("the secret or continue guessing until you get it right!")
        while True:
            six_count = input('Type "continue" to continue the game or type "reveal" to end the game and reveal the secret: ')
            if six_count == "continue":
                break
            elif six_count == "reveal":
                print("\n------------------------------------------------------------------------------------\n")
                print("The secret will now be revealed! The secret was:")
                print(f"\n{secret}")
                print("\n------------------------------------------------------------------------------------\n")
                print("Would you like to play another game?")
                while True:
                    end = input('Type "new" to play again or type "quit" to exit: ')
                    if end == "new":
                        process = Process(target=task)
                        process.start()
                        process.join()
                        process.start()
                    elif end == "quit":
                        print("\n------------------------------------------------------------------------------------")
                        print("\nThank you for playing!")
                        print("\n------------------------------------------------------------------------------------")
                        exit()
                    else:
                        continue
            else:
                continue

    # The following code is to input the player's guess and make sure that their guess is valid
    while True:
        try:
            guess = input("\nPlease enter your guess (it must be the same length as the difficulty chosen): ")
            if guess == "quit":
                print("\n------------------------------------------------------------------------------------")
                print("\nThank you for playing!")
                print("\n------------------------------------------------------------------------------------")
                exit()
            elif guess == "guesses":
                print("\n------------------------------------------------------------------------------------\n")
                print(f"So far you have made {guess_counter} guesses! Here are the guesses you have made:\n")
                for i in guesses_made:
                    print(i)
                print("\n------------------------------------------------------------------------------------\n")
                raise ValueError
            elif guess == "guess_info":
                print("\n------------------------------------------------------------------------------------\n")
                print(all_info)
                print("\n------------------------------------------------------------------------------------\n")
                raise ValueError
            elif guess == "info":
                inform = 'With the increased popularity of short daily puzzle games like Wordle during the pandemic, Mathdle is a similar game inspired like the previously mentioned Wordle, except coded by a solo programmer from the ground up. The objective of Wordle is to deduce a secret word by accumulation of evidence, lodging one guess at a time and being given information about how many matching characters you had, and whether they were in the right positions. There is also a well-known physical game called Mastermind that require similar deductive skills. The primary difference between this game and Wordle is that Wordle is a game in which a player guesses a random word, Mathdle is a game in which the player guesses a randomly generated equation, targeted towards people who prefer numbers over words. This game has a target string as a simple math equation of a known length (measured in characters), whereas in Wordle, the target string is a word, and each of the guesses must also be math equations of the same length.\n\nThe player will be given an option to either play the game themself and guess a randomly generated secret or they can input values to create their own secret and watch an AI solve the secret that they have created. If the player wishes to play the game themselves, they will be prompted to choose a difficulty where the number inputted corresponds to the length of the secret and therefore a greater value corresponds to a larger secret and therefore difficulty.\n\nEach cell in the Mathdle contains a single digit, or one of four possible operators “+-*%” or an “=” relationship; and the format of the Mathdle is always {value operator value operator value = result}. That is, each Mathdle always has exactly two operators, one equality, three values, and one result. Each value is an integer between 1 and 99 inclusive, expressed in the minimum number of digits (no leading zeros); and the result is an integer also expressed without any leading zeros. The four operators are “+”, “-”, “*”, “%”, all with exactly the same interpretation as in Python, and with the same precedence as in Python (“*” and “%” are carried out before either of “+” or “-”). The difficulty of a Mathdle game is measured by its length in total characters.\n\nAs you make guesses, your guess will be compared to the hidden randomly generated secret if you choose to play the game. Your guess will be printed and directly underneath the result, the information regarding the guess will be printed as well. Directly underneath each cell of your guess, there will either be a “G” representing the colour green, “g” representing the colour grey, or “Y” representing the colour yellow. If underneath the cell you see a “G”, this means that the character in that cell is correct and is a part of the secret. If underneath the cell you see a “Y”, this means that the character occupying that cell is a part of the secret at some location but not at the location that it is currently occupying. Additionally, if the same character appears again in the guess made and has the tag “g”, it means that there is only one instance of that specific character present in the secret.  If there is a “g” underneath the cell, it means that that character is not present within the secret at all. A good guess is one that makes use of all this information that is revealed from your previous guesses.\n\nYour guess does not have to be a valid equation. However, the solution to the Mathdle will always be a valid equation. For example, for a Mathdle of length five, even 12345 or +-=%* would be considered valid inputs even though they will never be the secret.\n\nAt any point throughout the game, you have a few options. You can type “quit” to exit the game at any time, type “info” to display all this information, type “guesses” to show all the guesses that you have made so far or even “guess_info” to show all the information related to the guesses that you have made so far for each individual cell or type “restart” to restart the game. Also, a normal game of Wordle will allow the player to make six guesses before the game is over and the secret is revealed. In Mathdle however, after six guesses, the play will be prompted whether or not they wish to end the game. If they wish to end the game, the secret will be revealed, otherwise they are allowed to keep guessing until they get the right answer.\n'
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
                print("\nThat is all! Have fun playing MATHDLE!")
                print("\n------------------------------------------------------------------------------------")
                raise ValueError
            elif guess == "restart":
                process = Process(target=task)
                process.start()
                process.join()
                process.start()
            else:
                pass
            
            guess_list = []
            for item in guess:
                if item in DIGITS or item in EQUALITY or item in OPERATORS:
                    guess_list.append(item)
                else:
                    raise Endturn
            if len(guess_list) == len(secret):
                break
            else:
                raise Endturn
        except Endturn:
            print("Your guess is invalid.")
        except ValueError:
            pass
     
    # Now that we have our guess, we can compare the guess we made to the secret
    guess_counter += 1 #Increases the number of guesses made by 1
    similarity = set_colors(secret, guess)
    similarity_list = []
    for colour in similarity:
        if colour[-1] == GREEN:
            similarity_list.append("G")
        elif colour[-1] == YELLO:
            similarity_list.append("Y")
        elif colour[-1] == GREYY:
            similarity_list.append("g")
    
    # Print outcome of guess
    print("\n------------------------------------------------------------------------------------\n")
    print(f"For guess number {guess_counter}, here is your outcome:\n")
    print(guess)
    print(''.join(similarity_list))
    
    # Now let the player know if the guess that they made was a good one or a bad one
    good_guess = passes_restrictions(guess, all_info)
    if good_guess == True:
        print("\nThat was a good guess! Keep it up!")
    elif good_guess == False:
        print("\nNot the best guess. Better luck with the next one.")

    # Some final stuff: just add the guess to the bank of knowledge
    move = (guess, ''.join(similarity_list))
    guesses_made.append(move)
    all_info.append(set_colors(secret, guess))
    

print("\n------------------------------------------------------------------------------------\n")
print(f"Congratulations! You have solved the Mathdle after {guess_counter} guesses!")
print("The secret was:")
print(f"\n{secret}")
print("\n------------------------------------------------------------------------------------\n")
print("Would you like to play another game?")
while True:
    end = input('Type "new" to play again or type "quit" to exit: ')
    if end == "new":
        process = Process(target=task)
        process.start()
        process.join()
        process.start()
    elif end == "quit":
        print("\n------------------------------------------------------------------------------------")
        print("\nThank you for playing!")
        print("\n------------------------------------------------------------------------------------")
        exit()
    else:
        continue

