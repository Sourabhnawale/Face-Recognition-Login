import os
import sqlite3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize main window
root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")
root.title('Main Page')

# Load and display header image
header_image = Image.open("images/11.webp").resize((150, 50), Image.LANCZOS)
bd_image = ImageTk.PhotoImage(header_image)
bd_label = tk.Label(root, image=bd_image)
bd_label.image = bd_image
bd_label.place(x=30, y=15)

# Load and display background image
background_image = Image.open('images/sss.png').resize((w, h), Image.ANTIALIAS)
background_label = ImageTk.PhotoImage(background_image)
background_label_widget = tk.Label(root, image=background_label)
background_label_widget.image = background_label
background_label_widget.place(x=0, y=100)

# Create a canvas for the header
header_canvas = tk.Canvas(root, height=60, width=1518, background="#BEADFA")
header_canvas.place(x=0, y=80)

# Create a canvas for the "What's New" section
# new_canvas = tk.Canvas(root, height=70, width=170, background="#f37021", bd=0)
# new_canvas.create_text(100, 40, text="What\'s New", font=("Arial", 14))
# new_canvas.place(x=0, y=690)

# Database connection
my_conn = sqlite3.connect('faceData.db')

# Display title
personal_label = tk.Label(root, text="Face Authentication System", foreground="black", background="#BEADFA", bd=0, height=1, font=("Times New Roman", 30))
personal_label.place(x=550, y=90)

# Create a frame for the table
frame = tk.Frame(root)
frame.pack(expand=True)

# Create style for the Treeview
style = ttk.Style()
style.configure("Treeview",
                bordercolor="#000000",  # Set border color
                borderwidth=1,          # Set border width
                rowheight=25)          # Set row height
style.configure("Treeview.Heading",
                bordercolor="#000000",  # Set border color for headings
                borderwidth=1)          # Set border width for headings

# Create the Treeview for displaying data
tree = ttk.Treeview(frame, columns=("ID", "Name", "Other"), show='headings', height=15)
tree.pack(side=tk.LEFT)

# Scrollbar for the Treeview
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Fetch and display data in the Treeview
cursor = my_conn.execute('SELECT * FROM User')
columns = [description[0] for description in cursor.description]
tree["columns"] = columns

# Set column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

# Insert data into the Treeview
for row in cursor:
    tree.insert("", tk.END, values=row)

# Clean up
cursor.close()
my_conn.close()

# Start the main loop
root.mainloop()

