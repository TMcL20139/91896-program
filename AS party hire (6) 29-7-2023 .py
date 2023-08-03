from tkinter import*
from tkinter import ttk

import tkinter as tk, tkinter.font as tk_font

import random

#function to close main window
def quit():
    main_window.destroy()

#adds users customer inputs to a list
def add_customer():
    first_name.get()
    #checks first name is in letters
    name_letter = first_name.get().isalpha()
    last_name.get()
    #checks last name is in letters
    last_name_letter = last_name.get().isalpha()
    itembox.get()
    #converts the item number input from integer to string 
    itemtext = str(itembox.get())
    numbox.get()
    #checks if the item number input is a number
    textnum = numbox.get().isnumeric()
    #if the item number is a number and doesent contain any symbols or caracters or isint blank
    if textnum == True:
        intnum = int(numbox.get())
        # if the users input is not accepted, the names inputs contains numbers or symbols, or the number is out of range of 500, or the entrys have been lefts blank or untouched
        if name_letter == False or last_name_letter == False or itemtext == "" or itemtext == "Select/enter item" or intnum == 0 or intnum > 500:
            #makes a window. this window displays an error message showing that one of the users inputs is not acepted giving the user infomation so they can fix the error
            new_window = Toplevel(main_window)

        #prevents user from interacting with main window until error message is closed so they dont create more windows or interact with the main window
            new_window.grab_set()
        #closes new window
            def new_window_close():
                new_window.destroy()
            Button(new_window, text="ok", command=new_window_close, width = 3).grid(row= 3)

    #if the item number input is not a number 
    if textnum == False:
        # if the users input is not accepted, the names inputs contains numbers or symbols, or the number is out of range of 500, or the entrys have been lefts blank or untouched        
        if name_letter == False or last_name_letter == False or itemtext == "" or itemtext == "Select/enter item" or textnum == False:
            #makes a window. this window displays an error message showing that one of the users inputs is not acepted giving the user infomation so they can fix the error
            new_window = Toplevel(main_window)
            #prevents user from interacting with main window until error message is closed so they dont create more windows or interact with the main window
            new_window.grab_set()
            #closes new window
            def new_window_close():
                new_window.destroy()
            Button(new_window, text="ok", command=new_window_close, width = 3).grid(row= 3)

    #stops name inputs if it is not in letters
    if name_letter == False or last_name_letter == False:
        #removes what is in the name entry box
        first_name.delete(0,"end")
        last_name.delete(0, "end")
        Label(new_window,text= "please enter valid name",width = 20).grid(row=0)

    #stops item input if it is not acceptable
    if itemtext == "" or itemtext == "Select/enter item":
        Label(new_window,text= "please choose an item",width = 20).grid(row=1)
        ##removes what is in the item entry box
        itembox.delete(0, "end")

    #stops item number if it not under 500
    if textnum == False:
        Label(new_window,text= "please enter number",width = 20).grid(row=2)
    if textnum == True:
        intnum = int(numbox.get())
        if intnum == 0 or intnum > 500:
            Label(new_window,text= "please enter valid number",width = 20).grid(row=2)
    #textnum variabe is meant to check if the item number input is a number or integer
    #intnum converts the item number input into an integer so it can be checked if the input is a valid number between 1 and 500

    #adds inputs to customer list (append)
    if name_letter == True and last_name_letter == True and itemtext != "" and itemtext != "Select/enter item" and textnum == True and intnum != 0 and intnum <= 500:
        #genrates a random number for a recipt number
        recipt = random.randint(1000,9999)
        customers.append([first_name.get(), last_name.get(), itembox.get(), numbox.get(), recipt])
        #adds number to entered count to chek how many customer entries have been entered
        entered_count["entries"] +=1
            
#prints out and displayes the users inputs
def print_entry():
    #tells you what the info is supposed to be

    Label(main_window, text="#", font = ("verdana",10, "bold"), bg=bg2, fg=fg).grid(row=0, column=4)
    Label(main_window, text="name",font = ("verdana",10, "bold"), bg=bg2, fg=fg).grid(row=0, column=5)
    Label(main_window, text="Hired item",font = ("verdana",10, "bold"), bg=bg2, fg=fg).grid(row=0, column=7)
    Label(main_window, text="no of",font = ("verdana",10, "bold"), bg=bg2, fg=fg).grid(row=0, column=8)
    Label(main_window, text="recipt",font = ("verdana",10, "bold"), bg=bg2, fg=fg).grid(row=0, column=9)

    #variable x keeps track of the customer entries
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

        #prints customer info in idle
        print("")
        print(x+1)
        print("name:",customers[x][0], customers[x][1])
        print("item:", customers[x][2],"", customers[x][3])
        print("recipt:", customers[x][4])

        #adds number for printing entrys from list
        x +=1
        row +=1
    print("---")

        

#deletes a customer entry
def delete():
    #checks if row number selected is not higher then the customer list.
        dele = int(delete_item.get())
        if dele > entered_count["entries"] or dele == 0:
            print("no")
        elif dele <= entered_count["entries"] and dele !=0:
            print("yes")
            #so the user does not need to enter in 0 to delete the first 1 entry.
            dele-=1

            delete_item.delete(0,"end")
            del customers[int(dele)]
            x = entered_count["entries"]
            entered_count["entries"]-=1
            delete_item.delete(0,"end")
            dele+=2

            #removes entry
            print_entry()
            Label(main_window, text="-",width = 1,font = font, bg=bg2, fg=fg).grid(row=x, column=4)
            Label(main_window, text="-",width = 10,font = font, bg=bg2, fg=fg).grid(row=x, column=5)
            Label(main_window, text="-",width = 10,font = font, bg=bg2, fg=fg).grid(row=x, column=6)
            Label(main_window, text="-",width = 10,font = font, bg=bg2, fg=fg).grid(row=x, column=7)
            Label(main_window, text="-",width = 5,font = font, bg=bg2, fg=fg).grid(row=x, column=8, sticky= W)
            Label(main_window, text="-",width = 5,font = font, bg=bg2, fg=fg).grid(row=x, column=9, sticky= E)
    
        
#functions in main window buttons and text
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

    Label(main_window, text=" ", width = 5, font = font, bg=bg2).grid(row=7, column=0)

    Label(main_window, text="row #", bg=bg2, font = font, fg=fg).grid(row=8, column=0, sticky=W)

    Button(main_window, text="delete", command=delete, width = 6, font = font, bg = bg3, fg="red").grid(row=8, column=0,padx=40)

    #the blank lables (text="") are for the rows with nothing in them for the layout

#font and colour theme

font = ("verdana",9)
#courier"MS Serif"mario64

#bg = "aquamarine1"
#bg3 = "dark turquoise"


#bg= "slateblue" background
#bg2 = "aquamarine" foreground
#bg3 ="cyan" button
#bg="grey59"
#bg2 = "grey22"
#bg3 ="grey36"
fg = "midnight blue"
bg="light blue"
bg2 = "white"
bg3 ="darkturquoise"

#for the main window
main_window = Tk()
main_window.configure(bg=bg2)
main_window.title("Party Hire Program")

#first and last name entry boxes
first_name = Entry(main_window, width = 20, font = font, bg=bg, fg=fg)
first_name.grid(row=1, column=1, sticky = W)
last_name = Entry(main_window, width = 20, font = font, bg=bg,fg=fg)
last_name.grid(row=2, column=1, sticky = W)

#list of items to choose from
items = ["balloons", "lights", "chairs", "tables", "costumes", "hats", "party decorations"]
#item dropdown entry box
itembox = ttk.Combobox(main_window, values = items, width = 15, font = font)
itembox.grid(row=4,column=1, sticky = W)
itembox.set("Select/enter item")
#item dropdown box style colour and font
style = ttk.Style()
style.theme_use('clam')
style.configure('TCombobox', fieldbackground = bg, background= bg3, fg=fg ,foreground=fg, buttonbackground =bg3)
#item number spinbox for entry
numbox = Spinbox(main_window, from_=0, to=500, width = 5, font = font, bg=bg, fg=fg, buttonbackground =bg3)
numbox.grid(row=4,column=2, sticky = W)

#empty customer list. to be filled with user customer details inputs
customers = []
#dictonary tracks the number of user entries
entered_count = {"entries":0}

#delete row entry dropdown box
delete_item = Spinbox(main_window, from_=0, to=9999 ,width = 2, font = font, bg=bg, fg=fg, buttonbackground =bg3)
delete_item.grid(row=8, column=1, sticky = W)


main()
