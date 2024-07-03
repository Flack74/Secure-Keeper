from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    hindi = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऍ', 'ऐ', 'ओ', 'ऑ', 'औ', 'अं', 'अः', 'अँ', 'क', 'ख', 'ग', 'घ',
             'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म',
             'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'क़', 'ख़', 'ग़', 'ज़', 'फ़', 'ड़', 'ढ़', '्ष', 'ज', '्ञ', 'त्क', 'द्व',
             'द्य',
             'द्', 'द', 'त्', 'त', 'ड्', 'ड', 'द्भ', 'द्म', 'ह्म', 'ह्य', 'श्र', 'र', 'र्प', 'प्र', 'ट्र', ]
    japanese = ['ろ', 'ぬ', 'ふ', 'あ', 'う', 'え', 'お', 'や', 'ゆ', 'よ', 'わ', 'ほ', 'へ', 'た', 'て', 'い', 'す', 'か', 'ん',
                'な', 'に', 'ら', 'せ', 'ち', 'と', 'し', 'は', 'き', 'く', 'ま', 'の', 'つ', 'さ', 'そ', 'ひ', 'こ', 'み', 'も']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_hindi = [choice(hindi) for _ in range(randint(2, 4))]
    password_jap = [choice(japanese) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers + password_hindi + password_jap
    shuffle(password_list)

    passwd = "".join(password_list)
    password.insert(0, passwd)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website.get(): {
            "email": email.get(),
            "password": password.get()
        }
    }
    if len(website.get()) == 0 or len(email.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Alert", message="Please make sure you haven't left any fields empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website.delete(0, END)
            email.delete(0, END)
            password.delete(0, END)


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

        website_name = website.get()
        if website_name in data:
            email_search = data[website_name]["email"]
            password_search = data[website_name]["password"]
            messagebox.showinfo(title=website_name,
                                message=f"Email : {email_search}\nPassword : {password_search}")
        else:
            messagebox.showinfo(title=website_name,
                                message=f"No details for {website_name} exists")
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo = PhotoImage(file="password_logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, columnspan=2)

# Website label, entry and Search button
lab_web = Label(text="Website:")
lab_web.grid(row=1, column=0, sticky="e")

website = Entry(width=35)
website.grid(row=1, column=1, columnspan=2, sticky="ew")
website.focus()

search = Button(text="Search", command=find_password)
search.grid(row=1, column=2, sticky="ew")

# Email/Username label and entry
lab_email = Label(text="Email/Username:")
lab_email.grid(row=2, column=0, sticky="e")

email = Entry(width=35)
email.grid(row=2, column=1, columnspan=2, sticky="ew")

# Password label, entry, and generate button
lab_pass = Label(text="Password:")
lab_pass.grid(row=3, column=0, sticky="e")

password = Entry(width=21)
password.grid(row=3, column=1, sticky="ew")

gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2, sticky="ew")

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
