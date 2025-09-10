import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import speech_recognition as sr
import time
from playsound import playsound
from translate import Translator
import os
from gtts import gTTS
import cv2

# Initialize Tkinter window
root = tk.Tk()
root.title("Face Recognition Authentication")
root.geometry("800x600")  # Set window size

# Labels for displaying authentication status
status_label = tk.Label(root, text="Authentication Status: Waiting...", font=("Helvetica", 16))
status_label.pack(pady=20)

# Initialize variables
flag = 0
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainingdata.yml')  # Load your pre-trained model

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0  # Initialize ID
# names = ['None', 'Criminal person identified', 'Missing person', ...]

# Start video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Set video width
cam.set(4, 480)  # Set video height

minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

# Flag to exit the loop after authentication
auth_successful = False

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 8, minSize=(int(minW), int(minH)))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        if confidence < 60:
            id = str(id)
            confidence = "  {0}%".format(round(100 - confidence))

            # Update Tkinter label for authenticated user
            status_label.config(text="Authentication Status: Authenticated User", fg="green")

            # Display the authentication status text on the video feed
            cv2.putText(img, "Authenticated User", (x + 5, y - 30), font, 1, (0, 255, 0), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            # Show a popup message for authentication
            ms.showinfo("Authentication Status", "Authenticated User")

            # Set authentication successful flag to exit the loop
            auth_successful = True
            from subprocess import call
            call(['python','Gui_master.py'])
            break  # Exit the loop

        else:
            id = "Unknown Person Identified"
            confidence = "  {0}%".format(round(100 - confidence))

            # Update Tkinter label for unauthenticated user
            status_label.config(text="Authentication Status: Unauthenticated User", fg="red")

            # Display the authentication status text on the video feed
            cv2.putText(img, "Unauthenticated User", (x + 5, y - 30), font, 1, (0, 0, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    # Show video stream
    cv2.imshow('camera', img)

    # Update Tkinter window to keep it responsive
    root.update()

    # Exit the loop if 'Q' is pressed
    if cv2.waitKey(1) == ord('Q'):
        break

    # Exit if authentication was successful
    if auth_successful:
        break

# If no user was authenticated and 'Q' was pressed, show an error message
if not auth_successful:
    ms.showerror("Authentication Status", "Unauthenticated User")

# Release the camera and close OpenCV windows
cam.release()
cv2.destroyAllWindows()

# Close the Tkinter window after a delay or manual action
def close_window():
    root.quit()

# Use after() method to close window after 3 seconds
root.after(3000, close_window)

# Keep the Tkinter window open
root.mainloop()
