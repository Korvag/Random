from tkinter import *
import encodetest
window = Tk()

eord = Entry(window, text='Are you encrypting or decrypting? <E> to encrypt, <D> to decrypt, <Q> to quit:\n',bd=5)
eord.place(x=50,y=50)
eordlabel = Label(window, text='Are you encrypting or decrypting? <E> to encrypt, <D> to decrypt, <Q> to quit', fg='black',font=("Times New Roman", 12))
eordlabel.place(x=50,y=25)

data = Entry(window, text='Are you encrypting white text or a file? Enter <t> for text or <f> for a file:\n',bd=5)
data.place(x=50,y=150)
datalabel = Label(window, text='Are you encrypting white text or a file? Enter <t> for text or <f> for a file:\n', fg='black', font=('Times New Roman',12))
datalabel.place(x=50,y=100)

user = Entry(window, text='Enter the text:\n',bd=5)
user.place(x=50,y=250)
userlabel = Label(window, text='Enter the text:\n', fg='black',font=('Times New Roman',12))
userlabel.place(x=50,y=200)

file = Entry(window, text='Enter the full file path:\n',bd=5)
file.place(x=50,y=350)
filelabel = Label(window, text='Enter the full file path:\n', fg='black',font=('Times New Roman',12))
filelabel.place(x=50,y=300)


window.title('Encrypter')
window.geometry("500x500+10+10")
window.mainloop()

encodetest.main(eord,data,user,file)
