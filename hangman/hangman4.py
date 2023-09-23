import os
from english_words import get_english_words_set
import random
import time


def wordgen():
    word = random.choice(list(get_english_words_set(['gcide'], lower = True)))
    word_disp = ("word:  " + "_ " * len(word))
    return (word,word_disp)



def man(count):
    scaffold = ["______\n",  "___|___\n",  "   |\n",  " o |\n",  "  __\n",  "/|\\|\n",  "/ \\|\n",  " | |\n",  "/| |\n",  "/  |\n"]
    if count == 0:
        return('\n\n\n\n\n')
    elif count == 1:
        return('\n\n\n\n' + scaffold[0])
    elif count == 2:
        return ("\n" + scaffold[2] + scaffold[2] + scaffold[2] + scaffold[1])
    elif count == 3:
        return (scaffold[4] + scaffold[2] + scaffold[2] + scaffold[2] + scaffold[1])
    elif count == 4:
        return (scaffold[4] + scaffold[3] + scaffold[2] + scaffold[2] + scaffold[1])
    elif count == 5:
        return (scaffold[4] + scaffold[3] + scaffold[7] + scaffold[2] + scaffold[1])
    elif count == 6:
        return (scaffold[4] + scaffold[3] + scaffold[8] + scaffold[2] + scaffold[1])
    elif count == 7:
        return (scaffold[4] + scaffold[3] + scaffold[5] + scaffold[2] + scaffold[1])
    elif count == 8:
        return (scaffold[4] + scaffold[3] + scaffold[5] + scaffold[9] + scaffold[1])
    elif count == 9:
        return (scaffold[4] + scaffold[3] + scaffold[5] + scaffold[6] + scaffold[1])
        

   
def guessing(word):
    letters = list(word)
    guesses = list("_" * len(word))
    guessed = []
    count = 0

    while "_" in guesses:
        if count == 9:
            break
        guess = input("Guess a letter, or 1 to quit:  ")
        if guess == '1':
            os.system("cls")
            exit()

        if guess in guessed:
            print("Already guessed.  Try again.")
            time.sleep(1)
        elif guess in letters:
            indexes = [index for (index,item) in enumerate(letters) if item == guess]
            for item in indexes:
                guesses[item] = guess
            guessed.append(guess)
        else:
            print("Wrong!")
            count += 1
            guessed.append(guess)
            time.sleep(1)

        os.system("cls")
        print(man(count))
        for item in guesses:
            print(item,end=" ")
        print()
    
    if guess == '1':
        os.system("cls")
    elif count == 9:
        print(f"\nYou lose!\nThe word was {word}")
        time.sleep(5)
    else:
        print("Congrats! You guessed the word!\n")
        time.sleep(5)
    return (guess)

        

        

def main():
    guess = '0'

    while guess != '1':
        os.system("cls")
        word,word_disp = wordgen()
        print("\n\n\n\n\n")
        print(word_disp)
        guess = guessing(word)
    os.system("cls")


if __name__ == "__main__":
    main()

