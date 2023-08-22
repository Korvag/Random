import os

def scaffold(count,word):

    noose = ''
    scaffold = ["______\n","___|___\n","   |\n"," * |\n","  __\n","/|\\|\n","/ \\|\n"]

    if count == 1:
        noose = ('\n' + scaffold[0])
    elif count == 2:
        noose = ('\n' + scaffold[2] + scaffold[2] + scaffold[2] + scaffold[1])
    elif count == 3:
        noose = ('\n' + scaffold[4] + scaffold[2] + scaffold[2] + scaffold[2] + scaffold[1])
    elif count == 4:
        noose = ('\n' + scaffold[4] + scaffold[3] + scaffold[2] + scaffold[2] + scaffold[1])
    elif count == 5:
        noose = ('\n' + scaffold[4] + scaffold[3] + scaffold[5] + scaffold[2] + scaffold[1])
    elif count == 6:
        noose = ('\n' + scaffold[4] + scaffold[3] + scaffold[5] + scaffold[6] + scaffold[1] + f"\nYou lose!\nThe word was {word}")
    return (noose)


def guess_word():
        word = input("word to be guessed:  ")
        os.system("cls")
        dashes = ("word:  " + ("_ " * len(word)))
        return (word,dashes)

def guess_letter(letters,guesses):
    guess = input("guess a letter:  ")
    if guess in letters:
        indexes = [index for (index,item) in enumerate(letters) if item == guess]
        for item in indexes:
            guesses[item] = guess
    else:
        print("wrong")
        count += 1

    for item in guesses:
        print(item,end = " ")
    print ()






def main():

    while True:
        count = 0 


        word,dashes = guess_word()
        if word == "q" or word == "Q":
            break
        else: print (dashes)

        letters = list(word)
        guesses = list("_" * len(word))

        guess_letter(letters,guesses)
        noose = scaffold(count,word)
        print (noose)

        
main()