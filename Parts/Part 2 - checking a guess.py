# Created by Tuong Bao Nguyen
# Started 07/05/2023

GREEN = "green"
YELLO = "yellow"
GREYY = "grey"

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
