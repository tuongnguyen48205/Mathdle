# Created by Tuong Bao Nguyen

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