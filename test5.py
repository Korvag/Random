#!/usr/bin/python3

import socket

host = socket.gethostname()
ip = socket.gethostbyname(host)
ip2 = ip.split('.')
index = 0

def copy():
    file = str(input('Enter the file to copy: '))
    file2 = str(input('Enter the file to copy to: '))
    with open(file,'r') as f:
        with open(file2,'a') as g:
            for line in f:
                g.write(line)


def encrypt():
    file = str(input('Enter the full path of the file to encrypt: '))
    file3 = str(input('Enter the full path of the file for the encrypted contents:  '))
    with open(file3,'w') as v:
        v.write('\n')
        v.close()
    with open (file,'r') as file1:
        for letter in file1:
            z=[]
            a = str(letter)
            b = list(letter.encode('ascii'))
            for i in b:
                z.append(int(i))
        
            c = []
            d = []
            e = []
            f = []

            for i in z:
                c.append(i + int(ip2[0]))
            for j in c:
                d.append(j + int(ip2[1]))
            for k in d:
                e.append(k + int(ip2[2]))
            for l in e:
                f.append(str(l + int(ip2[3])))
            with open(file3,'a') as file2:
                for item in f:
                    file2.write(item + '\n')
    with open(file,'w') as q:
        q.write('\n')
        q.close()

def decrypt():
    print()
    file1 = str(input('Enter the full path for the file to decrypt:  '))
    with open (file1,'r') as file:
        z = []
        for k in file:
            if k != '\n':
                z.append(int(k))
            a=[]
            b=[]
            c=[]
            d=[]
            for e in z:
                a.append(int(e) - int(ip2[3]))
            for f in a:
                b.append(int(f) - int(ip2[2]))
            for g in b:
                c.append(int(g) - int(ip2[1]))
            for h in c:
                d.append(int(h) - int(ip2[0]))

        for i in d:
            j = chr(i)
            print(j, end="")
    print()

def main():
    while True:
        print()
        user = str(input("E to encrypt, d to decrypt, c to copy, q to quit:  "))

        if user == 'E'  or user == 'e':
            encrypt()
        elif user == 'd' or user == 'D':
            decrypt()
        elif user == 'c' or user == 'C':
            copy()
        elif user == 'q' or user == 'Q':
            break
        else:
            print('that is not an option')

main()
