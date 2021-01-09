"""
File: hangman.py
Name: 萬思妤
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Players have N_TURNS chances to guess the word by inputting one character each round.
    """
    answer = random_word()
    life = N_TURNS
    print('The word looks like: ', end="")
    ans = ""
    for i in range(len(answer)):
        ans += '-'
    print(ans)
    # The dashed word.
    print('Tou have '+str(N_TURNS)+' guesses left.')
    while True:
        guess = input('Your guess:')
        guess = guess.upper()
        if guess.isalpha():
            if len(guess) > 1:
                print('Illegal format')
            else:
                if answer.find(guess) != -1:
                    # When users guess correctly.
                    print('You are correct!')
                    c = ""
                    for i in range(len(answer)):
                        if ans.isalpha():
                            # When users figure out the word.
                            print('You win!!')
                            print('The word was: '+str(ans))
                        else:
                            if ans[i].isalpha():
                                # Copy the character that users already guessed correctly.
                                c += ans[i]
                            else:
                                if guess == answer[i]:
                                    # Add the new character that users guessed correctly.
                                    c += answer[i]
                                else:
                                    c += '-'
                    ans = c
                    if ans.isalpha():
                        print('You win!!')
                        print('The word was: ' + str(ans))
                        break
                    else:
                        print('The word looks like: '+str(ans))
                        print('You have '+str(life)+' guesses left.')
                elif answer.find(guess) == -1:
                    # When users guess wrong.
                    life -= 1
                    print('There is no '+str(guess)+'\'s in the word.')
                    print('The word looks like: '+str(ans))
                    print('You have '+str(life)+' guesses left.')
        else:
            print('Illegal format')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
