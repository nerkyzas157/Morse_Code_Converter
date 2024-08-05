MORSE_ALPHABET = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": ".---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    '"': ".-..-.",
    "&": ".-...",
    "@": ".--.-.",
    "$": "...-..-",
    "=": "-...-",
    "!": "-.-.--",
    "+": ".-.-.",
    ";": "-.-.-.",
    "_": "..--.-",
    " ": "/",
}


def text_to_morse(text):
    output = ""
    for char in text:
        for i, v in MORSE_ALPHABET.items():
            if i == char:
                output += v + " "
            if char not in MORSE_ALPHABET.keys():
                print(f"There was a misunderstood character: {char}")
    return output


def morse_to_text(morse_code):
    output = ""
    morse_value = ""
    for char in morse_code:
        if char != " ":
            morse_value += char
        else:
            if morse_value not in MORSE_ALPHABET.values():
                print(f"There was a misunderstood character: {morse_value}")
                continue
            for i, v in MORSE_ALPHABET.items():
                if v == morse_value:
                    output += i
            morse_value = ""
    return output


def main():
    print("Hello and welcome to Morse Code Converter!")
    request = input(
        "Type 'morse' to convert text to morse code.\nType 'text' to convert morse code to text.\n"
    )
    if request.lower() == "morse":
        text = input("Please enter text: ")
        print(
            f"Here's your text converted to morse code: {text_to_morse(text.upper())}"
        )
    if request.lower() == "text":
        morse_code = input("Please enter morse code: ")
        morse_code += " "
        print(f"Here's your morse code converted to text: {morse_to_text(morse_code)}")


if __name__ == "__main__":
    main()
