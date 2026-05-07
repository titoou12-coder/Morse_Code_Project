# Alphabet to morse code dictionary
morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
    "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
    "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",

    " ": "/",

    ".": "\n"
}

# Morse code to Alphabet dictionary
reverse_morse = {value: key for key, value in morse.items()}


# Input letter, Output morse of letter
# Type "quit" to quit this mode
def learning_1():
    print("Enter letter: ")
    letter = input().lower()
    if letter == "quit":
        return False

    if letter in morse:
        print(morse[f"{letter}"])
    else:
        print("Invalid input. Try again")
    return True


while learning_1():
    pass


# Input a letter in morse, Output letter
# Type "///" to quit this mode
def learning_2():
    print("Enter morse: ")
    morse_input = input()
    if morse_input == "///":
        return False

    if morse_input in reverse_morse:
        print(reverse_morse[morse_input])
    else:
        print("Invalid morse. Try again")
    return True


while learning_2():
    pass
