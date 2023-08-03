from tkinter import*
from tkinter import ttk

import tkinter as tk, tkinter.font as tk_font

import random

#function to close main window
def quit():
    main_window.destroy()

def add_customer():
    first_name.get()
    name_letter = first_name.get().isalpha()
    last_name.get()
    last_name_letter = last_name.get().isalpha()
    itembox.get()
    itemtext = str(itembox.get())
    numbox.get()
    textnum = numbox.get().isnumeric()
    if textnum == True:
        intnum = int(numbox.get())
        #make a window
        if name_letter == False or last_name_letter == False or itemtext == "" or itemtext == "Select/enter item" or intnum == 0 or intnum > 500:
            new_window = Toplevel(main_window)

        #prevents user from interacting with main window until error message is closed
        #so they dont create more windows
            new_window.grab_set()
        #will this work with a newer window created from a new window?
            def ok():
                new_window.destroy()
            Button(new_window, text="ok", command=ok, width = 3).grid(row= 3)

    if textnum == False:
        if name_letter == False or last_name_letter == False or itemtext == "" or itemtext == "Select/enter item" or textnum == False:
            new_window = Toplevel(main_window)
            new_window.grab_set()

            def ok2():
                new_window.destroy()
            Button(new_window, text="ok", command=ok2, width = 3).grid(row= 3)

    #name check
    if name_letter == False or last_name_letter == False:
        first_name.delete(0,"end")
        last_name.delete(0, "end")
        Label(new_window,text= "please enter valid name",width = 20).grid(row=0)

    #item chec
    if itemtext == "" or itemtext == "Select/enter item":
        Label(new_window,text= "please choose an item",width = 20).grid(row=1)

    #item number check
    if textnum == False:
        Label(new_window,text= "please enter number",width = 20).grid(row=2)
    if textnum == True:
        intnum = int(numbox.get())
        if intnum == 0 or intnum > 500:
            Label(new_window,text= "please enter valid number",width = 20).grid(row=2)
    #add integer checker

    if name_letter == True and last_name_letter == True and itemtext != "" and itemtext != "Select/enter item" and textnum == True and intnum != 0 and intnum <= 500:
        #outcome prints first customer (without name)
        #fix add last name check
        #adds name to list (append)
        recipt = random.randint(1000,9999)
        customers.append([first_name.get(), last_name.get(), itembox.get(), numbox.get(), recipt])
        entered_count["entries"] +=1
            

def print_entry():

    Label(main_window, text="#", font = ("verdana",10, "bold"), bg=bg2, fg=fg).grid(row=0, column=4)
    Label(main_window, text="name",font = ("verdana",10, "bold"), bg=bg2, fg=fg).grid(row=0, column=5)
    Label(main_window, text="Hired item",font = ("verdana",10, "bold"), bg=bg2, fg=fg).grid(row=0, column=7)
    Label(main_window, text="no of",font = ("verdana",10, "bold"), bg=bg2, fg=fg).grid(row=0, column=8)
    Label(main_window, text="recipt",font = ("verdana",10, "bold"), bg=bg2, fg=fg).grid(row=0, column=9)

    x = 0
    row = 1
    while x < entered_count["entries"]:
    
        #prints customer info in GUI
        Label(main_window,text= customers[x][0],width = 5, font = font, bg=bg2, fg=fg).grid(row=row, column=5)
        Label(main_window,text= customers[x][1],width = 10, font = font, bg=bg2, fg=fg).grid(row=row, column=6)
        Label(main_window,text= customers[x][2],width = 10, font = font, bg=bg2, fg=fg).grid(row=row, column=7)
        Label(main_window,text= customers[x][3],width = 5, font = font, bg=bg2, fg=fg).grid(row=row, column=8, sticky= W)
        Label(main_window,text= customers[x][4],width = 5, font = font, bg=bg2, fg=fg).grid(row=row, column=9 , sticky= E)
        Label(main_window,text= x+1,width = 2, font = font, bg=bg2, fg=fg).grid(row=row, column=4)

        #adds number
        x +=1
        row +=1

        a = 1
 
def delete():
        dele = int(delete_item.get())
        if dele > entered_count["entries"]:
            print("no")
        elif dele <= entered_count["entries"]:
            print("yes")

            dele-=1

            delete_item.delete(0,"end")
            del customers[int(dele)]
            x = entered_count["entries"]
            entered_count["entries"]-=1
            delete_item.delete(0,"end")
            dele+=2

            #removes entry
            print_entry()
            Label(main_window, text="-",width = 1).grid(row=x, column=4)
            Label(main_window, text="-",width = 10).grid(row=x, column=5)
            Label(main_window, text="-",width = 10).grid(row=x, column=6)
            Label(main_window, text="-",width = 10).grid(row=x, column=7)
            Label(main_window, text="-",width = 5).grid(row=x, column=8, sticky= W)
            Label(main_window, text="-",width = 5).grid(row=x, column=9, sticky= E)
    
        
#functions in main window (buttons)   
def main():
    Label(main_window, text="Party Hire Store", font = ("verdana",15, "bold"), height = 2, bg=bg2 , fg=fg).grid(row=0, column=1)
    
    Button(main_window, text="quit", command=quit, font = font, width = 3, bg=bg3, fg=fg).grid(row=0, column=0, sticky= W)

    Label(main_window, text=" ",bg=bg2).grid(row=5, column=0)

    Button(main_window, text="print",command=print_entry, width = 5, font = font, bg=bg3, fg=fg).grid(row=6, column=0, padx=30)

    Button(main_window, text="add customer",command=add_customer, width = 14, font = font, bg=bg3, fg=fg).grid(row=6, column=1, sticky= W)    

    Label(main_window, text="first name",  font = font, bg=bg2, fg=fg).grid(row=1, column=0)
    Label(main_window, text="last name",  font = font, bg=bg2, fg=fg).grid(row=2, column=0)
    Label(main_window, text=" ",bg=bg2, fg=fg).grid(row=3, column=0)
    Label(main_window, text="item", font = font, bg=bg2, fg=fg).grid(row=4, column=0)

    Label(main_window, text="", width = 5, font = font, bg=bg2).grid(row=7, column=0)

    Label(main_window, text="row #", bg="red", font = font, fg=fg).grid(row=8, column=0, sticky=W)

    Button(main_window, text="delete", command=delete, width = 6, font = font, bg = bg3, fg=fg).grid(row=8, column=0,padx=40)

font = ("verdana",9)
#courier"MS Serif"mario64


#bg= "slateblue" background
#bg2 = "aquamarine" foreground
#bg3 ="cyan" button
bg="grey45"
bg2 = "grey22"
bg3 ="grey33" #dark theme
fg = "white"

main_window = Tk()
main_window.configure(bg=bg2)

first_name = Entry(main_window, width = 20, font = font, bg=bg, fg=fg)
first_name.grid(row=1, column=1, sticky = W)
last_name = Entry(main_window, width = 20, font = font, bg=bg,fg=fg)
last_name.grid(row=2, column=1, sticky = W)

items = ["balloons", "lights", "chairs", "tables", "costume", "pack 2", "pack 3"]
itembox = ttk.Combobox(main_window, values = items, width = 15, font = font)
itembox.grid(row=4,column=1, sticky = W)
itembox.set("Select/enter item")
style = ttk.Style()
style.theme_use('clam')
# ,foreground="white"
style.configure('TCombobox', fieldbackground = bg, background= bg3, fg=fg ,foreground="white", buttonbackground =bg3)

# bg=bg, buttonbackground =bg3,
numbox = Spinbox(main_window, from_=0, to=500, width = 5, font = font, bg=bg, fg=fg, buttonbackground =bg3)
numbox.grid(row=4,column=2, sticky = W)

customers = []
entered_count = {"entries":0}

#, fg="white"
delete_item = Entry(main_window, width = 2, font = font, bg=bg, fg=fg)
delete_item.grid(row=8, column=1, sticky = W)
#do checker to check for not number

main()

#first enter name
#then select an item or enter an item
#then choose number of item
#then confirm details

#put register details in new window

