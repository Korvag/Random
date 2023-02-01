import random

bot_count = 0
user_count = 0

print('First to 10 wins is the champion, or you can quit if you\'re a coward!')

while user_count <10 or bot_count <10:
    user = input('R for rock, P for paper, S for scissors, or q to quit:\n').lower()
    bot = random.randint(1,3)

    if user == 'q':
        break

    if bot == 1:
        bot1 = 'r'
    elif bot == 2:
        bot1 = 'p'
    elif bot == 3:
        bot1 = 's'

    if (user == 'r' and bot1 == 'r') or (user == 'p' and bot1 == 'p') or (user == 's' and bot1 == 's'):
        print ('I chose ',bot1)
        print ('It\'s a tie!')
        print ('I have ',bot_count,'wins and you have ',user_count,'wins\n\n')
    elif (user == 'r' and bot1 == 's') or (user == 'p' and bot1 == 'r') or (user == 's' and bot1 == 'p'):
        print ('I chose ',bot1)
        print('You win!')
        user_count += 1
        print ('I have ', bot_count, 'wins, and you have ', user_count, 'wins\n\n')
    elif (user == 'r' and bot1 == 'p') or (user == 'p' and bot1 == 's') or (user == 's' and bot1 == 'r'):
        print ('I chose ',bot1)
        print('I win!')
        bot_count += 1
        print ('I have ', bot_count, 'wins, and you have ', user_count, 'wins\n\n')
    elif user != 'r' or user != 'p' or user != 's':
        print ('Invalid option, please choose again')


if user_count > bot_count:
    print ('You have the most wins! Congratulations!')
elif bot_count > user_count:
    print ('I have the most wins - You lose!')
else:
    print ('We tied!')

print('\n\n')