from tkinter import * 
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")


Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
address = Label(root, text="Address")
state = Label(root, text="State")
phone = Label(root, text="Phone")
email = Label(root, text="Email")

name.grid(row=1, column=2)
address.grid(row=2, column=2)
state.grid(row=3, column=2)
phone.grid(row=4, column=2)
email.grid(row=5, column=2)

namevalue = StringVar
addressvalue = StringVar
statevalue = StringVar
phonevalue = StringVar
emailvalue = StringVar

checkvalue = IntVar


nameentry = Entry(root, textvariable=namevalue)
addressentry = Entry(root, textvariable=addressvalue)
stateentry = Entry(root, textvariable=statevalue)
phoneentry = Entry(root, textvariable=phonevalue)
emailentry = Entry(root, textvariable=emailvalue)

# Packing entry fields

nameentry.grid(row=1, column=3)
addressentry.grid(row=2, column=3)
stateentry.grid(row=3, column=3)
phoneentry.grid(row=4, column=3)
emailentry.grid(row=5, column=3)

# Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)

#Submit Button

Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()