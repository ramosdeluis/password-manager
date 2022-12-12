from tkinter import messagebox
from tkinter import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    user_password.delete(0, END)
    from random import choice
    password = ''
    for _ in range(8):
        password += choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!$%&()?*+')
    user_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    site = user_site.get()
    email = user_username.get()
    password = user_password.get()

    if site.strip() == '':
        messagebox.showerror(title='ops', message='Sorry, you need to put a website.')
    elif password.strip() == '':
        messagebox.showerror(title='ops', message='Sorry, you need to put a password.')
    elif email.strip() == '':
        messagebox.showerror(title='ops', message='Sorry, you need to put an email.')

    else:
        is_ok = messagebox.askokcancel(title=site, message=f'These are the details entered:\n'
                                                           f'Site: {site}\n'
                                                           f'Email: {email}\n'
                                                           f'Password: {password}\n'
                                                           f'Is it ok to save?')

        if is_ok:
            write_password(site, email, password)


def write_password(site, email, password):
    with open('passwords.txt', mode='a') as file:
        file.write(f'{site} <> {email} <> {password}\n')
    user_site.delete(0, END)
    user_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(200, 200)
window.title('Password Manager')
window.config(padx=20, pady=20)

# Labels
site_label = Label(text='Website:', font=('Arial', 16, 'bold'))
email_label = Label(text='Email/username:', font=('Arial', 16, 'bold'))
password_label = Label(text='Password:', font=('Arial', 16, 'bold'))

site_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entry
user_site = Entry(width=30)
user_username = Entry(width=30)
user_username.insert(0, 'user@gmail.com')
user_password = Entry(width=30)

user_site.grid(column=1, row=1)
user_username.grid(column=1, row=2)
user_password.grid(column=1, row=3)

# Canvas
canvas = Canvas()
logo = PhotoImage(file='logo.png', height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Buttons
generate_button = Button(text='Generate', width=12, command=password_generator)
save_button = Button(text='Save', width=28, command=save)
generate_button.grid(column=0, row=4)
save_button.grid(column=1, row=4)

window.mainloop()
