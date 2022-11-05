from tkinter import *

shikha = Tk()
shikha.geometry("1224x2564")
shikha.title("Billing System")

# insert function
def insert_():
    pass
#delete function
def delete_():
    pass

#theme function
def theme_():
        pass
#creating labels
name = Label(shikha, text="First Name: ", font="timesnewroman 12 bold").grid(row=1, column=2, padx=22, pady=10)
lname = Label(shikha, text="Last Name: ", font="timesnewroman 12 bold").grid(row=2, column=2, padx=22, pady=10)
gender = Label(shikha, text="Gender: ", font="timesnewroman 12 bold").grid(row=3, column=2, padx=22, pady=10)
lang = Label (shikha, text="Languages: ", font="timesnewroman 12 bold").grid(row=4, column=2, padx=22, pady=10)
email = Label(shikha, text="Email: ", font="timesnewroman 12 bold").grid(row=5, column=2, padx=22, pady=10)
address = Label(shikha, text = "Address: ", font="timesnewroman 12 bold").grid(row=6, column=2, padx=32, pady=50)
state = Label(shikha, text = "State: ", font="timesnewroman 12 bold").grid(row=7, column=2, padx=22, pady=10)
zip_= Label(shikha, text = "Zip code: ", font="timesnewroman 12 bold").grid(row=8, column=2, padx=22, pady=10)
cr_card  = Label(shikha, text= "Credit Card Type", font="timesnewroman 12 bold").grid(row=9, column=2, padx=22, pady=10)

#making variables to get user input
namevalue = StringVar()
lnamevalue = StringVar()
gendervalue = IntVar()
gendervalue.set(1)
teluguvalue = IntVar()
englishvalue = IntVar()
hindivalue = IntVar()
mailvalue = StringVar()
addressvalue = StringVar()
statevalue = StringVar()
zipvalue = IntVar()
crcardvalue = StringVar()



#getting user input
name_entry = Entry(shikha, textvariable= namevalue).grid(row = 1, column=3)
lname_entry = Entry(shikha, textvariable=lnamevalue).grid(row=2, column=3)
gender_entry= Radiobutton(shikha, text="MALE", variable= gendervalue, value = 1).grid(row=3, column=3)
gender_entry= Radiobutton(shikha, text="FEMALE", variable= gendervalue, value = 2).grid(row=3, column=4)
lang_entry = Checkbutton(shikha, text = "Telugu", variable=teluguvalue).grid(row = 4, column=3)
lang_entry = Checkbutton(shikha, text = "English", variable=englishvalue).grid(row = 4, column=4)
lang_entry = Checkbutton(shikha, text = "Hindi", variable=hindivalue).grid(row = 4, column=5)
mail_entry = Entry(shikha, textvariable=mailvalue).grid(row = 5, column=3)
add_entry =Text(shikha,height=11,width=20,wrap="word").grid(row = 6, column=3)
sb = Scrollbar(add_entry).grid(row = 6, column=3)
state_entry = Entry(shikha, textvariable=statevalue).grid(row =7, column=3)
zip_entry = Entry(shikha, textvariable=zipvalue).grid(row = 8, column=3)
cr_card_Entry = Entry(shikha, textvariable=crcardvalue).grid(row = 9, column=3)

#adding the three buttons
insert_b = Button(shikha, command=insert_, text="INSERT", font="timesnewroman 8 bold", padx=18, pady=6).grid(row=4, column =7, padx=20, pady=10)
delete_b= Button(shikha, command=delete_, text="DELETE", font="timesnewroman 8 bold", padx=18, pady=6).grid(row=6, column =7, padx=20, pady=10)
theme_b = Button(shikha, command=theme_, text="THEME", font="timesnewroman 8 bold", padx=18, pady=6).grid(row=7, column =7, padx=20, pady=10)

shikha.mainloop()