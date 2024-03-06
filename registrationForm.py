from tkinter import * 
root = Tk()
root.geometry("500x300")


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

root.mainloop()