import os
from english_words import get_english_words_set
import random
import time

while True:
    
    word = random.choice(list(get_english_words_set(['gcide'], lower = True)))
    os.system("cls")

    print ("word:  " + "_ " * len(word))

    letters = list(word)
    guesses = list("_" * len(word))

    guessed = []

    count = 0
    scaffold = ["______\n","___|___\n","   |\n"," * |\n","  __\n","/|\\|\n","/ \\|\n"]

    while "_" in guesses:
        
        if count == 1:
            print()
            print(scaffold[0])
        elif count == 2:
            print ()
            print ("\n",scaffold[2],scaffold[2],scaffold[2],scaffold[1])
        elif count == 3:
            print ()
            print (scaffold[4],scaffold[2],scaffold[2],scaffold[2],scaffold[1])
        elif count == 4:
            print ()
            print (scaffold[4],scaffold[3],scaffold[2],scaffold[2],scaffold[1])
        elif count == 5:
            print ()
            print (scaffold[4],scaffold[3],scaffold[5],scaffold[2],scaffold[1])
        elif count == 6:
            print ()
            print (scaffold[4],scaffold[3],scaffold[5],scaffold[6],scaffold[1])
            print ("You Lose!")
            print (f"The word was {word}")
            break

        guess = input("guess a letter or 1 to quit:  ")
        if guess == '1':
            break


        if guess in guessed:
            print("Already guessed, try again.")
        elif guess in letters:
            indexes = [index for (index,item) in enumerate(letters) if item == guess]
            for item in indexes:
                guesses[item] = guess
            guessed.append(guess)
        else:
            print("Wrong")
            count += 1
            guessed.append(guess)


        for item in guesses:
            print(item,end = " ")
        print ()
    if guess == '1':
        break
    else:
        print("Congrats! You got the word\n")
        time.sleep(5)