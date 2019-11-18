from tkinter import *
from Structures import Stack

root = Tk()
root.title("Stack")
root.geometry("300x300")

mstack = Stack.Stack()

show = StringVar()
entry = StringVar()


def add():
    mstack.push(addEntry.get())


def showS():
    show.set(mstack)





addButton = Button(root, text="добавить элемент", command=add)
addButton.place(x=0, y=0, width=150, height=50)

addEntry = Entry(root)
addEntry.place(x=150, y=0, width=150, height=50)
showButton = Button(root, text="показать стэк", command=showS)
showButton.place(x=0, y=50, width=150, height=50)

def fromFile(mstackl):
    out = ""
    mstack.clear()
    f = open("../Files/stackFile", "r")
    for line in f.readlines():
        for l in line:
            mstack.push(l)
        while mstack.size() != 0:
            out += str(mstack.pop())
        out += '\n'
    show.set(out)

showButton = Button(root, text="считать из файла", command= lambda : fromFile(mstack))
showButton.place(x=150, y=50, width=150, height=50)

showLabel = Label(root, textvariable=show)
showLabel.place(x=0, y=100, width=300, height=200)

root.mainloop()
