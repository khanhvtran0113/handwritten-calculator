from split import split
from predict import predict
from solve import solve
import matplotlib.pyplot as plt


def main(image_path):

    # Split image into individual elements
    elements = split(image_path)

    for element in elements:
        plt.imshow(element, cmap='gray')
        plt.show()

    # Predict on elements
    symbols = predict(elements)

    # Solve
    anwser = solve(symbols)

    print(symbols)
    print(anwser)


if __name__ == "__main__":
    image_path = "/Users/khanhtran/Downloads/Drawing.jpeg"
    main(image_path)
