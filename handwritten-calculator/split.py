import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image



def split(image_path):

    # Get image and resize
    original_image = Image.open(image_path).convert("L")
    width = original_image.size[0]
    height = original_image.size[1]
    aspect_ratio = width / height  # width/height
    new_size = (int(75*aspect_ratio), 75)
    # resize to dimensions of images in dataset in README
    resized_image_pil = original_image.resize(new_size, Image.BICUBIC)

    # Convert to black and white and normalize
    threshold = 160
    bw_image_pil = resized_image_pil.point(lambda x: 0 if x < threshold else 255)
    bw_image_normalized = np.array(bw_image_pil) / 255

    # Get each part of expression
    elements = get_individual_elements(bw_image_normalized)

    # Add padding to elements (so every image is 75 by 75)
    padded_elements = pad_elements(elements)

    # Add extra channel (this is dirty and repeated logic)
    return np.expand_dims(padded_elements, axis=-1)



def pad_elements(elements):
    padded_elements = list()

    for element in elements:
        # Get amount of padding needed
        width = element.shape[1]
        padding = 75-width

        # If width > height, do nothing
        if padding <= 0:
            padded_elements.append(element)
            continue

        # Get right and left padding
        right_padding = padding // 2
        if padding % 2 == 0:
            left_padding = right_padding
        else:
            left_padding = padding - right_padding

        padded_element = np.pad(element, ((0, 0), (right_padding, left_padding)), constant_values=(1, 1))
        padded_elements.append(padded_element)

    return np.array(padded_elements)

# gets individual symbols, letters, and letters in whole image
def get_individual_elements(image):
    elements = list()

    # Iterate over columns
    i = 0
    n = image.shape[1]

    # separates elements by columns of whitespace pixels
    while i < n:
        new_element = list()

        # While empty column
        while i < n and np.all(image[:, i] == 1):
            i += 1

        # While not empty column
        while i < n and np.any(image[:, i] < 1):
            new_element.append(image[:, i].copy())
            i += 1

        elements.append(new_element)

    # Remove empty element arrays
    elements = [element for element in elements if len(element) > 0]

    # Change from list of columns to normal image
    return [np.transpose(elements) for elements in elements]


if __name__ == "__main__":
    image_path = "/Users/khanhtran/Downloads/Drawing.jpeg"
    elements = split(image_path)

    for element in elements:
        plt.imshow(element, cmap='gray')
        plt.show()

