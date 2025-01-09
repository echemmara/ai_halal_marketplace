import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Initialize the model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),  # Convolutional Layer
    MaxPooling2D((2,2)),  # Pooling Layer
    Conv2D(64, (3,3), activation='relu'),  # Convolutional Layer
    MaxPooling2D((2,2)),  # Pooling Layer
    Flatten(),  # Flatten the data
    Dense(128, activation='relu'),  # Fully connected layer
    Dense(1, activation='sigmoid')  # Output layer for binary classification (Halal/Not Halal)
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Data Preprocessing and Augmentation
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

# Load training and validation data
train_generator = train_datagen.flow_from_directory(
    'path_to_dataset/training',
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    'path_to_dataset/training',
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# Train the model
model.fit(train_generator, epochs=10, validation_data=validation_generator)
