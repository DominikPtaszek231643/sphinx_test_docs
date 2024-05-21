import os
from pathlib import Path

from PIL import Image


def resave_all_images(dataset_path):
    for typeset_dir in Path(dataset_path).iterdir():

        for class_dir in Path(typeset_dir).iterdir():

            for filename in os.listdir(class_dir):
                if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    raise Exception(f'This file is not image {filename}')
                try:
                    with Image.open(os.path.join(class_dir, filename)) as img:
                        img.save(os.path.join(class_dir, filename))  # Re-save image

                except Exception as e:
                    print(f"Error processing {filename}: {e}")

                    img_path = os.path.join(class_dir, filename)
                    os.remove(img_path)
                    print(f'This image is deleted!!!!! {img_path}')

                print(f'Current image preprocessed:{class_dir} {filename}')

    print('Everything went smoothly!')


resave_all_images('./new_dataset_400')