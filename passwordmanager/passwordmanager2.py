user = input("Enter the account:  ")
password = input("Input the password: ")

print (user,password)


def password():
    password = input('Enter the encryption password:\n')
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