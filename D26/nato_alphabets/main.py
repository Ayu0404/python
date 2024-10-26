import pandas

#TODO 1. Create a dictionary :
data=pandas.read_csv('D26/nato_alphabets/nato_phonetic_alphabet.csv')
phonetic_dict= {row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    name=input('Enter your name ').upper()
    try:
        phonetics=[phonetic_dict[letter] for letter in name]
    except KeyError :
        print(f'Only alphabets are acceptable.')
        generate_phonetic()
    else:
        print(phonetics)

generate_phonetic()