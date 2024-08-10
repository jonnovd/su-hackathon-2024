from PIL import Image
import numpy as np

image_path = 'data/train_images/p101.jpg'
image = Image.open(image_path)

image = image.convert('RGB')

image_array = np.array(image)

image_array = image_array / 255.0

print(image_array)

print(image_array.shape)
