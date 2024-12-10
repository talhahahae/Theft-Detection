from PIL import Image
import os

def preprocess_data(input_dir, output_dir, size=(224, 224)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for subdir in os.listdir(input_dir):
        class_dir = os.path.join(input_dir, subdir)
        output_class_dir = os.path.join(output_dir, subdir)
        print(output_class_dir)
        if not os.path.exists(output_class_dir):
            os.makedirs(output_class_dir)
        for frame in os.listdir(class_dir):
            img_path = os.path.join(class_dir, frame)
            img = Image.open(img_path).resize(size)
            img.save(os.path.join(output_class_dir, frame))

# Run the preprocessing
preprocess_data('Data', 'Output_Data', size=(224, 224))
