from tkinter import*
from tkinter import ttk

import random

#function to close main window
def quit():
    main_window.destroy()

def add_customer():
    enter_name.get()
    name_letter = enter_name.get().isalpha()
    itembox.get()
    itemtext = str(itembox.get())
    intnum = int(numbox.get())
    if name_letter == False or itemtext == "" or itemtext == "Select/enter item" or intnum == 0 or intnum > 500:
        newWindow = Toplevel(main_window)

        #prevents user from interacting with main window until error message is closed
        #so they dont create more windows
        newWindow.grab_set()
        #will this work with a newer window created from a new window?
        
        def ok():
            newWindow.destroy()
        Button(newWindow, text="ok", command=ok, width = 3).grid(row= 3)

    #name check
    if name_letter == False:
        enter_name.delete(0,"end")
        Label(newWindow,text= "please enter valid name",width = 20).grid(row=0)

    #item check
    if itemtext == "" or itemtext == "Select/enter item":
        Label(newWindow,text= "please choose an item",width = 20).grid(row=1)

    #item number check
    if intnum == 0 or intnum > 500:
        Label(newWindow,text= "please enter valid number",width = 20).grid(row=2)
        
    elif name_letter == True and itemtext != "" or itemtext != "Select/enter item" and intnum != 0 or intnum <= 500:
        #adds name to list (append)
        recipt = random.randint(1000,9999)
        customers.append([enter_name.get(), itembox.get(), numbox.get(), recipt])
        entered_count["entries"] +=1


def print_entry():
    new_window = Toplevel(main_window)

    Label(new_window, text="#",).grid(row=0, column=4)
    Label(new_window, text="name",).grid(row=0, column=5)
    Label(new_window, text="Hired item",).grid(row=0, column=6)
    Label(new_window, text="no of",).grid(row=0, column=7)
    Label(new_window, text="recipt",).grid(row=0, column=8)

    x = 0
    row = 1
    while x < entered_count["entries"]:
    
        #prints customer info in GUI
        Label(new_window,text= customers[x][0],width = 10).grid(row=row, column=5)
        Label(new_window,text= customers[x][1],width = 10).grid(row=row, column=6)
        Label(new_window,text= customers[x][2],width = 5).grid(row=row, column=7, sticky= W)
        Label(new_window,text= customers[x][3],width = 5).grid(row=row, column=8 , sticky= E)
        Label(new_window,text= x+1,width = 2).grid(row=row, column=4)

        

        #adds number
        x +=1
        row +=1

        a = 1
        
def delete():
    
    dele = int(delete_item.get())
    dele-=1
    
    del customers[int(dele)]
    
    x = entered_count["entries"]
    entered_count["entries"]-=1
    delete_item.delete(0,"end")

    bg_colour1 = "MediumPurple"
    
    dele+=2

    #removes entry
    print_entry()
    Label(main_window, text="-",width = 1).grid(row=x, column=4)
    Label(main_window, text="-",width = 10).grid(row=x, column=5)
    Label(main_window, text="-",width = 10).grid(row=x, column=6)
    Label(main_window, text="-",width = 5).grid(row=x, column=7, sticky= W)
    Label(main_window, text="-",width = 5).grid(row=x, column=8, sticky= E)
    
        
#functions in main window (buttons)   
def main():    
    Label(main_window, text="Party Hire Store",).grid(row=0, column=1)
    
    Button(main_window, text="quit", command=quit, width = 3).grid(row=0, column=0, sticky= W)

    Button(main_window, text="print",command=print_entry, width = 5).grid(row=4, column=0, padx=30)

    Button(main_window, text="register customer",command=add_customer, width = 14).grid(row=4, column=1, sticky= W)    

    Label(main_window, text="name",).grid(row=1, column=0)
    Label(main_window, text="Hired item",).grid(row=2, column=0)
    Label(main_window, text="no of",).grid(row=3, column=0)

    Label(main_window, text="", width = 5).grid(row=5, column=0)

    Label(main_window, text="row #", bg="red").grid(row=8, column=0, sticky=W)

    Button(main_window, text="delete", command=delete, width = 6).grid(row=8, column=0,padx=40)
    


main_window = Tk()   

enter_name = Entry(main_window)
enter_name.grid(row=1, column=1)

items = ["balloons", "lights", "chairs", "tables", "pack 1", "pack 2", "pack 3"]
itembox = ttk.Combobox(main_window, values = items, width = 17)
itembox.grid(row=2,column=1)
itembox.set("Select/enter item")

numbox = Spinbox(main_window, from_=0, to=500, width = 8)
numbox.grid(row=3,column=1, sticky = W)

customers = []
entered_count = {"entries":0}

delete_item = Entry(main_window, width = 2)
delete_item.grid(row=8, column=1, sticky = W)

alive = [0]

main()

#first enter name
#then select an item or enter an item
#then choose number of item
#then confirm details

#put register details in new window
