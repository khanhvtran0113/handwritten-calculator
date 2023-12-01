from split import split
from predict import predict
from solve import parse, change_number_base, solve
import matplotlib.pyplot as plt


def main(image_path):
    # Number base of input image
    base = 16

    # Split image into individual elements
    elements = split(image_path)

    # Predict on elements
    symbols = predict(elements)

    # Parse symbols list to join elements belonging to single number
    parsed_symbols = parse(symbols)

    # Convert list of parsed symbols into decimal from number base of input imgae
    parsed_symbols_with_base = change_number_base(parsed_symbols, base)

    # Solve
    answer = solve(parsed_symbols_with_base)

    print(symbols)
    print(answer)


if __name__ == "__main__":
    image_path = "/Users/khanhtran/Downloads/Hex_equation_drawing.png"
    main(image_path)
