num = int(input('Enter the number of rows in the triangle:  '))
print()
j=1

while j <= num:
    if j == 1:
        print(j,'  ',' '*(num-1),"*"*(j))
    else:
        if num >= 2 < 10:
            print(j,'  ',' '*(num-j+1),"*"*(j+j-1))
        elif num >= 10 < 100:
            print(j,' '*(num-j),"*"*(j+j-1))
        elif num >= 100:
            print(j,' '*(num-j),"*"*(j+j-1))
        #else:
            #print(j,'  ',' '*(num-j),"*"*(j+j-1))
    j+=1
print()