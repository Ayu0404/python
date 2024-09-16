import string

alphabets=list(string.ascii_lowercase)

def get_user_input():
    choice=input('Encode or Decode? ').lower()
    shift=int(input('Enter the key. '))
    word=input('Enter the your message. ').lower()
    cease_cipher(choice,shift,word)


def ask_again():
    again=input('Do you want to play again? Yes or No? ').lower()
    if again=='yes':
        return True
    else:
        return False


def cease_cipher(choice,shift,word):
    msg=''
    if choice=='encode':
        for w in word:
            msg+= alphabets[(shift%26)+alphabets.index(w)]
        print(f'Encrypted message is {msg}')
    
    if choice=='decode':
        for w in word:
            msg+= alphabets[abs((shift%26)-alphabets.index(w))]
        print(f'Decrypted message is {msg}')
    
    is_again=ask_again()
    if is_again:
        get_user_input()
    else:
        print('Goodbye')



get_user_input()