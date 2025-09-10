import numpy as np
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

mode = "display"  # Change to "train" if you want to train the model

# Function to plot model history
def plot_model_history(model_history):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs[0].plot(model_history.history['accuracy'])
    axs[0].plot(model_history.history['val_accuracy'])
    axs[0].set_title('Model Accuracy')
    axs[0].set_ylabel('Accuracy')
    axs[0].set_xlabel('Epoch')
    axs[0].legend(['Train', 'Validation'], loc='best')
    
    axs[1].plot(model_history.history['loss'])
    axs[1].plot(model_history.history['val_loss'])
    axs[1].set_title('Model Loss')
    axs[1].set_ylabel('Loss')
    axs[1].set_xlabel('Epoch')
    axs[1].legend(['Train', 'Validation'], loc='best')
    
    plt.show()
    fig.savefig('plot.png')

# Data paths
train_dir = 'training_set'
val_dir = 'testing_set'
num_train = 3187
num_val = 902
batch_size = 64
num_epoch = 5

# Data augmentation
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir, target_size=(64, 64), batch_size=batch_size,
    color_mode="grayscale", class_mode='categorical')

validation_generator = val_datagen.flow_from_directory(
    val_dir, target_size=(64, 64), batch_size=batch_size,
    color_mode="grayscale", class_mode='categorical')

num_classes = len(train_generator.class_indices)  # Get number of classes dynamically

# Model definition
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(num_classes, activation='softmax'))  # Ensure correct number of classes

if mode == "train":
    model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.0001, decay=1e-6), metrics=['accuracy'])
    model_info = model.fit(
        train_generator,
        steps_per_epoch=num_train // batch_size,
        epochs=num_epoch,
        validation_data=validation_generator,
        validation_steps=num_val // batch_size
    )
    plot_model_history(model_info)
    model.save_weights('modelnew.h5')

if mode == "display":
    model.load_weights('modelnew.h5')

    # Manually assigned emotion dictionary
    emotion_dict = {1: "Rupesh", 2: "Sourabh", 3: "Swapnil", 4: "None"}  

    # Ensure the color dictionary covers all classes
    color_dict = {i: (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)) for i in range(len(emotion_dict))}

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        x, y, w, h = 100, 100, 200, 200  # Static bounding box
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
        
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (64, 64)), -1), 0)
        
        prediction = model.predict(cropped_img)
        maxindex = int(np.argmax(prediction))
        print("Predicted Index:", maxindex)  # Debugging: Print predicted index
        
        # Ensure maxindex exists in emotion_dict to prevent KeyError
        predicted_label = emotion_dict.get(maxindex, "Unknown")  
        label_color = color_dict.get(maxindex, (255, 255, 255))  # Default to white if missing
        
        cv2.putText(frame, predicted_label, (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, label_color, 2, cv2.LINE_AA)
        cv2.imshow('Video', cv2.resize(frame, (800, 480), interpolation=cv2.INTER_CUBIC))
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
