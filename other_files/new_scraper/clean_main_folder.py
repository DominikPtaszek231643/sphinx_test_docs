
import os



def rename_and_cleanup_images(directory):
    # Define the allowed extensions
    allowed_extensions = {".jpg", ".jpeg"}

    # Initialize a counter for renaming files
    counter = 0

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if the file is an image with allowed extension
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() in allowed_extensions:
            file_name = str(file_path.split("/")[-1].split('\\')[-1].split('.')[0])
            print(file_name)


            # Rename the file
            new_filename = f"full_classroom_data{counter}{os.path.splitext(file_path)[1]}" if 'full_classroom' in file_name else     f"empty_classroom_data{counter}{os.path.splitext(file_path)[1]}"
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
            counter += 1
        elif os.path.isfile(file_path):
            # Delete the file if it's not an allowed image format
            os.remove(file_path)
            print(f"Deleted '{filename}' as it's not a .jpg or .jpeg file")




# Replace 'your_directory_path' with the path to the directory containing your images
rename_and_cleanup_images("./all_photos")



import os



def rename_and_cleanup_images(directory):
    # Define the allowed extensions
    allowed_extensions = {".jpg", ".jpeg"}

    # Initialize a counter for renaming files
    counter = 0

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if the file is an image with allowed extension
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() in allowed_extensions:
            # Rename the file
            new_filename = f"empty_classroom_duck_{counter}{os.path.splitext(file_path)[1]}"
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
            counter += 1
        elif os.path.isfile(file_path):
            # Delete the file if it's not an allowed image format
            os.remove(file_path)
            print(f"Deleted '{filename}' as it's not a .jpg or .jpeg file")




# Replace 'your_directory_path' with the path to the directory containing your images
# rename_and_cleanup_images("./empty_classroom")
