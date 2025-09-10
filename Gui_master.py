from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter.ttk import *
#import cv2
import webbrowser
from PIL import Image, ImageTk
import time


root = tk.Tk()
root.title("Instagram Style Page")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(bg="white")

# Function to update time
def update_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

# Load and resize images
bg_img = Image.open("C:/Users/GAURI/Downloads/100% Code Face detection/100% Code/images/s.jpg").resize((w, h), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)

logo_img = Image.open("C:/Users/GAURI/Downloads/100% Code Face detection/100% Code/images/11.webp").resize((150, 50), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)

profile_img = Image.open("images/profile.webp").resize((50, 50), Image.LANCZOS)
profile_photo = ImageTk.PhotoImage(profile_img)

post_img = Image.open("images/social.webp").resize((400, 400), Image.LANCZOS)
post_photo = ImageTk.PhotoImage(post_img)

# Background Label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

c = Canvas(root, height="60", width="1520", background="#BEADFA")
c.place(x=0,y=60)

personal = tk.Label(root, text= "Face Authentication System",foreground="black", background="#BEADFA",bd=0,height=1,font=("Times New Roman",30))
personal.place(x=550,y=70)

# Top Navigation Bar
nav_bar = tk.Frame(root, bg="white", height=60)
nav_bar.pack(fill=tk.X)

logo_label = tk.Label(nav_bar, image=logo_photo, bg="white")
logo_label.pack(side=tk.LEFT, padx=10, pady=5)

search_entry = tk.Entry(nav_bar, font=("Arial", 12), bd=1, relief=tk.SOLID, width=30)
search_entry.pack(side=tk.LEFT, padx=20)

profile_btn = tk.Button(nav_bar, image=profile_photo, bd=0, bg="white")
profile_btn.pack(side=tk.RIGHT, padx=10)

# Time Display
time_label = tk.Label(nav_bar, font=("Arial", 12), bg="white")
time_label.pack(side=tk.RIGHT, padx=20)
update_time()

# Welcome Label

# Feed Section
feed_frame = tk.Frame(root, bg="white")
feed_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

post_label = tk.Label(feed_frame, image=post_photo, bg="white")
post_label.pack(pady=10)

like_btn = tk.Button(feed_frame, text="❤️ Like", font=("Arial", 12), bg="white", bd=0)
like_btn.pack()

# Run Application
root.mainloop()
