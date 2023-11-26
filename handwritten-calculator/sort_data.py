import shutil
import os


INPUT_FOLDER = "/Users/khanhtran/Desktop/archive/extracted_images/"
OUTPUT_FOLDER = "/Users/khanhtran/Desktop/archive/symbols/"


def main(symbols: dict):

    # Create base folder
    shutil.os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Copy numbers
    for number in symbols["numbers"]:
        print(f"Copying entire {number} folder")
        shutil.rmtree(OUTPUT_FOLDER + number, ignore_errors=True)
        shutil.copytree(INPUT_FOLDER + number, OUTPUT_FOLDER + number)

    # Copy operations:
    for operation in symbols["operations"]:
        print(f"Copying entire {operation} folder")
        shutil.rmtree(OUTPUT_FOLDER + operation, ignore_errors=True)
        shutil.copytree(INPUT_FOLDER + operation, OUTPUT_FOLDER + operation)

    # Copy letters
    for letter in symbols["letters"]:
        print(f"Copying entire {letter} folder")
        shutil.rmtree(OUTPUT_FOLDER + letter, ignore_errors=True)
        """
        For the letters, there exists both upper and lower case.
        """
        if os.path.exists(INPUT_FOLDER + letter):
            shutil.copytree(INPUT_FOLDER + letter, OUTPUT_FOLDER + letter)
        elif os.path.exists(INPUT_FOLDER + letter.upper()):
            shutil.copytree(INPUT_FOLDER + letter.upper(), OUTPUT_FOLDER + letter)


if __name__ == "__main__":
    symbols = dict()

    symbols["numbers"] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols["operations"] = ["+", "-", "forward_slash"]
    symbols["letters"] = ["a", "b", "c", "d", "e", "f", "x"]

    main(symbols)

