# TODO: Create dictionary with Code morse'a signs


signs = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
         "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
         "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "Ą": ".-.-",
         "Ć": "-.-..", "Ę": "..-..", "Ł": ".-..-", "Ń": "--.--", "Ó": "---.", "Ś": "...-...", "Ź": "--..-.",
         "Ż": "--..-",
         }


# TODO: Send prompt to user with ask name


userInput = input("Podaj swoje imię: ")


# TODO: Split each letter and send to list


letters = [x for x in userInput]


# TODO: asign letter to code morse'a


lettersAfterCode = []

for letter in letters:
    letterInMorseCode = signs[letter.upper()]
    lettersAfterCode.append(letterInMorseCode)

print(letters)
print(lettersAfterCode)
