'''
q = []
q.append

print("Initial queue is:",q)

def Enqueue():
    name=input("Add Name: ")
    q.append(name)
    print ("you been added to ben's queuue")

def dequeue():
'''
'''
from tkinter import *





f=open(r"C:\Users\SERN_INTERN\Documents\python\item_cost.txt", "r")
f=(f.read())
f=f.replace(" ", "_")
f=f.split()




def listBox(grocery):
    for i in range(len(grocery)):
        item = grocery[i][0]
        quantity = grocery[i][1]
        item_cost = grocery[i][2]
        theList.insert(END, f"{item} - {quantity} (Cost: ${item_cost})")
        


def listIndex(grocery, item):
    index = -1
    for i in range(len(grocery)):
        if grocery[i][0] == item:
            index = i
            break
    return index



def addList(grocery, item, quantity, cost):
    index = listIndex(grocery, item)
    item_cost = cost * quantity
    if index == -1:
        grocery.append([item, quantity, item_cost])
        print(grocery)
    else:
        grocery[index][1] += quantity
        grocery[index][2] += item_cost
    total_cost.set(total_cost.get() + item_cost)

def removeList(grocery, index):
    item_cost = grocery[index][2]
    total_cost.set(total_cost.get() - item_cost)
    del grocery[index]

def add():
    try:
        item_name = item.get()
        item_quantity = quantity.get()
        item_cost = cost.get()
        addList(grocery, item_name, item_quantity, item_cost)
        theList.delete(0, END)
        listBox(grocery)
    except ValueError:
        return

def remove():
    index = theList.index(ACTIVE)
    removeList(grocery, index)
    theList.delete(index)

    


root = Tk()
grocery = []
total_cost = DoubleVar()
total_cost.set(sum(item[2] for item in grocery))

root.title("Ben's Queue")
root.geometry("300x300")


theList = Listbox(selectmode=SINGLE, width=30)
theList.grid(row=0, column=2, columnspan=2, sticky=E)
listBox(grocery)

item = StringVar()
quantity = IntVar()
cost = DoubleVar()

Label(text="Name:").grid(row=1, column=1, sticky=E)
Entry(textvariable=item).grid(row=1, column=2, sticky=W, ipadx=30)

Label(text=":").grid(row=2, column=1, sticky=E)
Entry(textvariable=quantity).grid(row=2, column=2, sticky=W, ipadx=30)

Label(text="Cost:").grid(row=3, column=1, sticky=E)
Entry(textvariable=cost).grid(row=3, column=2, sticky=W, ipadx=30)

Button(text="Add", command=add).grid(row=4, column=2, columnspan=2, sticky=E)
Button(text="Remove", command=remove).grid(row=0, column=4, sticky=W,)

Label(text="Total Cost:").grid(row=5, column=1, sticky=E)
Label(textvariable=total_cost).grid(row=5, column=2, sticky=E)

Button(text="Done", command=root.destroy).grid(row=7,column=2, sticky=S)




root.mainloop()
'''

