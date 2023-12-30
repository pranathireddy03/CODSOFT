import tkinter as tk
import random
import string

def generate_password():
    length = int(entry_length.get())
    if length > 0:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        entry_password.delete(0, tk.END)
        entry_password.insert(tk.END, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create GUI elements
frame_length = tk.Frame(root)
frame_length.pack()

label_length = tk.Label(frame_length, text="Password Length:")
label_length.pack(side=tk.LEFT)

entry_length = tk.Entry(frame_length, width=5)
entry_length.pack(side=tk.LEFT)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack()

frame_password = tk.Frame(root)
frame_password.pack()

label_password = tk.Label(frame_password, text="Generated Password:")
label_password.pack(side=tk.LEFT)

entry_password = tk.Entry(frame_password, width=30)
entry_password.pack(side=tk.LEFT)

root.mainloop()
