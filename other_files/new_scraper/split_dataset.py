import splitfolders

# Define the input folder containing all the images

input_folder = "./img_by_class"
# Define the output folder where the split datasets will be saved
output_folder = "./new_dataset_400"

# Split the dataset into train, validation, and test sets with a ratio of 0.8, 0.1, 0.1 respectively
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(0.6, 0.2, 0.2), group_prefix=None)

print("Dataset split completed successfully!")