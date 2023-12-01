operations = ['forward_slash', 'x', '+', '-']
def parse(symbols):
    parsed_symbols = []
    i = 0
    while i < len(symbols):
        if symbols[i] in operations:
            parsed_symbols.append(str(symbols[i]))
            i += 1
        else:
            number = ""
            while i < len(symbols) and symbols[i] not in operations:
                number += symbols[i]
                i += 1
            parsed_symbols.append(number)
    return parsed_symbols

def change_number_base(parsed_symbols, base):
    parsed_symbols_with_base = []
    for symbol in parsed_symbols:
        if symbol in operations:
            parsed_symbols_with_base.append(symbol)
        else:
            # convert to base 10
            parsed_symbols_with_base.append(int(symbol, base))
    return parsed_symbols_with_base
def solve(parsed_symbols_with_base):
    equation_to_string = ''.join(str(element) for element in parsed_symbols_with_base)
    try:
        solution = eval(equation_to_string)
    except Exception as e:
        print(f"Caught an exception: {e}")
    else:
        return solution

if __name__ == "__main__":
    example = ['c', '7', '+', '5', '3']
    base = 16
    parsed_symbols_with_base = change_number_base(parse(example), base)
    answer = solve(parsed_symbols_with_base)
    print(answer)