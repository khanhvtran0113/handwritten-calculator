from split import split
from predict import predict
from solve import parse, change_number_base, solve
import matplotlib.pyplot as plt
import io
import base64

def handleBase64Image(base64_image, base):

    # Decode the Base64 string into bytes
    image_bytes = base64.b64decode(base64_image.split(',')[1])

    # Use the io module to create a BytesIO object
    image_buffer = io.BytesIO(image_bytes)

    # Main can handle a path or buffer
    return main(image_buffer, base)

def main(image, base):
    """
    Image parameter can take either image buffer or path.
    """

    # Split image into individual elements
    elements = split(image)

    # Predict on elements
    symbols = predict(elements)

    # Parse symbols list to join elements belonging to single number
    parsed_symbols = parse(symbols)

    # Convert list of parsed symbols into decimal from number base of input imgae
    parsed_symbols_with_base = change_number_base(parsed_symbols, base)

    # Solve
    answer = solve(parsed_symbols_with_base)

    return answer, symbols


if __name__ == "__main__":
    base = 16
    image_path = "/Users/khanhtran/Downloads/Hex_equation_drawing.png"
    answer, symbols = main(image_path, base)
    print(symbols)
    print(answer)
