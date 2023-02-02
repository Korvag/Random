def password(password):
    b=[]
    number=0
    number2=1

    if len(password) % 2 == 0:
        pass
    else:
        password = password + 'a'
    for l in password:
        b.append(str(ord(l)))

    a=int(len(password))/2
    c=int(len(password))
    d=b[0:int(a)]
    e=b[int(a):int(c)]

    for item in d:
        number += int(item)
    for item in e:
        number2 = number2 * int(item)
    return(number,number2)


def add(c,d):
    a=[]
    name = input('What is the account name?\n')
    pwd = input('What is the password?\n')

    for l in pwd:
        a.append(str(ord(l)))

    with open ('password.txt','a') as f:
        f.write('\n')
        f.write(name + '|')
        for l in a:
            f.write(str((int(l) + c) * d))
        f.write(str(len(a)))
        

def decrypt(f):
    index = 0
    iteration = 0
    a=[]
    b=[]
    result = ''
    data = f.rstrip()
    user,pwd = data.split('|')

    length = int(((int(len(pwd)) - 1)/int(pwd[-1])))
    pwd = pwd[0:(len(pwd)-1)]
    a.append(pwd)
            
    while iteration < (int(len(pwd))/int(length)):
        result = (pwd[index:(index+length)] + ' ')
        index += length
        iteration += 1
        b.append(result.strip(' '))
    return(user,b)



def view(c,d):
    account = input('Which account are you looking for? all for all accounts, account name for specific account:\n')
    with open ('password.txt','r') as f:
        for line in f.readlines():
            if account.lower() == 'all':
                user,b = decrypt(line)
            elif line.startswith(account):
                user,b = decrypt(line)

            print(user, '| ', end ='')
            for item in b:
                print(chr((int(item) // d) - c), end = '')
            print('\n')
    print('\n\n')




def main():
    master_pwd = input('What is the master password?\n')
    a,b = password(master_pwd)

    while True:
        mode = input('Do you want to add or view a password?  add, view, or q to quit:\n').lower()
        print('\n')
        if mode == 'q':
            break

        if mode == 'add':
            add(a,b)
        elif mode == 'view':
            view(a,b)
        else:
            print('That\'s not an option')


if __name__ == '__main__':
    main()