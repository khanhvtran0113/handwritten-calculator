import os
import pickle
import shutil
import numpy as np
from _util import load_image, normalize_images, one_hot_encode, PICKLE_FOLDER

IMAGES_FOLDER = "/Users/khanhtran/Desktop/archive/symbols/"
TRAIN_SIZE, VAL_SIZE, TEST_SIZE = 0.8, 0.1, 0.1
# SEED set to 1 to achieve reproducibility
SEED = 1

def main():
    # Load images
    images, labels = load_images()

    # Normalize images
    images = normalize_images(images)

    # Split data
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(images, labels)

    # Save data
    shutil.os.makedirs(PICKLE_FOLDER, exist_ok=True)
    save(X_train, "X_train.pkl")
    save(X_val, "X_val.pkl")
    save(X_test, "X_test.pkl")

    save(y_train, "y_train.pkl")
    save(y_val, "y_val.pkl")
    save(y_test, "y_test.pkl")


def save(data, filename):
    with open(PICKLE_FOLDER+filename, 'wb') as file:
        pickle.dump(data, file)

def load_images():
    images, labels = list(), list()

    # Loop through each image
    for label in os.listdir(IMAGES_FOLDER):
        for image in os.listdir(IMAGES_FOLDER + label):
            images.append(load_image(IMAGES_FOLDER + label + "/" + image))
            labels.append(label)

    # Convert lists to numpy arrays
    images = np.array(images)
    labels = np.array(labels)

    return images, labels

def split_data(images, labels):
    """
    This function implements a more simplistic, manual spitting
    algorithm in order to be more memory efficient.
    """
    n = len(images)
    train_count = int(n*TRAIN_SIZE)
    val_count = int(n*VAL_SIZE)
    test_count = int(n*TEST_SIZE)

    # Create random list of indices for given size
    shuffled_indices = np.random.default_rng(SEED).permutation(n)
    train_indices = shuffled_indices[:train_count]
    val_indices = shuffled_indices[train_count:train_count+val_count]
    test_indices = shuffled_indices[train_count+val_count:]

    # Create train/val/test split using these indices
    X_train = images[train_indices]
    X_val = images[val_indices]
    X_test = images[test_indices]

    y_train = labels[train_indices]
    y_val = labels[val_indices]
    y_test = labels[test_indices]

    # One-hot encode labels
    y_train = one_hot_encode(y_train)
    y_val = one_hot_encode(y_val)
    y_test = one_hot_encode(y_test)

    return X_train, X_val, X_test, y_train, y_val, y_test

if __name__ == "__main__":
    main()
