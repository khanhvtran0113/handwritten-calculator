import tensorflow as tf
import numpy as np

from _util import MODEL_FOLDER, ONE_HOT_TO_LABEL, load_image, normalize_images


def predict(normalized_images):

    # Get model
    model = tf.keras.models.load_model(MODEL_FOLDER)

    # Predict
    y = model.predict(normalized_images)

    # Convert to labels
    return get_labels(y)


def get_labels(y):
    one_hots = [np.argmax(yi) for yi in y]
    return [ONE_HOT_TO_LABEL[one_hot] for one_hot in one_hots]


if __name__ == "__main__":
    # Load image to predict on
    image = load_image("")
    normalized_images = normalize_images(np.array([image]))

    labels = predict(normalized_images)
    print(labels)
