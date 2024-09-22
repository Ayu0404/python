import random as r
EASY_ATTEMPTS=10
HARD_ATTEMPTS=5
RESULT={
    'HIGH':'high',
    'LOW':'low',
    'CORRECT':'correct'
}

def check_num(num,answer):
    if num>answer:
        return RESULT['HIGH']
    elif num<answer:
        return RESULT['LOW']
    else:
        return RESULT['CORRECT']


def guesses(attempts, answer):
    guess=[]
    while attempts>0:
        print(f'{attempts} attempts left.')
        num=int(input('Enter a number '))
        
        if num in guess:
            print('You have already guessed the number ')
        else:
            result=check_num(num,answer)

            if result=='high':
                print('Too high')
            elif result=='low':
                print('Too low')
            else:
                print('Correct. You guessed it. ')
                break
            
            guess.append(num)
            attempts-=1
    
    if attempts==0:
        print('You lose.')


def play_number_guessing():
    print('Guess the number between 1 and 100. ')
    choice = int(input('Enter 1 for easy or 2 for hard. '))
    answer=r.randint(1,100)
    if choice == 1:
        print(f'You have {EASY_ATTEMPTS} attempts to guess the number. ')
        guesses(EASY_ATTEMPTS,answer)
    else:
        print(f'You have {HARD_ATTEMPTS} attempts to guess the number. ')
        guesses(HARD_ATTEMPTS,answer)



play_number_guessing()