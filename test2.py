import random

user = input('Choose X or O:  \n')
if user == 'X' or user == 'x':
    bot = 'O'
    if user == 'x':
        user = 'X'
else:
    bot = 'X'

spaces = [' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ']
exclude = [0,1,2,3,4,5,6,7,8]

while True:
    print('\n', spaces[0], '|', spaces[1], '|', spaces[2], '\n----------------\n', spaces[3], '|', spaces[4], '|', spaces[5], '\n----------------\n', spaces[6], '|', spaces[7], '|', spaces[8],'\n')

    option = int(input('Choose a space: ')) -1 
    spaces[option] = ' '+user+' '
    exclude.remove(option)
    print(spaces,'\n',exclude)
    
    option2 = random.choice(list(exclude))
    print ("Your opponent chooses " + str(option2+1))
    spaces[option2] = ' '+bot+' '
    exclude.remove(option2)
    print(spaces,'\n',exclude)


    if spaces[0:3] == f' {user} | {user} | {user} ' or spaces[3:6] == f' {user} | {user} | {user} ' or spaces[6:] == f' {user} | {user} | {user} ':
        print('You win!')
        break
    elif spaces[0] == f' {user} ' and spaces[4] == f' {user} ' and spaces[8] == f' {user} ':
        print('You win!')
        break
    elif spaces[2] == f' {user} ' and spaces[4] == f' {user} ' and spaces[6] == f' {user} ':
        print('You win!')
        break
    elif spaces[0:3] == f' {bot} | {bot} | {bot} ' or spaces[3:6] == f' {bot} | {bot} | {bot} ' or spaces[6:] == f' {bot} | {bot} | {bot} ':
        print('I win!')
        break
    elif spaces[0] == f' {bot} ' and spaces[4] == f' {bot} ' and spaces[8] == f' {bot} ':
        print('I win!')
        break
    elif spaces[2] == f' {bot} ' and spaces[4] == f' {bot} ' and spaces[6] == f' {bot} ':
        print('I win!')
        break
    