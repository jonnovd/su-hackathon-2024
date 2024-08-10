from PIL import Image
import numpy as np

# Load the image
image_path = 'data/train_images/p101.jpg'
image = Image.open(image_path)

# Convert the image to RGB (if not already)
image = image.convert('RGB')

# Convert the image to a NumPy array
image_array = np.array(image)

# Optionally, normalize the image (e.g., to [0, 1] range)
image_array = image_array / 255.0

print(image_array)

print(image_array.shape)