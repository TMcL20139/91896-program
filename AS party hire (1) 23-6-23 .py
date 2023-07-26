from tkinter import*
from tkinter import ttk

import random

#function to close main window
def quit():
    main_window.destroy()

def add_customer():
    #adds name to list (append)
    recipt = random.randint(1000,9999)
    
    customers.append([enter_name.get(), recipt])
    enter_name.delete(0,"end")
    entered_count["entries"] +=1
    

#choose an item
def item1():
    recipt = random.randint(1000,9999)
    customers.append([enter_name.get(), "Ballons", recipt])
    enter_name.delete(0,"end")
    entered_count["entries"] +=1

def item_num():
    Label(main_window,text= w.get(),width = 10).grid(row=6, column=1)
    
def print_entry():
    x = 0
    row = 1
    while x < entered_count["entries"]:
    

        #prints students name in gui
        Label(main_window,text= customers[x][0],width = 10).grid(row=row, column=5)
        Label(main_window,text= customers[x][1],width = 10).grid(row=row, column=6)
        Label(main_window,text= customers[x][2]).grid(row=row, column=7)
        Label(main_window,text= x+1,width = 2).grid(row=row, column=4)

        #adds number
        x +=1
        row +=1

def delete():
    
    dele = int(delete_item.get())
    dele-=1
    
    del customers[int(dele)]
    
    x = entered_count["entries"]
    entered_count["entries"]-=1
    delete_item.delete(0,"end")

    bg_colour1 = "MediumPurple"
    
    dele+=2
    
    print_entry()
    Label(main_window, text="-----",width = 1).grid(row=x, column=4)
    Label(main_window, text="-----",width = 10).grid(row=x, column=5)
    
        
#functions in main window (buttons)   
def main():
    bg_colour1 = "MediumPurple"
    Button(main_window, text="delete", command=delete, width = 5).grid(row=5, column=0,padx=40)
    
    Button(main_window, text="quit", command=quit, width = 3).grid(row=0, column=0, sticky= W)

    Button(main_window, text="print",command=print_entry, width = 5).grid(row=0, column=0, padx=30)

    Button(main_window, text="number", command=item_num, width = 5).grid(row=6, column=2, padx=30)
      

    Label(main_window, text="name", bg=bg_colour1).grid(row=1, column=0)

    Label(main_window, text="row #", bg="red").grid(row=5, column=0, sticky=W)
    


main_window = Tk()
w = Spinbox(main_window, from_=0, to=500)
w.grid(row=6,column=0)
items = ["ballons", "lights", "chairs", "tables"]
itembox = ttk.Combobox(main_window, values = items)
itembox.grid(row=7,column=0)
customers = []
entered_count = {"entries":0}
enter_name = Entry(main_window)
enter_name.grid(row=1, column=1)
delete_item = Entry(main_window, width = 2)
delete_item.grid(row=5, column=1, sticky = W)

main()

#first enter name
#then select an item or enter an item
#then choose number of item
#then confirm details

#details are printed out in a list of customers
