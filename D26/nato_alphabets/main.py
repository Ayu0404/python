import pandas

#TODO 1. Create a dictionary :
data=pandas.read_csv('Day26/nato_alphabets/nato_phonetic_alphabet.csv')
phonetic_dict= {row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name=input('Enter your name ').upper()
phonetics=[phonetic_dict[letter] for letter in name]
print(phonetics)
