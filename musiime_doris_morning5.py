# Assignment : Deadline 01 July 2023 Time 5:00pm EAT
# Create a receipt printing program with GUI interface,
# a more advanced detail earns you more points.
from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.title("Billing receipt")
root.geometry("700x700")
bg_color = 'white'
# Variable
c_name = StringVar()
c_phone = StringVar()
item = StringVar()
Rate = IntVar()
Quantity = IntVar()
bill_no = StringVar()
x = random.randint(1000, 10000)
bill_no.set(str(x))

global l
l = []
# Function
def additm():
    n = Rate.get()
    m = Quantity.get()*n
    l.append(m)
    if item.get()!='':
        textarea.insert((10.0+float(len(l)-1)), f"{item.get()}\t\t{Quantity.get()}\t\t{m}\n")
    else:
        messagebox.showerror('Error','Please enter the item') 

def pbill():
    if c_name.get()=="" or c_phone.get()=="":
        messagebox.showerror("Error, Customer details are a must")
    else:
        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END,f'\n================')
        textarea.insert(END,f"Total Paybill Amount :\t\t\t{sum(l)}")
        textarea.insert(END,f'\n================')
        print_bill()

def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set(0)
    Quantity.set(0)
    welcome()

def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()
def print_bill():
    op = messagebox.askyesno("Print bill", "Do you want to print the bill?")
    if op > 0:
        bill_details = textarea.get('1.0', END)
        f1 = open("bills"+str(bill_no.get())+".txt", "w")
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo("Printed",f"Bill no, :{bill_no.get()} Printed Successfully")
    else:
        return
def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END,"\t Welcome to SHeen Retails")
    textarea.insert(END,f'\n\nBill Number :\t\t{bill_no.get()}')
    textarea.insert(END,f'\n Customer Name:\t\t{c_name.get()}')
    textarea.insert(END,f'\n Phone Number:\t\t{c_phone.get()}')
    textarea.insert(END,f"\n==================================")
    textarea.insert(END,f'\n Product\t\t QTY\t\tPrice')
    textarea.insert(END,f"\n==================================")
    textarea.configure(font='arial 10')    

# Top Section
title = Label(root, text="Receipt", bg=bg_color, fg='#000000', font=('times new roman',20), relief=GROOVE, bd=2)
title.pack(fill=X)
# Customer details
F1=LabelFrame(root, text="Customer details", bg=bg_color, fg='#000000', font=('times new roman',10), relief=GROOVE, bd=2)
F1.place(x=0, y=80, relwidth=1)

cname_lbl = Label(F1,text="Customer name", bg=bg_color, fg='#000000', font=('times new roman',10), relief=GROOVE, bd=2)
cname_lbl.grid(row=0, column=0, padx=10, pady=5)
cname_txt=Entry(F1, width=15, font='arial 15 ', relief=SUNKEN, textvariable=c_name)
cname_txt.grid(row=0, column=1, padx=10, pady=5)

cphone_lbl = Label(F1,text="Phone no.", bg=bg_color, fg='#000000', font=('times new roman',10), relief=GROOVE, bd=2)
cphone_lbl.grid(row=0, column=2, padx=10, pady=5)
cphone_txt=Entry(F1, width=15, font='arial 15 ', relief=SUNKEN, textvariable=c_phone)
cphone_txt.grid(row=0, column=3, padx=10, pady=5)

# Product details
F2=LabelFrame(root, text="Product details",font=('times new roman',10), relief=GROOVE, bd=2)
F2.place(x=20, y=180, width=640, height=500)

itm = Label(F2, text="Product Name", font=('times new roman',10),bg = bg_color, fg='black')
itm.grid(row=0, column=0, padx=30, pady=20)
itm_txt = Entry(F2, width=20, font='arial 10', textvariable=item)
itm_txt.grid(row=0, column=1, padx=30, pady=20)

rate = Label(F2, text="Product Rate", font=('times new roman',10),bg = bg_color, fg='black')
rate.grid(row=1, column=0, padx=30, pady=20)
rate_txt = Entry(F2, width=20, font='arial 10', textvariable=Rate)
rate_txt.grid(row=1, column=1, padx=30, pady=20)

quantity = Label(F2, text="Product Quantity", font=('times new roman',10),bg = bg_color, fg='black')
quantity.grid(row=2, column=0, padx=30, pady=20)
quantity_txt = Entry(F2, width=20, font='arial 10', textvariable=Quantity)
quantity_txt.grid(row=2, column=1, padx=30, pady=20)

# Button
btn1 = Button(F2, text='Add Item', font='arial 10', command=additm, padx =5, pady =10, bg='lime', width=10)
btn1.grid(row=3, column=0, padx=30, pady=5)

btn2 = Button(F2, text='Print Bill', font='arial 10', command=pbill, padx =5, pady =10, bg='lime', width=10)
btn2.grid(row=3, column=1, padx=10, pady=5)

btn3 = Button(F2, text='Clear', font='arial 10', padx =5, command=clear, pady =10, bg='lime', width=10)
btn3.grid(row=4, column=0, padx=10, pady=5)

btn4 = Button(F2, text='Exit', font='arial 10', padx =5, command=exit, pady =10, bg='lime', width=10)
btn4.grid(row=4, column=1, padx=10, pady=5)

# Bill area
F3 = Frame(root, relief=GROOVE, bd=2)
F3.place(x=360, y=200, width= 300, height= 300)
bill_title=Label(F3, text='Bill Area', font='arial 10',relief=GROOVE, bd=2).pack(fill=X)
scroll_y =Scrollbar(F3, orient= VERTICAL)
textarea = Text(F3, yscrollcommand=scroll_y )
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
welcome()

root.mainloop()