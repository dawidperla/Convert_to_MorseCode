from tkinter import *

# # TODO: Create dictionary with Code morse'a signs
#
#
# signs = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
#          "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
#          "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
#          "Ą": ".-.-",
#          "Ć": "-.-..", "Ę": "..-..", "Ł": ".-..-", "Ń": "--.--", "Ó": "---.", "Ś": "...-...", "Ź": "--..-.",
#          "Ż": "--..-",
#          }
#
#
# # TODO: Send prompt to user with ask name
#
#
# userInput = input("Podaj swoje imię: ")
#
#
# # TODO: Split each letter and send to list
#
#
# letters = [x for x in userInput]
#
#
# # TODO: asign letter to code morse'a
#
#
# lettersAfterCode = []
#
# for letter in letters:
#     letterInMorseCode = signs[letter.upper()]
#     lettersAfterCode.append(letterInMorseCode)
#
# print(letters)
# print(lettersAfterCode)


# TODO: Create GUI with Label, textarea, button

FONT_NAME = "Courier"

window = Tk()
window.title("ASCI to Morse'a Code Converter")
window.config(padx=50, pady=50)
label = Label(text="Podaj tekst do konwersji", font=(FONT_NAME, 10, "bold"))
label.grid(column=0, row=0)
text = Text(height=2,)
text.grid(column=1, row=0)
label = Label(text="Tekst w kodzie Morse'a", font=(FONT_NAME, 10, "bold"))
label.grid(column=0, row=1)
text = Text(height=2,)
text.grid(column=1, row=1, pady=10)
button = Button(text="Tłumacz", highlightthickness=0, width=91)
button.grid(column=1, row=2, pady=10)
window.mainloop()
