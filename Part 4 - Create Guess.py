# Created by Tuong Bao Nguyen
# Started 14/05/2023

import random
from hidden import solve_FoCdle

ENABLE_PLAYTEST = True
DEF_DIFFIC = 10
POSSIBLE_CHARACTER = "+-*%0123456789="
GREEN = "green"
YELLO = "yellow"
GREYY = "grey"

# secret = "25+4*12=73"

def create_guess(all_info, difficulty=DEF_DIFFIC):
    '''
    Takes information built up from past guesses that is stored in `all_info`, 
    and uses it as guidance to generate a new guess of length `difficulty`.
    '''
    
    # A placeholder "_" is used to create a list of length 'difficulty'
    # which will make it easier to work with later on, so each character
    # in the FoCdle can just replace the placeholder.
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
    # the placeholder "_" are replaced with a possible FoCdle character
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



# Let's play a game of FoCdle... below we pass your `create_guess` function to
# our hidden `solve_FoCdle` function, which uses it to guess the secret in a
# game of FoCdle. This closely follows the program outline described in task 3.
# You may also call `solve_FoCdle` with `debug=True` to see printed information
# that corresponds with comments in that same outline. 
# 
# Note: When you click "Mark", the `solve_FoCdle` function is run 100 times
# with "25+4*12=73" as the secret, taking the average number of guesses
# required to solve it. The hidden assessment tests will use many different
# random secrets, so make sure you test your code beyond this example!

if ENABLE_PLAYTEST:  # Set to True to run this code when clicking "Run" in Grok
    secret = "25+4*12=73"
    nguesses, final_guess = solve_FoCdle(secret, create_guess, debug=False)
    print(f"Solved the FoCdle after {nguesses} guesses: '{final_guess}'")
