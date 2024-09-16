from constant import HANGMAN, HANGMAN_PICS, WORDS
import random as r

print(HANGMAN)


def play_hangman():
    word=r.choice(WORDS)
    guessed_word=[]
    is_end=False
    lives=len(HANGMAN_PICS)
    idx=0

    print(f'Guess the word.... The length of the mysterious word is {len(word)}.')
    for __ in range(0,len(word)):
        guessed_word.append('_')
    print(' '.join(guessed_word))
    
    while not is_end:
        guess=input('Guess a letter. ').lower()

        if guess in guessed_word:
            print(f'You have already guessed {guess}.')

        for i in range(0,len(word)):
            if guess==word[i]:
                guessed_word[i]=guess
        
        print(' '.join(guessed_word))
        
        if guess not in word:
            print(HANGMAN_PICS[idx])
            print(f'{guess} is not in the word. You lose a life.')
            idx+=1
            if idx==lives:
                is_end=True
                print('Game over. You lose.')

        
        if '_' not in guessed_word:
            is_end=True
            print('You Won !!')

play_hangman()
