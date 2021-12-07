from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip

FONT_NAME = "JetBrains Mono"
FONT = (FONT_NAME, 12, "bold")

LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*()"
COMBINED_LIST = list(LETTERS + NUMBERS + SYMBOLS)


def generate_password():
    password_entry.delete(0, END)
    random.shuffle(COMBINED_LIST)
    max_length = 12
    password_list = []

    # add a random char from the COMBINED_LIST till the provided max password length has been reached
    for _ in range(max_length):
        password_list.append(random.choice(COMBINED_LIST))

    # shuffle the list and print out the password to the terminal
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Bruh", message="Make sure you don't have any empty fields.")
    else:
        confirmation = messagebox.askokcancel(title=website,
                                              message="These are the details entered: "
                                              f"\nEmail: {email}\nPassword: {password}\nConfirm?")

        if confirmation == True:
            with(open("passwords.txt", "a")) as password_file:
                password_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


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
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=48, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
