from tkinter import *

def click(event):
    global scval
    text = event.widget.cget('text')
    if text == '=':
        if scval.get().isdigit():
            value = int(scval.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                scval.set("ERROR")

                

        scval.set(value)
        screen.update()
    elif text == 'C':
        scval.set('')
        screen.update()
    else:
        scval.set(scval.get()+ text)
        screen.update()


root = Tk()

root.geometry('600x800')
scval = StringVar()
scval.set('')
screen = Entry(root,textvar=scval,font='arabic 40 bold' )
screen.pack(fill=X,ipadx=6,pady=8,padx=8)

f1 = Frame(root,bg='grey')
b1 = Button(f1,text='C',padx=15,pady=15,font='arabic 20 bold')
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind('<Button-1>',click)

b2 = Button(f1,text='l',padx=15,pady=15,font='arabic 20 bold')
b2.pack(side=LEFT,padx=18,pady=5)
b2.bind('<Button-1>',click)

b3 = Button(f1,text='%',padx=15,pady=15,font='arabic 20 bold')
b3.pack(side=LEFT,padx=18,pady=5)
b3.bind('<Button-1>',click)

b4 = Button(f1,text="/",padx=15,pady=15,font='arabic 20 bold')
b4.pack(side=LEFT,padx=18,pady=5)
b4.bind('<Button-1>',click)

f1.pack()


f2 = Frame(root,bg='grey')
b1 = Button(f2,text='7',padx=14,pady=15,font='arabic 20 bold')
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind('<Button-1>',click)

b2 = Button(f2,text='8',padx=15,pady=15,font='arabic 20 bold')
b2.pack(side=LEFT,padx=18,pady=5)
b2.bind('<Button-1>',click)

b3 = Button(f2,text='9',padx=15,pady=15,font='arabic 20 bold')
b3.pack(side=LEFT,padx=18,pady=5)
b3.bind('<Button-1>',click)

b4 = Button(f2,text='*',padx=14,pady=15,font='arabic 20 bold')
b4.pack(side=LEFT,padx=18,pady=5)
b4.bind('<Button-1>',click)
f2.pack()


f3 = Frame(root,bg='grey')
b1 = Button(f3,text='4',padx=16,pady=15,font='arabic 20 bold')
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind('<Button-1>',click)

b2 = Button(f3,text='5',padx=15,pady=15,font='arabic 20 bold')
b2.pack(side=LEFT,padx=18,pady=5)
b2.bind('<Button-1>',click)

b3 = Button(f3,text='6',padx=15,pady=15,font='arabic 20 bold')
b3.pack(side=LEFT,padx=18,pady=5)
b3.bind('<Button-1>',click)

b4 = Button(f3,text='-',padx=16,pady=15,font='arabic 20 bold')
b4.pack(side=LEFT,padx=18,pady=5)
b4.bind('<Button-1>',click)
f3.pack()


f4 = Frame(root,bg='grey')
b1 = Button(f4,text='1',padx=14,pady=15,font='arabic 20 bold')
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind('<Button-1>',click)

b2 = Button(f4,text='2',padx=15,pady=15,font='arabic 20 bold')
b2.pack(side=LEFT,padx=18,pady=5)
b2.bind('<Button-1>',click)

b3 = Button(f4,text='3',padx=15,pady=15,font='arabic 20 bold')
b3.pack(side=LEFT,padx=18,pady=5)
b3.bind('<Button-1>',click)

b4 = Button(f4,text='+',padx=14,pady=15,font='arabic 20 bold')
b4.pack(side=LEFT,padx=18,pady=5)
b4.bind('<Button-1>',click)
f4.pack()


f5 = Frame(root,bg='grey')
b1 = Button(f5,text='0',padx=54,pady=15,font='arabic 20 bold')
b1.pack(side=LEFT,padx=34,pady=5)
b1.bind('<Button-1>',click)

# b2 = Button(f5,text='2',padx=15,pady=15,font='arabic 20 bold')
# b2.pack(side=LEFT,padx=18,pady=5)
# b2.bind('<Button-1>',click)

b3 = Button(f5,text='.',padx=15,pady=15,font='arabic 20 bold')
b3.pack(side=LEFT,padx=18,pady=5)
b3.bind('<Button-1>',click)

b4 = Button(f5,text='=',padx=15,pady=15,font='arabic 20 bold')
b4.pack(side=LEFT,padx=18,pady=5)
b4.bind('<Button-1>',click)
f5.pack()


root.mainloop()