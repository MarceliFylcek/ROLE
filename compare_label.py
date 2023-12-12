from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load_image(file_path):
    return Image.open(file_path)

def display_image(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def average_images(image1, image2):
    # Convert images to numpy arrays
    np_image1 = np.array(image1)
    np_image2 = np.array(image2)
    
    avg_image = (0.97*np_image1 + 0.03*np_image2)  # Integer division for averaging
    
    return Image.fromarray(avg_image.astype('uint8'))

# Replace 'image1.jpg' and 'image2.jpg' with your image file paths
image1 = load_image('Output_image/00001.png')
image1 = image1.convert('L')

image2 = load_image('Output_label/00001.png')

# Display original images
#display_image(image1)
#display_image(image2)

# Calculate and display average image
average_img = average_images(image1, image2)
#display_image(average_img)
plt.figure(figsize=(11, 8))
plt.imshow(average_img, cmap='gray')  # Change 'viridis' to any other available colormap
plt.axis('off')
plt.show()