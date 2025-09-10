import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import * 
import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
from tkinter import messagebox as ms
import cv2
import os
from PIL import Image , ImageTk 
import tkinter as tk
import tkinter as ttk
import re
from tkinter.ttk import *
#import cv2
import sqlite3
import webbrowser
from PIL import Image, ImageTk

root = Tk()
w, h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.geometry("%dx%d+0+0" % (w,h))
root.title('Main Page')



image2 =Image.open('images/sss.png')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=100)


name = tk.StringVar()
address = tk.StringVar()
#username = tk.StringVar()
Email = tk.StringVar()
PhoneNo = tk.IntVar()
var = tk.IntVar()


image2 = Image.open("images/11.webp") 
image2=image2.resize((150,50),Image.LANCZOS)

bd_image = ImageTk.PhotoImage(image2)
bd_label = tk.Label(root, image=bd_image)
bd_label.image= bd_image
bd_label.place(x=30,y=15)

SVBar = tk.Scrollbar(root)
SVBar.pack(side=tk.RIGHT, fill="y")

root.configure(background ='white')   

c = Canvas(root, height="60", width="1518", background="#BEADFA")
c.place(x=0,y=80)

d = Canvas(root, height="70", width="170", background="#f37021",bd=0)
# # text = "What’s New"  # Your text here
# text_id = d.create_text(80, 40, text="What\'s New", font=("Arial", 14))
# d.place(x=0,y=650)


db = sqlite3.connect('faceData.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS User"
               "(Id TEXT,Name TEXT,  Email TEXT, Address TEXT, Gender TEXT,Phoneno TEXT)")
db.commit()
Name=StringVar()
Email=StringVar()
Address = StringVar()
Gender=IntVar()
Phoneno= StringVar()

my_conn = sqlite3.connect('faceData.db')

def Home():
    from subprocess import call
    call(["Python","main.py"])
open_acc = tk.Button(root, text= "Home",foreground="white", background="#BEADFA",bd=0,height=1,font=("Times New Roman",18,'bold'),command=Home)
open_acc.place(x=10,y=90)

def database():
   
   name = Name.get()
   address = Address.get()
   email = Email.get()
   mobileno = Phoneno.get()
   gender=Gender.get()
   conn = sqlite3.connect('faceData.db')
  #  with conn:
  #     cursor=conn.cursor()
  # # cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
  #  cursor.execute('INSERT INTO User (Name,Address,Email,Gender,Phoneno) VALUES(?,?,?,?,?)',(name,address,email,gender,mobileno))
  #  conn.commit()
  #  ms.showinfo('Success!', 'Account Created Successfully .........!')
   
   with sqlite3.connect('faceData.db') as db:
       c = db.cursor()

   # Find Existing username if any take proper action
   # find_user = ('SELECT * FROM registration WHERE Email = ?')
   # c.execute(find_user, [(Email.get())])
   
   regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
   if (re.search(regex, email)):
       a = True
   else:
       a = False
   # validation
   if (name.isdigit() or (name == "")):
       ms.showinfo("Message", "please enter valid name")
       
   elif (address == ""):
            ms.showinfo("Message", "Please Enter Address")
   
   elif (email == "") or (a == False):
       ms.showinfo("Message", "Please Enter valid email")
       
   
           
        
   elif((len(str(mobileno)))<10 or len(str((mobileno)))>10):
       ms.showinfo("Message", "Please Enter 10 digit mobile number")
   # elif (c.fetchall()):
   #     ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
  
   
   elif (gender == False):
       ms.showinfo("Message", "Please Enter gender")
   
   else:
       conn = sqlite3.connect('faceData.db')
       with conn:
           cursor = conn.cursor()
           cursor.execute('INSERT INTO User (Name,Address,Email,Gender,Phoneno) VALUES(?,?,?,?,?)',(name,address,email,gender,mobileno))

           conn.commit()
           db.close()
           ms.showinfo('Success!', 'Account Created Successfully !')
           from subprocess import call
           call(["Python","face_login.py"])
          
           
   
   
   
   
   


a11=tk. Label(root,text='Register here ',fg='black',bg ='powder blue',font=('Times new roman',25,'bold')).place(x=700,y=180)

frame=tk.Frame(root,height=430,width=650,bg="#F5FFFA")
frame.place(x=500,y=250)

label=tk.Label(frame,text="Full Name:",font=("Calibri",15,'bold'),bg="#F5FFFA")
label.place(x=180,y=50)

entry=tk.Entry(frame,border=2,width=30,textvar=Name)
entry.place(x=300,y=50,height=25)

label=tk.Label(frame,text="Address:",font=("Calibri",15,'bold'),bg="#F5FFFA")
label.place(x=180,y=100)

entry=tk.Entry(frame,border=2,width=30,textvar=Address)
entry.place(x=300,y=100,height=25)

label=tk.Label(frame,text="Email:",font=("Calibri",15,'bold'),bg="#F5FFFA")
label.place(x=180,y=150)

entry=tk.Entry(frame,border=2,width=30,textvar=Email)
entry.place(x=300,y=150,height=25)



label=tk.Label(frame,text="Contact No:",font=("Calibri",15,'bold'),bg="#F5FFFA")
label.place(x=180,y=200)

entry=tk.Entry(frame,border=2,width=30,textvar=Phoneno)
entry.place(x=300,y=200,height=25)


a1=tk.Label(frame,text="Gender:",font=("Calibri",15,'bold'),bg="#F5FFFA").place(x=180,y=250)

tk.Radiobutton(frame,text="Male",font=("Calibri",15,'bold'),bg="#F5FFFA",value=1,variable=Gender).place(x=300,y=250)
tk.Radiobutton(frame,text="Female",font=("Calibri",15,'bold'),bg="#F5FFFA",value=2,variable=Gender).place(x=400,y=250)

def display():
    
    
    from subprocess import call
    call(['python','display.py'])


btn=tk.Button(frame,text="Create Account",font=("Arial",14,'bold'),width=20,command=database,
              
              bg="#F5FFFA",
              fg="black",
            )
btn.place(x=50,y=350)


btn=tk.Button(frame,text="Display",font=("Arial",14,'bold'),width=20,command=display,
              
              bg="#F5FFFA",
              fg="black",
            )
btn.place(x=380,y=350)


root.mainloop()
