import tkinter as tk
from tkinter import *
from time import gmtime, strftime
import os

#Please read EULA

filename2 = ("./Orders/TotalOrders/Items.txt")
with open(filename2, "w+") as f2b:
    f2b.write("")
    #f2b.write("Total Items: \n\n")

totalOrder=[]
def resetAllMenus():
    
    item1.set("None")
    item1size.set("Normal")
    quantity1.set("0")
    row1S.set(0)
    row1V.set(0)
    
    item2.set("None")
    item2size.set("Normal")
    quantity2.set("0")
    row2S.set(0)
    row2V.set(0)
    
    item3.set("None")
    item3size.set("Normal")
    quantity3.set("0")
    row3S.set(0)
    row3V.set(0)
    
    item4.set("None")
    item4size.set("Normal")
    quantity4.set("0")
    row4S.set(0)
    row4V.set(0)
    
    item5.set("None")
    item5size.set("Normal")
    quantity5.set("0")
    row5S.set(0)
    row5V.set(0)
    
    nameEntryBox.delete(0, 'end')
    
    workOutTotal()

def addFinalOrder():
    global totalOrder
    if nameEntryBox.get() != "":
        workOutTotal()
        totalPrice = (float(item1Total()) + float(item2Total()) + float(item3Total()) + float(item4Total()) + float(item5Total()))
        currentTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        totalOrder = [[nameEntryBox.get(),totalPrice,currentTime],[item1.get(),quantity1.get(),item1size.get(),row1S.get(),row1V.get()],[item2.get(),quantity2.get(),item2size.get(),row2S.get(),row2V.get()],[item3.get(),quantity3.get(),item3size.get(),row3S.get(),row3V.get()],[item4.get(),quantity4.get(),item4size.get(),row4S.get(),row4V.get()],[item5.get(),quantity5.get(),item5size.get(),row5S.get(),row5V.get()]]

        resetAllMenus()
        addToFile()


def spaceCreator(string,when):
    if when == 0:
        comparison=45
    elif when == 1:
        comparison=10
        
    exactNumberOfSpaces=(":")
    spaceNumber=comparison-(int(len(string)))
    x = exactNumberOfSpaces.ljust(spaceNumber)
        
    return (x)
    
def addToFile():
    global totalOrder
    stop=False
    
    filename = ("./Orders/" + str(totalOrder[0][0]) + ".txt")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("TOTAL ORDER:\n\n")
        f.write(str(totalOrder[0][0]) + "     "  + str(totalOrder[0][2]) + "     " + str(totalOrder[0][1]) + "\n\n")
        for i in range(0,len(totalOrder)):# Makes sure not to write items with "none" or quantity of "0" to be added to file \/
            if (totalOrder[(i)][0] != "None") and (totalOrder[(i)][1] != "0") and (i != 0): 
                if (totalOrder[i][0] == "Chips - £1.90 --> £2.70") or (totalOrder[i][0] == "Half Chips - £1.35") or (totalOrder[i][0] == "Cheesy Chips - £2.85 --> £3.65"):
                    if totalOrder[i][3] == "1":
                        salt = " Salt"
                    elif totalOrder[i][3] == "0":
                        salt = " No Salt"

                    if totalOrder[i][4] == "1":
                        vinegar = " Vinegar"
                    elif totalOrder[i][4] == "0":
                        vinegar = " No Vinegar"

                    totalOrder[i][0] = str(str(totalOrder[i][0]) + str(vinegar) + str(salt))
                        
                f.write(str(totalOrder[(i)][0]) + str(spaceCreator(str(totalOrder[(i)][0]),0))  + str(totalOrder[(i)][2]) + str(spaceCreator(str(totalOrder[(i)][2]),1)) + str(totalOrder[(i)][1]) + ":\n")
                print(totalOrder[i])            
    f.close
    
    filename2 = ("./Orders/TotalOrders/Items.txt")
    os.makedirs(os.path.dirname(filename2), exist_ok=True)
    with open(filename2, "r+") as f2:
        data = []
        for i in range(0,len(totalOrder)):
            if (totalOrder[(i)][0] != "None") and (totalOrder[(i)][1] != "0") and (i != 0):
                foodToAdd= (str(totalOrder[(i)][0]) + str(spaceCreator(str(totalOrder[(i)][0]),0))  + str(totalOrder[(i)][2]) + str(spaceCreator(str(totalOrder[(i)][2]),1)) + str(totalOrder[(i)][1]) + ":\n")
                #print(foodToAdd)
                foodToAdd = [x.strip(' ') for x in foodToAdd]
                #print (foodToAdd)
                foodToAdd=''.join(foodToAdd)
                #print (foodToAdd)
                data.append(foodToAdd)
        f2.close

    with open(filename2, "a") as f2b:
        f2b.writelines( data )
        f2b.close

    with open(filename2, "r+") as f2c:
        lines = [line.rstrip('\n') for line in f2c]
        lengthOfFile=len(lines)
        for i in range(0,lengthOfFile):
            for n in range(0,lengthOfFile):
                l1=((lines[i].split(':'))[0])
                l2=((lines[n].split(':'))[0])

                l1a=((lines[i].split(':'))[1])
                l2a=((lines[n].split(':'))[1])
                
                if (l1 == l2) and (l1a == l2a) and (i != n ) and (stop==False):
                    fixRepeats(i,n,lines)
                    stop=True
    f2c.close
    
def fixRepeats(i,n,lines):
    with open(filename2, "a") as f2b:
        newtotal=0
        oldA=((lines[i].split(':'))[2])
        oldB=((lines[n].split(':'))[2])
        newTotal=((int(oldB))+(int(oldA)))
        newString=str(str((lines[i].split(':'))[0]) + ":" + str((lines[i].split(':'))[1]) + ":" + str(newTotal) + "\n")
        f2b.writelines( newString )
    f2b.close

    f = open(filename2, "r")
    allFileData = f.readlines()
    f.close()

    f = open(filename2, "w")
    print(lines[i])
    print(allFileData)
    allFileData.remove(lines[i] + "\n")
    allFileData.remove(lines[n] + "\n")
    print(allFileData)

    for c in range(0,len(allFileData)):
        f.write(allFileData[c])
    f.close()


def finalExport():
    toWrite=[]
    with open(filename2, "r+") as f2c:
        lines = [line.rstrip('\n') for line in f2c]
        lengthOfFile=len(lines)
        for i in range(0,lengthOfFile):
            l1=((lines[i].split(':'))[0])

            l1a=((lines[i].split(':'))[1])

            l1b=((lines[i].split(':'))[2])
                
            print(lines)
            print("")
            print(l1)
            print(l1a)
            print(l1b)

            toWrite.append(str(l1) + str(spaceCreator(str(l1),0)) + str(l1a) + str(spaceCreator(str(l1a),0)) + str(l1b) + "\n")
            print(toWrite)
    f2c.close()
    
    f = open(filename2, "w")
    for c in range(0,len(toWrite)):
        f.write(toWrite[c])
    f.close()
    
def numberMultiplier(x,y):
    value = ((float(x))*(float(y)))
    return (value)
   
  
def workOutTotal():
    total = (float(item1Total()) + float(item2Total()) + float(item3Total()) + float(item4Total()) + float(item5Total()))
    totalNumber.config(text=str("%.2f " % total))
    ###Next stage work out wrap total

root = tk.Tk()

defaultWidth=30

backgroundImagePath="./bg.gif"
backgroundImage=tk.PhotoImage(file=backgroundImagePath)
backgroundLabel= tk.Label(root, image=backgroundImage)
backgroundLabel.grid(column=0,row=0,columnspan=15)

lineImagePath="./line.gif"
lineImage=tk.PhotoImage(file=lineImagePath)
lineLabel= tk.Label(root, image=lineImage)
lineLabel.grid(column=0,row=1,columnspan=15)

lineLabel2= tk.Label(root, image=lineImage)
lineLabel2.grid(column=0,row=8,columnspan=15)

lineLabel3= tk.Label(root, image=lineImage)
lineLabel3.grid(column=0,row=8,columnspan=15)

verticalLinePath="./vline.gif"
verticalImage=tk.PhotoImage(file=verticalLinePath)
verticalImageItem= tk.Label(root, image=verticalImage)
verticalImageItem.grid(column=1,row=1,rowspan=6)

verticalImageItem2= tk.Label(root, image=verticalImage)
verticalImageItem2.grid(column=3,row=1,rowspan=6)
#
nameLabel=tk.Label(root, text="Name: ",font = "Calibri 20")
nameLabel.grid(row=7,column=0,columnspan=2)

nameEntryBox = tk.Entry(root)
nameEntryBox.grid(row=7,column=2)

totalLabel=tk.Label(root, text="Total: ",font = "Calibri 20 bold")
totalLabel.grid(row=7,column=4)

totalNumber=tk.Label(root, text=(" 0.0 "),font = "Calibri 20")
totalNumber.grid(row=7,column=5,columnspan=2)

totalbutton = tk.Button(root, text="Click to Work Out Total",font = "Calibri 20", command=workOutTotal)
totalbutton.grid(row=7,column=8,columnspan=3,padx = 20)

addOrderButton = tk.Button(root, text="Click to add final order",font = "Calibri 20", command=addFinalOrder)
addOrderButton.grid(row=7,column=12,columnspan=3)
###########

row1S = StringVar(value = 0)
row1V = StringVar(value = 0)
c1 = Checkbutton(root,text = "Salt",var = row1S)
c2 = Checkbutton(root,text = "Vinegar",var = row1V)
c1.grid(row=2,column = 0)
c2.grid(row=2,column = 2)

row2S = StringVar(value = 0)
row2V = StringVar(value = 0)
c3 = Checkbutton(root,text = "Salt",var = row2S)
c4 = Checkbutton(root,text = "Vinegar",var = row2V)
c3.grid(row=3,column = 0)
c4.grid(row=3,column = 2)

row3S = StringVar(value = 0)
row3V = StringVar(value = 0)
c5 = Checkbutton(root,text = "Salt",var = row3S)
c6 = Checkbutton(root,text = "Vinegar",var = row3V)
c5.grid(row=4,column = 0)
c6.grid(row=4,column = 2)

row4S = StringVar(value = 0)
row4V = StringVar(value = 0)
c7 = Checkbutton(root,text = "Salt",var = row4S)
c8 = Checkbutton(root,text = "Vinegar",var = row4V)
c7.grid(row=5,column = 0)
c8.grid(row=5,column = 2)

row5S = StringVar(value = 0)
row5V = StringVar(value = 0)
c9 = Checkbutton(root,text = "Salt",var = row5S)
c10 = Checkbutton(root,text = "Vinegar",var = row5V)
c9.grid(row=6,column = 0)
c10.grid(row=6,column = 2)

###########
def item1Total():
    ss=item1.get()
    ssize=item1size.get()
    sq=quantity1.get()
    rt=0.00

    if (ss == ("Chip Butty - £1.80")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.80,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.80,sq))
    elif (ss == ("Chips - £1.90 --> £2.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.90,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.70,sq))
    elif (ss == ("Half Chips - £1.35")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.35,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.35,sq))
    elif (ss == ("Cheesy Chips - £2.85 --> £3.65")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.85,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.65,sq))
    elif (ss == ("Plain Sausage - £1.15 --> £1.55")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.15,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.55,sq))
    elif (ss == ("Battered Sausage - £1.30 --> £1.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.30,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.70,sq))
    elif (ss == ("Mushrooms - £2.00")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.00,sq))
    elif (ss == ("Saveloy - £1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.60,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("Buttered Roll - £0.50")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(0.50,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(0.50,sq))
    elif (ss == ("Mushy Peas Sauce - £1.20 --> 1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("Beans - £1.20 --> £1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("4 Chicken Nuggets - £2.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.70,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.70,sq))
    elif (ss == ("Cod - £3.80 --> £4.50")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(3.80,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.50,sq))
    elif (ss == ("1/4lb Beefburger - £2.90")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.90,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.90,sq))
    elif (ss == ("1/4lb Cheeseburger - £3.00")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(3.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.00,sq))
    elif (ss == ("Curry Sauce - £1.20 --> 1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    return(rt)



item1 = tk.StringVar(root)
item1.set("None")
item1s=["None","","Chips - £1.90 --> £2.70","Half Chips - £1.35","Cheesy Chips - £2.85 --> £3.65","Plain Sausage - £1.15 --> £1.55","Battered Sausage - £1.30 --> £1.70",
        "Mushrooms - £2.00","Saveloy - £1.60","Buttered Roll - £0.50","Mushy Peas Sauce - £1.20 --> 1.60","Beans - £1.20 --> £1.60","Curry Sauce - £1.20 --> 1.60",
        "4 Chicken Nuggets - £2.70","Cod - £3.80 --> £4.50","1/4lb Beefburger - £2.90","1/4lb Cheeseburger - £3.00","Chip Butty - £1.80"]
item1Options = tk.OptionMenu(root, item1, *item1s)
item1Options.grid(row=2,column=4)
item1Options.config(width=defaultWidth)

quantity1 = tk.StringVar(root)
quantity1.set("0")
quantities1=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
quantityOptions1 = tk.OptionMenu(root, quantity1, *quantities1)
quantityOptions1.grid(row=2,column=8)
quantityOptions1.config(width=defaultWidth)

item1size = tk.StringVar(root)
item1size.set("Normal")
item1sizes=["Normal","Large"]
item1sizeOptions = tk.OptionMenu(root, item1size, *item1sizes)
item1sizeOptions.grid(row=2,column=12)
item1sizeOptions.config(width=defaultWidth)
#
item2 = tk.StringVar(root)
item2.set("None")
item2Options = tk.OptionMenu(root, item2, *item1s)
item2Options.grid(row=3,column=4)
item2Options.config(width=defaultWidth)

quantity2 = tk.StringVar(root)
quantity2.set("0")
quantities2=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
quantityOptions2 = tk.OptionMenu(root, quantity2, *quantities2)
quantityOptions2.grid(row=3,column=8)
quantityOptions2.config(width=defaultWidth)

item2size = tk.StringVar(root)
item2size.set("Normal")
item2sizes=["Normal","Large"]
item2sizeOptions = tk.OptionMenu(root, item2size, *item2sizes)
item2sizeOptions.grid(row=3,column=12)
item2sizeOptions.config(width=defaultWidth)
#
item3 = tk.StringVar(root)
item3.set("None")
item3Options = tk.OptionMenu(root, item3, *item1s)
item3Options.grid(row=4,column=4)
item3Options.config(width=defaultWidth)

quantity3 = tk.StringVar(root)
quantity3.set("0")
quantities3=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
quantityOptions3 = tk.OptionMenu(root, quantity3, *quantities3)
quantityOptions3.grid(row=4,column=8)
quantityOptions3.config(width=defaultWidth)

item3size = tk.StringVar(root)
item3size.set("Normal")
item3sizes=["Normal","Large"]
item3sizeOptions = tk.OptionMenu(root, item3size, *item3sizes)
item3sizeOptions.grid(row=4,column=12)
item3sizeOptions.config(width=defaultWidth)
#
item4 = tk.StringVar(root)
item4.set("None")
item4Options = tk.OptionMenu(root, item4, *item1s)
item4Options.grid(row=5,column=4)
item4Options.config(width=defaultWidth)

quantity4 = tk.StringVar(root)
quantity4.set("0")
quantities4=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
quantityOptions4 = tk.OptionMenu(root, quantity4, *quantities4)
quantityOptions4.grid(row=5,column=8)
quantityOptions4.config(width=defaultWidth)

item4size = tk.StringVar(root)
item4size.set("Normal")
item4sizes=["Normal","Large"]
item4sizeOptions = tk.OptionMenu(root, item4size, *item4sizes)
item4sizeOptions.grid(row=5,column=12)
item4sizeOptions.config(width=defaultWidth)
#
item5 = tk.StringVar(root)
item5.set("None")
item5Options = tk.OptionMenu(root, item5, *item1s)
item5Options.grid(row=6,column=4)
item5Options.config(width=defaultWidth)

quantity5 = tk.StringVar(root)
quantity5.set("0")
quantities5=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
quantityOptions5 = tk.OptionMenu(root, quantity5, *quantities5)
quantityOptions5.grid(row=6,column=8)
quantityOptions5.config(width=defaultWidth)

item5size = tk.StringVar(root)
item5size.set("Normal")
item5sizes=["Normal","Large"]
item5sizeOptions = tk.OptionMenu(root, item5size, *item5sizes)
item5sizeOptions.grid(row=6,column=12)
item5sizeOptions.config(width=defaultWidth)

def generic():
    print("Generic")
    
def exitProgram():
    root.destroy()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=resetAllMenus)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitProgram)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Export Final List", command=finalExport)
menubar.add_cascade(label="Final Export", menu=editmenu)

def item2Total():
    ss=item2.get()
    ssize=item2size.get()
    sq=quantity2.get()
    rt=0.00

    if (ss == ("Chip Butty - £1.80")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.80,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.80,sq))
    elif (ss == ("Chips - £1.90 --> £2.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.90,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.70,sq))
    elif (ss == ("Half Chips - £1.35")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.35,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.35,sq))
    elif (ss == ("Cheesy Chips - £2.85 --> £3.65")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.85,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.65,sq))
    elif (ss == ("Plain Sausage - £1.15 --> £1.55")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.15,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.55,sq))
    elif (ss == ("Battered Sausage - £1.30 --> £1.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.30,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.70,sq))
    elif (ss == ("Mushrooms - £2.00")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.00,sq))
    elif (ss == ("Saveloy - £1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.60,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("Buttered Roll - £0.50")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(0.50,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(0.50,sq))
    elif (ss == ("Mushy Peas Sauce - £1.20 --> 1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("Beans - £1.20 --> £1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("4 Chicken Nuggets - £2.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.70,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.70,sq))
    elif (ss == ("Cod - £3.80 --> £4.50")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(3.80,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.50,sq))
    elif (ss == ("1/4lb Beefburger - £2.90")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.90,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.90,sq))
    elif (ss == ("1/4lb Cheeseburger - £3.00")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(3.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.00,sq))
    elif (ss == ("Curry Sauce - £1.20 --> 1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    return(rt)


def item3Total():
    ss=item3.get()
    ssize=item3size.get()
    sq=quantity3.get()
    rt=0.00

    if (ss == ("Chip Butty - £1.80")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.80,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.80,sq))
    elif (ss == ("Chips - £1.90 --> £2.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.90,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.70,sq))
    elif (ss == ("Half Chips - £1.35")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.35,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.35,sq))
    elif (ss == ("Cheesy Chips - £2.85 --> £3.65")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.85,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.65,sq))
    elif (ss == ("Plain Sausage - £1.15 --> £1.55")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.15,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.55,sq))
    elif (ss == ("Battered Sausage - £1.30 --> £1.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.30,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.70,sq))
    elif (ss == ("Mushrooms - £2.00")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.00,sq))
    elif (ss == ("Saveloy - £1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.60,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("Buttered Roll - £0.50")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(0.50,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(0.50,sq))
    elif (ss == ("Mushy Peas Sauce - £1.20 --> 1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("Beans - £1.20 --> £1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("4 Chicken Nuggets - £2.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.70,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.70,sq))
    elif (ss == ("Cod - £3.80 --> £4.50")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(3.80,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.50,sq))
    elif (ss == ("1/4lb Beefburger - £2.90")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.90,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.90,sq))
    elif (ss == ("1/4lb Cheeseburger - £3.00")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(3.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.00,sq))
    elif (ss == ("Curry Sauce - £1.20 --> 1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    return(rt)


def item4Total():
    ss=item4.get()
    ssize=item4size.get()
    sq=quantity4.get()
    rt=0.00

    if (ss == ("Chip Butty - £1.80")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.80,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.80,sq))
    elif (ss == ("Chips - £1.90 --> £2.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.90,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.70,sq))
    elif (ss == ("Half Chips - £1.35")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.35,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.35,sq))
    elif (ss == ("Cheesy Chips - £2.85 --> £3.65")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.85,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.65,sq))
    elif (ss == ("Plain Sausage - £1.15 --> £1.55")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.15,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.55,sq))
    elif (ss == ("Battered Sausage - £1.30 --> £1.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.30,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.70,sq))
    elif (ss == ("Mushrooms - £2.00")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.00,sq))
    elif (ss == ("Saveloy - £1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.60,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("Buttered Roll - £0.50")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(0.50,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(0.50,sq))
    elif (ss == ("Mushy Peas Sauce - £1.20 --> 1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("Beans - £1.20 --> £1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("4 Chicken Nuggets - £2.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.70,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.70,sq))
    elif (ss == ("Cod - £3.80 --> £4.50")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(3.80,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.50,sq))
    elif (ss == ("1/4lb Beefburger - £2.90")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.90,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.90,sq))
    elif (ss == ("1/4lb Cheeseburger - £3.00")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(3.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.00,sq))
    elif (ss == ("Curry Sauce - £1.20 --> 1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    return(rt)

def item5Total():
    ss=item5.get()
    ssize=item5size.get()
    sq=quantity5.get()
    rt=0.00

    if (ss == ("Chip Butty - £1.80")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.80,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.80,sq))
    elif (ss == ("Chips - £1.90 --> £2.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.90,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.70,sq))
    elif (ss == ("Half Chips - £1.35")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.35,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.35,sq))
    elif (ss == ("Cheesy Chips - £2.85 --> £3.65")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.85,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.65,sq))
    elif (ss == ("Plain Sausage - £1.15 --> £1.55")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.15,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.55,sq))
    elif (ss == ("Battered Sausage - £1.30 --> £1.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.30,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.70,sq))
    elif (ss == ("Mushrooms - £2.00")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.00,sq))
    elif (ss == ("Saveloy - £1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.60,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("Buttered Roll - £0.50")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(0.50,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(0.50,sq))
    elif (ss == ("Mushy Peas Sauce - £1.20 --> 1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("Beans - £1.20 --> £1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    elif (ss == ("4 Chicken Nuggets - £2.70")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.70,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.70,sq))
    elif (ss == ("Cod - £3.80 --> £4.50")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(3.80,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.50,sq))
    elif (ss == ("1/4lb Beefburger - £2.90")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(2.90,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(2.90,sq))
    elif (ss == ("1/4lb Cheeseburger - £3.00")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(3.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.00,sq))
    elif (ss == ("Curry Sauce - £1.20 --> 1.60")):
        if ssize == "Normal":
            rt=rt+(numberMultiplier(1.20,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.60,sq))
    return(rt)


# display the menu
root.config(menu=menubar)
root.title("Chip Shop Ordering System")

root.mainloop()
#http://effbot.org/tkinterbook/entry.htm
