import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    password_length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def toggle_password_visibility():
    current_state = password_entry.cget('show')
    if current_state == '':
        password_entry.config(show='*')
    else:
        password_entry.config(show='')

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")  # Set initial size of the window

# Password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Uppercase letters
uppercase_var = tk.IntVar()
uppercase_checkbox = tk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.pack()

# Numbers
numbers_var = tk.IntVar()
numbers_checkbox = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
numbers_checkbox.pack()

# Symbols
symbols_var = tk.IntVar()
symbols_checkbox = tk.Checkbutton(window, text="Include Symbols", variable=symbols_var)
symbols_checkbox.pack()

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Generated password
password_entry = tk.Entry(window, show='*')
password_entry.pack()

# Show password button
show_password_button = tk.Button(window, text='Show Password', command=toggle_password_visibility)
show_password_button.pack()

# Run the main loop
window.mainloop()
