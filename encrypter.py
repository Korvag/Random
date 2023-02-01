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


def encrypt(z,output): 
    f=[]
    g=[]
    number,number2=password()
    for item in z:
        f.append(int((int(item) + number) * number2))

    if output == 'F' or output == 'f':
        file1 = input('Enter the file path of the file to save the encrypted data to:\n')
        with open(file1,'w') as file:
            file.close()
        with open(file1,'a') as file:
            for i in f:
                file.write(str(i)+' ')
    if output == 'T' or output == 't':
        for i in f:
            g.append(str(i)+' ')
        print(g)



def decrypt(z,output):
    f=[]
    number,number2=password()

    for item in z:
        f.append(chr(int((int(item)/number2)-number)))
    if output == 'T' or output == 't':
        for item in f:
            print(item,end='')
    if output == 'F' or output == 'f':
        file = input('Enter the full path for the file:\n')
        with open(file,'w') as file1:
            file1.close()
        with open(file,'a') as file1:
            for item in f:
                file1.write(item)
    print()


def text(user,eord,output):
    z=[]
    x=[]
    if eord == 'E' or eord == 'e':
        for letter in user:
            z.append(ord(letter))
        encrypt(z,output)
    if eord == 'D' or eord == 'd':
        z = user.split(' ')
        for item in z:
            if item != '':
                x.append(item)
        decrypt(x,output)


def extract(file,eord,output):
    with open(file,'r') as file2:
        c=[]
        b=[]
        if eord == 'E' or eord == 'e':
            for line in file2:
                c.append(str(line))
            encrypt(c,output)
        if eord == 'D' or eord == 'd':
            for line in file2:
                b = line.split(' ')
                for item in b:
                    if item != '':
                        c.append(str(item))
            decrypt(c,output)


def main():
    while True:
        eord = input('Are you encrypting or decrypting? <E> to encrypt, <D> to decrypt, <Q> to quit:\n')
        if eord == 'Q' or eord == 'q':
            break
        else:
            data = input('Are you encrypting text or a file? <T> for text or <F> for a file:\n')
            output = input('Would you like the output as text or a file? <T> for text or <F> for a file:\n')
            if data == 't':
                user = input("Enter the text:\n")
                text(user,eord,output)
            if data == 'f':
                file = input('Enter the full file path:\n')
                extract(file,eord,output)

if __name__ == '__main__':
    main()