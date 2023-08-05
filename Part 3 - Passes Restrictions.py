# Created by Tuong Bao Nguyen
# Started 08/05/2023

GREEN = "green"
YELLO = "yellow"
GREYY = "grey"

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
                
     
