from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("600x600")
root.title('notepad')
root.config(bg='lightblue')
root.resizable(False,False)

def save_file():
    print('')

def open_file():
    print("")

b1 = Button(root,width='20',height='2', bg='#fff',text='save file',command=save_file).place(x=100,y=5)
b1 = Button(root,width='20',height='2', bg='#fff',text='open file',command=open_file).place(x=300,y=5)


entry = Text(root,height='33',width='72',wrap=WORD)
entry.place(x=10,y=60)

root.mainloop()

