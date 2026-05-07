# Alphabet to morse code dictionary
morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
    "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
    "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
    "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",

    " ": "/",
    "": " ",

    ".": "\n"
}

# Morse code to Alphabet dictionary
reverse_morse = {value: key for key, value in morse.items()}


# Input letter, Output morse of letter
# Type "quit" to quit this mode
def translation_1():
    print("Enter phrase: ")
    phrase_input = input().lower()
    if phrase_input == "quit":
        return False
    else:
        translation = " ".join(morse[letter] for letter in phrase_input)
        print(translation)
    return True


while translation_1():
    pass


# Input a letter in morse, Output letter
# Type "///" to quit this mode
def translation_2():
    translation = []
    print("Enter morse: ")
    morse_input = input().lower()

    if morse_input == "///":
        return False
    else:
        split = morse_input.split(" ")
        for letter in split:
            if letter in reverse_morse:
                translated_letter = translation.append(reverse_morse[letter])
        print("".join(translation))
    return True


while translation_2():
    pass
