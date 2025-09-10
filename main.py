from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter.ttk import *
#import cv2
import webbrowser
from PIL import Image, ImageTk

base = Tk()

base.geometry("1650x950") 
base.title('Main Page')

w, h = base.winfo_screenwidth(),base.winfo_screenheight()
base.geometry("%dx%d+0+0" % (w,h))

image2 = Image.open("images/11.webp") 
image2=image2.resize((150,50),Image.LANCZOS)

bd_image = ImageTk.PhotoImage(image2)
bd_label = tk.Label(base, image=bd_image)
bd_label.image= bd_image
bd_label.place(x=30,y=15)


SVBar = tk.Scrollbar(base)
SVBar.pack(side=tk.RIGHT, fill="y")

base.configure(background ='white')   

c = Canvas(base, height="60", width="1518", background="#BEADFA")
c.place(x=0,y=80)

d = Canvas(base, height="70", width="170", background="#f37021",bd=0)
# text = "What’s New"  # Your text here
text_id = d.create_text(100, 40, text="What\'s New", font=("Arial", 14))
d.place(x=0,y=690)






personal = tk.Label(base, text= "Face Authentication System",foreground="black", background="#BEADFA",bd=0,height=1,font=("Times New Roman",30))
personal.place(x=550,y=90)




####################################################################################################################################
# def acc():
#     from subprocess import call
#     call(["Python","About_us.py"])
# account = tk.Button(base, text= "About Us",foreground="white", background="#BEADFA",bd=0,height=1,font=("Times New Roman",18), command= acc)
# account.place(x=140,y=90)

# def card():
#     from subprocess import call
#     call(["Python","contact_us.py"])
# card = tk.Button(base, text= "Contact Us",foreground="white", background="#BEADFA",bd =0,height=1,font=("Times New Roman",18),command=card)
# card.place(x=325,y=90)



###################################################################################################################

image_paths = [
    "images/s.jpg"
    # Add more image paths as needed
]


frame = ttk.Frame(base)
frame.place(x=0,y=145)


current_image_index = 0

def update_image():
    global current_image_index
    image_path = image_paths[current_image_index]
    img = Image.open(image_path)
    img = img.resize((1518, 550), Image.LANCZOS)  # Adjust the size as needed
    img = ImageTk.PhotoImage(img)
    
    label.config(image=img)
    label.image = img
    current_image_index = (current_image_index + 1) % len(image_paths)
    base.after(2000, update_image)  # Change image every 2000 milliseconds (2 seconds)

label = ttk.Label(frame)
label.pack()

update_image()  # Start the slideshow

def prev_image():
    global current_image_index
    current_image_index = (current_image_index - 1) % len(image_paths)
    update_image()

def next_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(image_paths)
    update_image()
##########################################################################################
def scroll_text():
    global text_id, text_x
    
    # Move the text horizontally
    canvas.move(text_id, -3, 0)  # Change the '-1' to adjust the scrolling speed
    
    # If the text moves out of the window, reset its position
    if canvas.bbox(text_id)[2] <= 0:
        text_x = canvas.winfo_width()
        canvas.coords(text_id, text_x, 30)  # Adjust '50' to change the vertical position
    
    # Call the scroll_text function again after 30 milliseconds
    base.after(30, scroll_text)
def register():
    from subprocess import call
    call(["Python","registration.py"])
open_acc = tk.Button(base, text= "Open an Account",foreground="Black", background="white",bd=0,height=1,font=("Times New Roman",20,'bold'),command=register)
open_acc.place(x=650,y=170)



# Create a Canvas widget
canvas = tk.Canvas(base, width=1450, height=70,background="#BEADFA",bd=0)
canvas.place(x=160,y=690)

# Display scrolling text on the Canvas
text = '''Unlock Your Instagram Experience: Embrace the Future with Face Authentication – Your Unique Identity, Your Personal Space, All at the Blink of an Eye!'''  # Your text here
text_id = canvas.create_text(400, 40, text=text, font=("Arial", 14), anchor=tk.W)
text_x = 200

# Start scrolling the text
scroll_text()

base.mainloop()