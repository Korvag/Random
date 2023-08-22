import encryptionmod


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split('|')
            print ('User:',user,'| Password:',fer.decrypt(passw.encode()).decode())


def add(number,number2,mode):
    name = input('Account Name:  ')
    pwd = input('Password:  ')
    encryptionmod.text(pwd,mode)

    with open ('password.txt','a') as f:
        f.write(name + '|' + str((int(pwd) + number) * number2) + '\n')


def main():
    password = input('What is the master password?  ')
    number,number2 = encryptionmod.password(password)
    while True:
        mode = input('Would you like to add a new password, or view existing passwords?  (add, view, q to quit)  ').lower()
        if mode == 'q':
            break

        if mode == 'add':
            add(number,number2,mode)
        elif mode == 'view':
            view(number,number2)
        else:
            print('That\'s not an option')



if __name__ == '__main__':
    main()

