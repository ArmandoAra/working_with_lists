data_morse_value = {
    "A": "● ▬",
    "B": "▬ ● ● ●",
    "C": "▬ ● ▬ ●",
    "D": "▬ ● ●",
    "E": "●",
    "F": "● ● ▬ ●",
    "G": "▬ ▬ ●",
    "H": "● ● ● ●",
    "I": "● ●",
    "J": "● ▬ ▬ ▬",
    "K": "▬ ● ▬",
    "L": "● ▬ ● ●",
    "M": "▬ ▬",
    "N": "▬ ●",
    "O": "▬ ▬ ▬",
    "P": "● ▬ ▬ ●",
    "Q": "▬ ▬ ● ▬",
    "R": "● ▬ ●",
    "S": "● ● ●",
    "T": "▬",
    "U": "● ● ▬",
    "V": "● ● ● ▬",
    "W": "● ▬ ▬",
    "X": "▬ ● ● ▬",
    "Y": "▬ ● ▬ ▬",
    "Z": "▬ ▬ ● ●",
    "1": "● ▬ ▬ ▬ ▬",
    "2": "● ● ▬ ▬ ▬",
    "3": "● ● ● ▬ ▬",
    "4": "● ● ● ● ▬",
    "5": "● ● ● ● ●",
    "6": "▬ ● ● ● ●",
    "7": "▬ ▬ ● ● ●",
    "8": "▬ ▬ ▬ ● ●",
    "9": "▬ ▬ ▬ ▬ ●",
    "0": "▬ ▬ ▬ ▬ ▬",
}

print("####  Welcome to the Morse Code Translator ####")
print("#### Only Letters and Numbers will be translate ####")
user_word = input("Introduce a text to convert in morse: ").upper()
user_word_list = user_word.split()

words_list = []
morse = ''

for item in range(len(user_word_list)):
    words_list.append([data_morse_value[letter] for letter in user_word_list[item] if letter in data_morse_value])

for word_index in range(len(words_list)):
    for letter in words_list[word_index]:
        morse += f'{letter}   '
    morse += '    '

print(user_word)
print(morse)








