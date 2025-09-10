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
from tkinter.ttk import *
#import cv2
import webbrowser
from PIL import Image, ImageTk

root = Tk()

root.geometry("1650x950") 
root.title('Main Page')

w, h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))

image2 =Image.open('social.webp')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=100)


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
# text = "What’s New"  # Your text here
def Home():
    from subprocess import call
    call(["Python","main.py"])
open_acc = tk.Button(root, text= "Home",foreground="white", background="#BEADFA",bd=0,height=1,font=("Times New Roman",18,'bold'),command=Home)
open_acc.place(x=10,y=90)

def Create_database():
        
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    cap = cv2.VideoCapture(0)
    
#    id = input('enter user id')
    id=entry2.get()
    
    sampleN=0;
    
    while 1:
    
        ret, img = cap.read()
    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
        for (x,y,w,h) in faces:
    
            sampleN=sampleN+1;
    
            cv2.imwrite("facesData/User."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
    
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
            cv2.waitKey(100)
    
        cv2.imshow('img',img)
    
        cv2.waitKey(1)
    
        if sampleN > 40:
            ms.showinfo('Success!', 'face Captured Successfully .........!')
            
    
            break
    
    cap.release()
    entry2.delete(0,'end')
    cv2.destroyAllWindows()
    
    

    
def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=300, y=400)   
    

def ID():     
    my_conn = sqlite3.connect('face.db')
    r_set=my_conn.execute("SELECT * FROM User")
    i=0 # row value inside the loop 
    for student in r_set: 
        for j in range(len(student)):
            e =tk.Entry(root, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
def reg():
   from subprocess import call
   call(['python','reg.py'])
   
   
def Train_database():
    from subprocess import call
    call(['python','train.py'])
    
def login():
    from subprocess import call
    call(['python','face_login.py'])
       
        
# reg = tk.Button(root, text= "Register",foreground="white", background="blue",bd=0,height=1,font=("Times New Roman",18),command=reg)
# reg.place(x=300,y=190)

# about = tk.Button(root, text= "Capture Face",foreground="white", background="blue",bd=0,height=1,font=("Times New Roman",18),command=Create_database)
# about.place(x=300,y=390)



button1= tk.Button(root, text="Register Here",width=25,background="powder blue" ,fg="black",font=("Times New Roman",20),bd=0,command=reg )
button1.place(x=450,y=300)
button2 = tk.Button(root, text="Login Here",width=25,command=login,background="powder blue" ,fg="black",font=("Times New Roman",20),bd=0)
button2.place(x=450, y=600)

button2= tk.Button(root, text="Capture Face",width=25,background="powder blue" ,fg="black",font=("Times New Roman",20),bd=0,command=Create_database )
button2.place(x=450,y=400)

button2 = tk.Button(root, text="Train Face Data",width=25,command=Train_database,background="powder blue" ,fg="black",font=("Times New Roman",20),bd=0)
button2.place(x=450, y=500)

personal = tk.Label(root, text= "Enter your Id here:",background="powder blue" ,fg="black",font=("Times New Roman",25),bd=0)
personal.place(x=450,y=700)



entry2=tk.Entry(root,bd=2,width=10)
entry2.place(x=730, y=700,height=35)



root.mainloop()