from tkinter import *
from Structures import Queue

root = Tk()
root.title("Queue")
root.geometry("300x300")

mqueue = Queue.Queue()

show = StringVar()
entry = StringVar()


def showL():
    show.set(mqueue)


def add():
    mqueue.insert(addEntry.get())


def fromFile(mqueue):
    mqueue.clear()
    f = open("../Files/queueFile", 'r')
    for num in f.readline().split(" "):
        mqueue.insert(float(num))

addButton = Button(root, text="добавить элемент", command=add)
addButton.place(x=0, y=0, width=150, height=50)

addEntry = Entry(root)
addEntry.place(x=150, y=0, width=150, height=50)
showButton = Button(root, text="показать список", command=showL)
showButton.place(x=0, y=50, width=150, height=50)

showButton = Button(root, text="считать из файла", command= lambda : fromFile(mqueue))
showButton.place(x=150, y=50, width=150, height=50)

showLabel = Label(root, textvariable=show)
showLabel.place(x=0, y=100, width=300, height=200)

root.mainloop()
