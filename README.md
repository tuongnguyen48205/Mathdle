# Mathdle
A game created in the coding language of Python

Information:

With the increased popularity of short daily puzzle games like Wordle during the pandemic, Mathdle is a similar game inspired like the previously mentioned Wordle, except coded by a solo programmer from the ground up. The objective of Wordle is to deduce a secret word by accumulation of evidence, lodging one guess at a time and being given information about how many matching characters you had, and whether they were in the right positions. There is also a well-known physical game called Mastermind that require similar deductive skills. The primary difference between this game and Wordle is that Wordle is a game in which a player guesses a random word, Mathdle is a game in which the player guesses a randomly generated equation, targeted towards people who prefer numbers over words. This game has a target string as a simple math equation of a known length (measured in characters), whereas in Wordle, the target string is a word, and each of the guesses must also be math equations of the same length. 

The player will be given an option to either play the game themself and guess a randomly generated secret or they can input values to create their own secret and watch an AI solve the secret that they have created. If the player wishes to play the game themselves, they will be prompted to choose a difficulty where the number inputted corresponds to the length of the secret and therefore a greater value corresponds to a larger secret and therefore difficulty. 

Each cell in the Mathdle contains a single digit, or one of four possible operators “+-*%” or an “=” relationship; and the format of the Mathdle is always {value operator value operator value = result}. That is, each Mathdle always has exactly two operators, one equality, three values, and one result. Each value is an integer between 1 and 99 inclusive, expressed in the minimum number of digits (no leading zeros); and the result is an integer also expressed without any leading zeros. The four operators are “+”, “-”, “*”, “%”, all with exactly the same interpretation as in Python, and with the same precedence as in Python (“*” and “%” are carried out before either of “+” or “-”). The difficulty of a Mathdle game is measured by its length in total characters.

For example, here is a trace

As you make guesses, your guess will be compared to the hidden randomly generated secret if you choose to play the game. Your guess will be printed and directly underneath the result, the information regarding the guess will be printed. Directly underneath each cell of your guess, there will either be a “G” representing the colour green, “g” representing the colour grey, or “Y” representing the colour yellow. If underneath the cell you see a “G”, this means that…

Your guess does not have to be a valid equation…

At any point throughout the game, you have a few options. You can type “quit” to exit the game at any time, type “info” to display all this information, type “guesses” to show all the guesses that you have made so far or even “guess_info” to show all the information related to the guesses that you have made so far for each individual cell or type “restart” to restart the game.

That is all! Have fun playing Mathdle!
