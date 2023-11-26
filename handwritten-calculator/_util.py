import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical

LABEL_TO_ONE_HOT = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
    '+': 16, '-': 17, 'forward_slash': 18, 'x': 19
}
ONE_HOT_TO_LABEL = {value: key for key, value in LABEL_TO_ONE_HOT.items()}
CLASS_COUNT = len(LABEL_TO_ONE_HOT)

PICKLE_FOLDER = "/Users/khanhtran/Desktop/handwritten-calculator/pickle/"
MODEL_FOLDER = "/Users/khanhtran/Desktop/handwritten-calculator/model/"

def load_image(filepath):
    # Load image as grayscale and resize to 75x75
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    # dimensions based on images from dataset in README
    return cv2.resize(img, (75, 75))


def normalize_images(images):
    # Normalize pixel range to [0, 1]
    images = images / 255.0

    """
    Add channel dimension to image

    Most CNN layers expect the input to have a channel dimension
    which grayscale images lack due to single channel. 
    """
    return np.expand_dims(images, axis=-1)

# Encodes labels into one-hot vectors
def one_hot_encode(labels):
    y = [LABEL_TO_ONE_HOT[label] for label in labels]
    return to_categorical(y, num_classes=CLASS_COUNT)
