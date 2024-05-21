from PIL import Image
import os

def resize_and_crop_images(directory, target_size=(640, 480)):
    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(directory, filename)
            image = Image.open(file_path)

            # Calculate the new size, maintaining the aspect ratio
            ratio = max(target_size[0] / image.size[0], target_size[1] / image.size[1])
            new_size = (int(image.size[0] * ratio), int(image.size[1] * ratio))
            image = image.resize(new_size, Image.ANTIALIAS)

            # Calculate the position to crop the image
            left = (new_size[0] - target_size[0]) / 2
            top = (new_size[1] - target_size[1]) / 2
            right = (new_size[0] + target_size[0]) / 2
            bottom = (new_size[1] + target_size[1]) / 2

            # Crop the image
            image = image.crop((left, top, right, bottom))

            # Save the resized and cropped image
            image.save(file_path)
            print(f"Resized and cropped {filename}")

# Replace 'your_directory_path' with the path to your images folder
resize_and_crop_images('./photos/full_class_cropped', target_size=(524,524))
