import splitfolders

# Define the input folder containing all the images
input_folder = "./database/data_sets/photos_by_class"

# Define the output folder where the split datasets will be saved
output_folder = "./database/data_sets/dataset"

# Split the dataset into train, validation, and test sets with a ratio of 0.8, 0.1, 0.1 respectively
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(0.7, 0.2, 0.1), group_prefix=None)

print("Dataset split completed successfully!")