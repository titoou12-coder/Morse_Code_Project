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

# TRY THIS


def mode_selection():
    if mode_choice == 1:
        print("you are in learning mode")
    elif mode_choice == 2:
        print("you are in translation mode")
    elif mode_choice == 3:
        print("you are in game mode")
    else:
        print("invalid slection. Try again")


mode_selection({mode_choice})


# def learning_1(key):
#     print("Enter letter:")
#     letter = input()
#     print(morse[f"{letter}"])

# # START


# # IDLE
# modes = int(input("""
#                 SELECT A MODE
#                     MODE 1: Leaning Mode
#                     MODE 2: Translation Mode
#                     MODE 3: Game Mode

#                 Please enter 1, 2 or 3 for the corresponding mode.

#               """))
# try:
#     while modes < 1 or modes > 3:  # MODES 2 AND 3 DO NOT WORK YET
#         raise Exception
# except:
#     print("INVALID INPUT ENTERED: PLEASE ENTER 1, 2 OR 3")
#     modes = int(input("""
#                 SELECT A MODE
#                     MODE 1: Leaning Mode
#                     MODE 2: Translation Mode
#                     MODE 3: Game Mode

#                 Please enter 1, 2 or 3 for the corresponding mode.

#               """))
# else:
#     # HAVENT DEVELOPPED MODE 2 OR 3 YET
#     if modes == 2 or modes == 3:
#         assert modes == 2 or modes == 3, "You have selected either Translation or Game Mode"
#         modes = int(input("""
#                 SELECT A MODE
#                     MODE 1: Leaning Mode
#                     MODE 2: Translation Mode
#                     MODE 3: Game Mode

#                 Please enter 1, 2 or 3 for the corresponding mode.

#               """))
#     # LEARNING MODE
#     elif modes == 1:
#         print("You have entered Learning Mode!")
#         alpha_to_morse = int(input("""
#                                What mode would you like to learn in:
#                                     MODE 1: Letter to Morse
#                                     MODE 2: Morse to Letter

#                                 Please, enter 1 or 2.

#                                 """))
#         try:
#             while alpha_to_morse <= 0 or alpha_to_morse > 2:
#                 raise Exception
#         except:
#             print("Invalid mode entered: Please enter 1 or 2")
#         else:
#             if alpha_to_morse == 1:
#                 print("You have chosen to go from letters to morse code!")
#                 letter = input("Enter a letter to get translated: ")
#                 print(morse[f"{letter}"])
