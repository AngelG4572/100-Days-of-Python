import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

print("Welcome to the Nato Alphabet Converter!")


def nato_word():
    user_word = input("Enter a word: ").upper()
    try:
        user_word_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_word()
    else:
        print(user_word_list)


nato_word()
