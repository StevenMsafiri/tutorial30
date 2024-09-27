from json import JSONDecodeError
from random import shuffle
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import  json
FONT = ("Arial", 10, "normal")


def find_password():
    website = web_input.get()
    try:
        with open("Password data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No info found about entered website")

    else:
        if website in data:
            messagebox.showinfo(title="website", message=f'email: {data[website]["email"]} \n'
                                                       f'password: {data[website]["password"]}')
        else:
            messagebox.showinfo(title="Error", message="No info saved about entered website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get()
    email = mail_input.get()
    password = pass_input.get()
    new_data = {
        website:{
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please make sure you haven't left any field empty")

    else:
        try:
            with open("Password data.json", "r") as data_file:
                # Reading
                data = json.load(data_file)

        except FileNotFoundError:
            with open("Password data.json", "w") as data_file:
                # noinspection PyTypeChecker
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("Password data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            messagebox.showinfo("Success", "Password has been saved")
            web_input.delete(0, END)
            pass_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
# window.geometry("500x500")
window.config(padx=50, pady=50)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 120, image=image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:", font=FONT)
web_label.grid(column=0, row=1)

web_input = Entry(width=28)
web_input.grid(column=1, row=1)
web_input.focus()

search_button = Button(width=8, text="Search", font=("Arial", 8, "normal"), command=find_password)
search_button.grid(column=2, row=1)

mail_label = Label(text="Email/Username:", font=FONT)
mail_label.grid(column=0, row=2)

mail_input = Entry(width=28)
mail_input.grid(column=1, row=2)
mail_input.insert(0, "stevenmsafir@gmail.com")

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

pass_input = Entry(width=28, show="*")
pass_input.grid(column=1, row=3)

pass_button = Button(text="Generate", font=("Arial", 8, "normal"), command=generate_password)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
