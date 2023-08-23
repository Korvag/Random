import random

while True:
    numbers = []
    total = 0
    die = input("Choose your die:  ")

    if die == "q" or die == "Q":
        break

    die = int(die)
    rolls = int(input("Choose how many times to roll:  "))

    while rolls > 0:
        number = random.randint(1,die)
        numbers.append(number)
        total += number
        rolls -= 1
    print (numbers,"\n",total,"\n")


            