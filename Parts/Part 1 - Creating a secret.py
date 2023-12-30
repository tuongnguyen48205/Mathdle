# Created by Tuong Bao Nguyen
# Started 07/05/2023

import random

DEF_DIFFIC = 10
MAX_TRIALS = 20
MAX_VALUE = 99
OPERATORS = "+-*%"
EQUALITY = "="
DIGITS = "0123456789"
NOT_POSSIBLE = "No FoCdle found of that difficulty"

def create_secret(difficulty=DEF_DIFFIC):
    '''
    Use a random number function to create a FoCdle instance of length 
    `difficulty`. The generated equation will be built around three values 
    each from 1 to 99, two operators, and an equality.
    
    This function takes an integer argument (difficulty) and returns a FoCdle
    secret of length difficulty. It can generate for pretty much all of the 
    difficulties but since it is random, after trying MAX_TRIALS number of
    times, it will return "No Focdle found of that difficulty."
    '''
    
    attempt_counter = 0
    
    # A while loop is used to keep trying to generate a FoCdle secret that
    # meets all of the requirements. However, with the attempt counter, once
    # the function has looped through MAX_TRIALS number of times, the function
    # will return NOT_POSSIBLE ("No FoCdle found of that difficulty").
    while True:      
        attempt_counter += 1
        if attempt_counter == MAX_TRIALS:
            return NOT_POSSIBLE
        
        # A placeholder "_" is used to create a list of length 'difficulty'
        # which will make it easier to work with later on, so each character
        # in the FoCdle can just replace the placeholder.
        try:
            mylist = []
            for i in range(difficulty):
                mylist.append('_')
    
            # Since the requirements state that three values between 1 and 99
            # and two operators need to be a part of the FoCdle, the following 
            # five lines will do this.
            first_number = random.randint(1, 99)
            second_number = random.randint(1, 99)
            third_number = random.randint(1, 99)
            operator1 = random.choice(OPERATORS)
            operator2 = random.choice(OPERATORS)
            
            # The following chunks of code will replace the placeholders ("_") 
            # with the first value generated, followed by the first operator,
            # then the second value, the second operator, third value and then
            # the equals sign in order to create the FoCdle secret.
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
            # be in order to fit the difficulty/length of the FoCdle.
            available_space = 0
            for i in mylist:
                if i == "_":
                    available_space += 1
            
            # The following chunk of code firstly determines what the final
            # number must be, based off of the values and operators randomly
            # generated previously. However, more importantly, if the number
            # of digits in this final number does not equal the number of 
            # placeholders remaining or is a negative number, it means that the
            # FoCdle does not work and so the whole program will execute again
            # due to the while loop until a FoCdle is generated which meets all
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
