import random as r
import string as s

NUMBERS=s.digits
LETTERS=s.ascii_letters
SPECIAL_CHARACTERS="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def generate_password(length,nums,special_char):    
    password=[]
    for __ in range(0,nums):
        password.append(r.choice(NUMBERS))
    for __ in range(0,special_char):
        password.append(r.choice(SPECIAL_CHARACTERS))
    
    letter_len=length-nums-special_char
    for __ in range(0,letter_len):
        password.append(r.choice(LETTERS))
    
    r.shuffle(password)
    print(''.join(password))    


length=int(input('Enter the length of your password '))
nums=int(input('How many numbers to include in your password? '))
special_char=int(input('How many special characters to include in your password? '))

generate_password(length,nums,special_char)