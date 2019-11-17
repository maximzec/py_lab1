from tkinter import *
from Structures import List



root = Tk()
root.title("List")
root.geometry("300x300")

mlist = List.List()


show = StringVar()
entry = StringVar()

def showL():
    show.set(mlist)
    print(mlist.print() ," ", addEntry.get())


def add():
    addEntry.update()
    mlist.addToEnd(List.Node(addEntry.get()))


addButton = Button(root, text = "добавить элемент" , command = add)
addButton.place(x=0,y=0, width = 150 , height = 50)

addEntry = Entry(root )
addEntry.place(x=150,y=0,width=150,height=50)
showButton = Button(root , text = "показать список" , command = showL)
showButton.place(x=0,y=50,width=150,height=50)

showButton = Button(root , text = "считать из файла")
showButton.place(x=150,y=50,width=150,height=50)


showLabel = Label(root, textvariable = show )
showLabel.place(x=0,y=100,width=150,height=200)


root.mainloop()