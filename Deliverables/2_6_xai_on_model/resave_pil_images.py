import os
from pathlib import Path

from PIL import Image


def resave_all_images(dataset_path):
    for dir_name in Path(dataset_path).iterdir():
        for filename in os.listdir(dir):
            if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise Exception(f'This file is not image {filename}')
            try:
                with Image.open(os.path.join(dir_name, filename)) as img:
                    img.save(os.path.join(dir_name, filename))  # Re-save image
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print('Everything went smoothly!')
