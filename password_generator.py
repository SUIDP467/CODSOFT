import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showwarning("Input Error", "Password length must be greater than 0.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        
        password_var.set(password)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number.")

# Creating the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x200")

# Creating and placing the widgets
frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

ttk.Label(frame, text="Password Length").grid(row=0, column=0, padx=5, pady=5)
length_entry = ttk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)

password_var = tk.StringVar()
ttk.Label(frame, text="Generated Password").grid(row=1, column=0, padx=5, pady=5)
password_entry = ttk.Entry(frame, textvariable=password_var, state='readonly')
password_entry.grid(row=1, column=1, padx=5, pady=5)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Adding Exit button
exit_button = ttk.Button(frame, text="Exit", command=app.quit)
exit_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Running the main event loop
app.mainloop()
