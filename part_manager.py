from tkinter import *
from db import Database #import our database class from the db module which contains our database class
from tkinter import messagebox
db = Database("store.db") #instantiate object from the database class

def populate_list():#function in charge of getting the data
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END,row)

def add_item():
    if part_text.get() == "" or Customer_text.get() == "" or Retailer_text.get() == "" or Price_text.get() == "":
        messagebox.showerror("Required Fields","Please include all fields")
        return
    db.insert(part_text.get(), Customer_text.get(), Retailer_text.get(),
    Price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), Customer_text.get(), Retailer_text.get(),
    Price_text.get()))
    populate_list( )

def remove_item():
    print("Remove")

def update_item():
    print("Update")

def clear_text():
    print("Clear")

app = Tk() #instantiate window object

#part Name
part_text = StringVar()
part_Label = Label(app, text="Part Name", font=("bold",14), pady=20)
part_Label.grid(row=0,column=0,sticky=W)
part_Entry = Entry(app, textvariable=part_text)
part_Entry.grid(row=0, column=1)

#Customer
Customer_text= StringVar()
Customer_Label = Label(app, text="Customer", font=("bold",14), pady=20)
Customer_Label.grid(row=0, column=2,sticky=W)
Customer_Entry = Entry(app, textvariable=Customer_text)
Customer_Entry.grid(row=0,column=3)

#Retailer
Retailer_text = StringVar()
Retailer_Label = Label(app, text="Retailer", font=("bold", 14), pady=20)
Retailer_Label.grid(row=1, column=0,sticky=W)
Retailer_Entry = Entry(app, textvariable=Retailer_text)
Retailer_Entry.grid(row=1,column=1)


#Price
Price_text = StringVar()
Price_Label = Label(app, text="Price", font=("bold",14), pady=20)
Price_Label.grid(row=1, column=2,sticky=W)
Price_Entry = Entry(app, textvariable=Price_text)
Price_Entry.grid(row=1, column=3)

#create a list box that will contain the list of my parts to be sold to customers

parts_list = Listbox(app, height=8, width=70, border=0)
parts_list.grid(row=3, column=0,columnspan=3,rowspan=6,pady=20, padx=20)

#Create a scrollbar for my list
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#set scrollbar to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#Buttons
add_btn = Button(app, text="Add Part", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text="Remove Part", width=12, command=remove_item)
remove_btn.grid(row=2,column=1)

update_btn = Button(app, text="Update Part", width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

 

app.title("Part Manager") 
app.geometry("700x350")

#populate data
populate_list()

app.mainloop() #Run program
  