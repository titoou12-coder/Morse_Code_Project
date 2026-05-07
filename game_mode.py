import random

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

# word bank of 30 words
# select letters - morse or morse - letters
# select short game (5 words) or long game (10 words)
# shuffle word bank -> select first 5 or 10
# keep score


words = ["birthday", "measurement", "lady", "king", "statement", "fajita", "banjo", "television", "restaurant", "country", "revolution", "library", "initiative",
         "application", "photo", "teaching", "description", "pizza", "news", "exams", "wedding", "affair", "question", "payment", "exquisite", "friendship", "depth", "year", "kazoo"]

random.shuffle(words)


def guess_the_morse():
    score = 0
    question_number = int(input("How many questions would you like?: "))
    for i in range(question_number):
        print(words[i])
        answer = " ".join(morse[letter] for letter in words[i])
        response = input()
        if response == answer:
            score += 1
            print("Correct! \n")
        else:
            print("Incorrect \nThe correct answer is:", answer, "\n")
    print("Your final score is", score, "/", question_number)
    return True


guess_the_morse()
