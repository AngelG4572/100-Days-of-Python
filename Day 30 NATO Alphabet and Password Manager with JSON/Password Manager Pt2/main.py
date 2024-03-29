from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
FONT = ("Times New Roman", 11, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    p_letters = [choice(letters) for _ in range(randint(8, 10))]
    p_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    p_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = p_letters + p_symbols + p_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "" or email == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                                f"\nPassword: {password} \nIs it okay to save?")
        if is_okay:
            try:
                with open(file="data.json", mode="r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open(file="data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open(file="data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)
            print(data)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")

    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}"
                                                       f"\nPassword: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager Pt2")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", font=FONT)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ", font=FONT)
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", font=FONT)
password_label.grid(row=3, column=0)

website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()

search = Button(text="Search", font=FONT, highlightthickness=0, width=15, command=find_password)
search.grid(row=1, column=2)

email_entry = Entry(width=55)
email_entry.insert(END, "a@venzeti.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

generate = Button(text="Generate Password", font=FONT, highlightthickness=0, command=generate_password)
generate.grid(row=3, column=2)

add = Button(text="Add", font=FONT, highlightthickness=0, width=41, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
