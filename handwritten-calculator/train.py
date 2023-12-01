import pickle
import os
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from _util import PICKLE_FOLDER, MODEL_FOLDER, CLASS_COUNT


def main():

    # load data
    X_train, X_val, X_test = load("X_train.pkl"), load("X_val.pkl"), load("X_test.pkl")
    y_train, y_val, y_test = load("y_train.pkl"), load("y_val.pkl"), load("y_test.pkl")

    # Get the model
    model = get_model()

    # Train the model
    train_model(model, X_train, y_train, X_val, y_val)

    # Check accuracy
    check_accuracy(model, X_test, y_test)
    
    # Save model
    os.makedirs(MODEL_FOLDER, exist_ok=True)
    model.save(MODEL_FOLDER)


def check_accuracy(model, X_test, y_test):
    _, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"Accuracy: {acc * 100} %")


def train_model(model, X_train, y_train, X_val, y_val):
    model.fit(X_train, y_train,
              epochs=7,
              batch_size=32,
              validation_data=(X_val, y_val)
              )


def get_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(75, 75, 1)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(CLASS_COUNT, activation='softmax'))

    # compile model
    opt = SGD(learning_rate=0.01, momentum=0.9)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return model



def load(filename):
    with open(PICKLE_FOLDER + filename, 'rb') as file:
        data = pickle.load(file)
    return data


if __name__ == "__main__":
    main()
