import os
import numpy as np

def process_files(directory):
    # List to store the results
    result = []

    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Ensure we're working with files only
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                
                # Filter lines that start with index 1 or 2
                lines_with_index_1 = [line for line in lines if line.strip().startswith('1')]
                lines_with_index_2 = [line for line in lines if line.strip().startswith('2')]
                
                # Check if the file has both index 1 and index 2 lines
                if lines_with_index_1 and lines_with_index_2:
                    # Store the filename and the relevant lines in the result list
                    result.append({
                        "filename": filename,
                        "index_1_lines": lines_with_index_1,
                        "index_2_lines": lines_with_index_2
                    })
    
    return result

# Specify the directory containing the files
directory = 'data/train_annotations'

# Process the files and get the result
processed_data = process_files(directory)

#Print the processed data
for item in processed_data:
    print(f"File: {item['filename']}")
    print("Lines starting with index 1 length:")
    for line in item['index_1_lines']:
        tokens = line.split(' ')
        w = float(tokens[3])
        h = float(tokens[4])

        length = np.sqrt((w*w) + (h*h))

        print(length)
    print("Lines starting with index 2 length:")
    for line in item['index_2_lines']:
        tokens = line.split(' ')
        w2 = float(tokens[3])
        h2 = float(tokens[4])

        length2 = np.sqrt((w2*w2) + (h2*h2))

        print(length2)

    print("\n" + "-"*50 + "\n")

# 2 0.709605 0.378216 0.336192 0.063465
# 1 0.318525 0.423671 0.497427 0.085763

# w1 = 0.336192
# h1 = 0.063465

# w2 = 0.497427
# h2 = 0.085763

# length1 = np.sqrt((w1*w1) + (h1*h1))
# length2 = np.sqrt((w2*w2) + (h2*h2))

# print(f'L2: {length1}\nL1: {length2}')
