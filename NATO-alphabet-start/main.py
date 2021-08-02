# TODO 1. Create a dictionary in this format:
import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
data = file.to_dict()
dictionary = {row.letter: row.code for (index, row) in file.iterrows()}
print(dictionary)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_meanings():
    user_input = input("Enter the word/sentence: ").upper()
    try:
        list_of = [dictionary[letter] for letter in user_input]
    except KeyError:
        print("Sorry only alphabets are allowed.")
        generate_meanings()
    else:
        print(list_of)


generate_meanings()
