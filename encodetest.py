from tkinter import *
window = Tk()

def password():
    password = str(input('Enter the encryption password:\n'))
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


def encrypt(z): 
    file1 = str(input('Enter the file path of the file to save the encrypted data to:\n')) 
    with open(file1,'w') as file:
        file.close()
    f=[]
    number,number2=password()
    with open(file1,'a') as file:
        for item in z:
            f.append(int((int(item) + number) * number2))
        for i in f:
            file.write(str(i)+' ')



def decrypt(z):
    f=[]
    g=[]
    number,number2=password()
    
    for item in z:
        f.append(chr(int((int(item)/number2)-number)))
    for item in f:
        print(item,end='')
    print()


def text(user,eord):
    z=[]
    x=[]
    if eord == 'E' or eord == 'e':
        for letter in user:
            z.append(ord(letter))
        encrypt(z)
    if eord == 'D' or eord == 'd':
        z = user.split(' ')
        for item in z:
            if item != '':
                x.append(item)
        decrypt(x)


def extract(file,eord):
    with open(file,'r') as file2:
        c=[]
        b=[]
        if eord == 'E' or eord == 'e':
            for line in file2:
                c.append(str(line))
            encrypt(c)
        if eord == 'D' or eord == 'd':
            for line in file2:
                b = line.split(' ')
                for item in b:
                    if item != '':
                        c.append(str(item))
            decrypt(c)


def main(w,x,y,z):
    while True:
        eord = Entry(window, text='Are you encrypting or decrypting? <E> to encrypt, <D> to decrypt, <Q> to quit:\n',bd=5)
        eord.place(x=50,y=50)
        eordlabel = Label(window, text='Are you encrypting or decrypting? <E> to encrypt, <D> to decrypt, <Q> to quit', fg='black',font=("Times New Roman", 12))
        eordlabel.place(x=50,y=25)
        if eord == 'Q' or eord == 'q':
            break
        else:
            data = str(x)
            if data == 't':
                user = str(y)
                text(user,eord)
            if data == 'f':
                file = str(z)
                extract(file,eord)

if __name__ == '__main__':
    main()