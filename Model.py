from tensorflow.keras import models, layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

# Data Generators
datagen = ImageDataGenerator(rescale=1.0 / 255.0, validation_split=0.2)

train_generator = datagen.flow_from_directory(
    'Output_Data', target_size=(224, 224), batch_size=32, class_mode='binary', subset='training'
)

val_generator = datagen.flow_from_directory(
    'Output_Data', target_size=(224, 224), batch_size=32, class_mode='binary', subset='validation'
)

# Model Definition
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Training the Model
model.fit(
    train_generator, validation_data=val_generator, epochs=10
)

# Save the Model
model.save('theft_detection_model.h5')

print("Model training complete and saved as 'theft_detection_model.h5'")
