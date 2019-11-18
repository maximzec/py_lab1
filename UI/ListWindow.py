from tkinter import *
from Structures import List

mlist = List.List()





def fromFile(mlist):
    mlist.clear()
    f = open("../Files/listFile", 'r')
    for num in f.readline().split(" "):
        mlist.addToEnd(List.Node(num))




def showL():
    show.set(mlist)


def add():
    mlist.addToEnd(List.Node(entry.get()))

root = Tk()
root.title("List")
root.geometry("300x300")
show = StringVar()
entry = StringVar()


addButton = Button(root, text="добавить элемент", command= add)
addButton.place(x=0, y=0, width=150, height=50)

addEntry = Entry(root , textvariable = entry)
addEntry.place(x=150, y=0, width=150, height=50)
showButton = Button(root, text="показать список", command=  showL)
showButton.place(x=0, y=50, width=150, height=50)

showButton = Button(root, text="считать из файла" , command = lambda : fromFile(mlist))
showButton.place(x=150, y=50, width=150, height=50)

showLabel = Label(root, textvariable=show)
showLabel.place(x=0, y=100, width=300, height=200)

root.mainloop()
