from tkinter import *

window=Tk()
window.geometry("295x375")
window.title('Calculator')
window.resizable(False,False)

e= Entry(window,width=340)
e.place(x=0,y=0,height=90)


def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

def add():
    n1 = e.get()
    global math
    global i
    math= 'addittion'
    i = int(n1)
    e.delete(0,END)
def Sub():
    n1 = e.get()
    global math
    global i
    math= 'Subtraction'
    i = int(n1)
    e.delete(0,END)

def Mul():
    n1 = e.get()
    global math
    global i
    math= 'Multiplication'
    i = int(n1)
    e.delete(0,END)
def Div():
    n1 = e.get()
    global math
    global i
    math= 'Division'
    i = int(n1)
    e.delete(0,END)
def Eq():
    n2 = e.get()
    e.delete(0,END)

    if math == 'addittion':
        e.insert(0,i+int(n2))
    elif math=='Subtraction':
        e.insert(0,i-int(n2))
    elif math=='Multiplication':
        e.insert(0,i*int(n2))
    elif math=='Division':
        e.insert(0,i/int(n2))
def clear():
    e.delete(0,END)





button1= Button(window,text='1',command=lambda:click(1))
button1.place(x=5,y=90,width=75,height=75)
button2= Button(window,text='2',command=lambda:click(2))
button2.place(x=75,y=90,width=75,height=75)
button3= Button(window,text='3',command=lambda:click(3))
button3.place(x=145,y=90,width=75,height=75)
operator1= Button(window,text='+',command=lambda:add())
operator1.place(x=215,y=90,width=75,height=75)

button4= Button(window,text='4',command=lambda:click(4))
button4.place(x=5,y=160,width=75,height=75)
button5= Button(window,text='5',command=lambda:click(5))
button5.place(x=75,y=160,width=75,height=75)
button6= Button(window,text='6',command=lambda:click(6))
button6.place(x=145,y=160,width=75,height=75)
operator2= Button(window,text='-',command=lambda:Sub())
operator2.place(x=215,y=160,width=75,height=75)

button7= Button(window,text='7',command=lambda:click(7))
button7.place(x=5,y=230,width=75,height=75)
button8= Button(window,text='8',command=lambda:click(8))
button8.place(x=75,y=230,width=75,height=75)
button9= Button(window,text='9',command=lambda:click(9))
button9.place(x=145,y=230,width=75,height=75)
operator3= Button(window,text='x',command=lambda:Mul())
operator3.place(x=215,y=230,width=75,height=75)

button0= Button(window,text='0',command=lambda:click(0))
button0.place(x=5,y=300,width=75,height=75)
operator4= Button(window,text='/',command=lambda:Div())
operator4.place(x=75,y=300,width=75,height=75)
operator5= Button(window,text='=',command= lambda:Eq())
operator5.place(x=145,y=300,width=75,height=75)
operator6= Button(window,text='clear',command=clear)
operator6.place(x=215,y=300,width=75,height=75)


window.mainloop()