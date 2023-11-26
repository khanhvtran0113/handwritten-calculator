import cv2
import numpy as np
import matplotlib.pyplot as plt


def split(image_path):

    # Get image and resize
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    aspect_ratio = original_image.shape[1] / original_image.shape[0]  # width/height
    # resize to dimensions of images in dataset in README
    resized_image = cv2.resize(original_image, (int(75*aspect_ratio), 75))

    # Convert to numpy array and normalize
    normalized_image = np.array(resized_image) / 255.0

    # Get each part of expression
    elements = get_individual_elements(normalized_image)

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
