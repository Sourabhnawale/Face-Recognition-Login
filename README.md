# Face Detection Login

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Enabled-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


**Face Detection Login** is a Python-based application that enables secure user authentication using facial recognition technology.  
The project leverages Deep Learning (CNN),OpenCV, and a Graphical User Interface to provide a seamless login and registration experience.  

# Features
- **User Registration** → Register new users by capturing their facial images.  
- **Face Recognition Login** → Authenticate users using real-time face detection & recognition.  
- **GUI Support** → Simple interface for registration, login, and user management.  
- **Model Training** → Train a CNN on collected face data.  
- **Database Integration** → Store user details & encodings in SQLite.  
- **Visualization** → Training/recognition graphs for better insights.  
- **Audio Feedback** → Voice feedback during login/registration.  



# Project Structure
Face Detection/
│
├── CNNModel.py # CNN model definition
├── display.py # GUI display utilities
├── face_login.py # Face login logic
├── face.db # SQLite database for user data
├── faceData.db # Additional database for face data
├── graphs.JPG / graphs1.JPG # Training/recognition graphs
├── Gui_master.py # Main GUI application
├── haarcascade_frontalface_default.xml # Haar Cascade for face detection
├── home.py # Home screen logic
├── main.py # Main entry point
├── model_CNN.py # CNN model utilities
├── modelnew.h5 # Trained CNN weights
├── plot.png # Training/accuracy plot
├── README.md # Project documentation
├── reg.py # Registration logic
├── registration.py # Registration GUI
├── social.webp # Social media icon/image
├── testing_file.py # Testing utilities
├── train.py # Model training script
├── trainingdata.yml # Face recognizer training data
├── voice.mp3 # Audio feedback file
├── your_database.db # Additional database
│
├── facesData/ # Collected training images
├── images/ # Extra images
├── testing_set/ # Test dataset
└── training_set/ # Training dataset



 Installation & Setup

1. Clone the repository
   ```bash
   git clone https://github.com/Sourabhnawale/Face-Recognition-Login.git
   cd Face-Recognition-Login
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the application

python main.py
Register a new user → Use GUI to capture facial images.
Login → Authenticate with face recognition in real time.
Database & Models → Stored in SQLite & trained CNN files.
Python 3.x
OpenCV
TensorFlow / Keras
NumPy
SQLite3
Pillow


Sourabh Nawale
GitHub Profile
sourabhnawale5154@gmail.com



