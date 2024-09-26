import pandas as pd

start_alpha = pd.read_csv("nato_phonetic_alphabet.csv")

# Creatibng a dictionary
phonetic_dict = {row.letter: row.code for (index, row) in start_alpha.iterrows()}
print(dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()