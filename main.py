from tkinter import *

FONT_NAME = "JetBrains Mono"
FONT = (FONT_NAME, 12, "bold")



def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    with(open("data.txt", "a")) as data_file:
        data_file.write(f"{website} | {email} | {password}")





window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# LABELS
website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=FONT)
email_label.config(padx=35)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

# ENTRIES
website_entry = Entry(width=57)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=57)
email_entry.insert(0, "example@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=38)
password_entry.grid(row=3, column=1)

# BUTTONS
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=48, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()