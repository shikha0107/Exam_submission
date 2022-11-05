import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.config(bg="powder blue")
root.geometry("1305x652")
firstname=tk.StringVar()
last_name=tk.StringVar()
email=tk.StringVar()
add=tk.StringVar()
def b1():
    a = firstname.get()
    b = last_name.get()
    c=email.get()
    d=add.get()
    lb1.insert(1, a)
    lb1.insert(2,b)
    lb1.insert(3,c)
    lb1.insert(4,d)

   
def b2():
    firstname.set("")
    last_name.set("")
    email.set("")
    add.set("")

def b3():
    root.config(bg="black")
    lb1.config(bg="red")
    f.config(bg="sky blue")


f=tk.Frame(root,height=800,width=470,bg='white',bd=10,relief='groove')
f.place(x=10,y=20)


l1=tk.Label(f,text="first name" ,font="arial 10 bold")
l2=tk.Label(f,text="last name ",font="arial 10 bold")
l3=tk.Label(f,text="gender",font="arial 10 bold")
l4=tk.Label(f,text="language",font="arial 10 bold")
l5=tk.Label(f,text="email",font="arial 10 bold")
l6=tk.Label(f,text="address",font="arial 10 bold")
l7=tk.Label(f,text="state",font="arial 10 bold")
l8=tk.Label(f,text="zip",font="arial 10 bold")
l9=tk.Label(f,text=" credit card type",font="arial 10 bold")

e1=tk.Entry(f,textvariable=firstname,font="arial 10 bold")
e2=tk.Entry(f,textvariable=last_name,font="arial 10 bold")
e3=tk.Entry(f,textvariable=email,font="arial 10 bold")
e4=tk.Entry(f,textvariable=add,font="arial 10 bold")
e5=tk.Entry(f,font="arial 10 bold")


r1=tk.Radiobutton(f,text="male", value="male",font="arial 10 bold")
r2=tk.Radiobutton(f,text="female", value="female",font="arial 10 bold")

c1=tk.Checkbutton(f,text="telugu")
c2=tk.Checkbutton(f,text="english")
c3=tk.Checkbutton(f,text="hindi")

n = tk.StringVar()
c = ttk.Combobox(f, width = 27, textvariable = n)
c['values'] = ('gujrat','rajasthan','maharastra','goa')

n = tk.StringVar()
cb = ttk.Combobox(f, width = 27, textvariable = n)
cb['values'] = ('bob','state bank of india','maharastra','goa bank ')


# li=tk.Listbox(root,width=50,height=20,bg="grey",font="Arail 14 bold")
# li.grid(row=5,column=0,rowspan=10)

lb1=tk.Listbox(root,width=50,height=20,bg="light grey",font="Arail 14 bold")

# lb1.grid(row=1,column=12,columnspan=3)


b1=tk.Button(root,text="insert",font=("ArialBold",12),width=7,height=1,bd=3,command=b1)
b1.pack()
# b1.grid(row=6,column=20,padx=40)
b2=tk.Button(root,text="delete",font=("ArialBold",12),width=7,height=1,bd=3,command=b2)
b2.pack()
# b2.grid(row=7,column=20,padx=40)
b3=tk.Button(root,text="theme",font=("ArialBold",12),width=7,height=1,bd=3,command=b3)
b3.pack()
# b3.grid(row=8,column=20,padx=40)




# li.insert(1,"hello")
# li.insert(1,"hello1")

l1.grid(row=1,column=2)
l2.grid(row=3,column=2)
l3.grid(row=5,column=2)
l4.grid(row=7,column=2)
l5.grid(row=9,column=2)
l6.grid(row=11,column=2)
l7.grid(row=13,column=2)
l8.grid(row=15,column=2)
l9.grid(row=17,column=2)

e1.grid(row=1,column=8)
e2.grid(row=3,column=8)
e3.grid(row=9,column=8)
e4.grid(row=11,column=8)
e5.grid(row=15,column=8)

r1.grid(row=5,column=8)
r2.grid(row=5,column=9)

c1.grid(row=7,column=7)
c2.grid(row=7,column=8)
c3.grid(row=7,column=9)

c.grid(row=13,column=8)
cb.grid(row=17,column=8)
# lb1.grid(row=2,column=50)
lb1.pack()
root.mainloop()