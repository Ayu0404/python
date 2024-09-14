import random as r

choices=[
    '''
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    ''',
    '''
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    ''',
    '''

    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
]

def result(p1_idx,p2_idx):
    if p1_idx == 0 and p2_idx == 1 or \
    p1_idx == 1 and p2_idx == 2 or \
    p1_idx == 2 and p2_idx == 0:
        print('The Computer WINS!')
    elif p1_idx == p2_idx:
        print('It is a draw.')
    else:
        print('Player 1 WINS!')


def rock_paper_scissors():
    print('WELCOME TO ROCK PAPER SCISSORS. ')
    try:
        p1=int(input('Enter 1 for Rock, 2 for Paper or 3 for scissors. '))
        p1_idx=p1-1
        print(choices[p1_idx])
        print('The computer chooses...')
        p2=r.randint(0,2)
        print(choices[p2])
    except Exception as e:
        print(e)
    else:
        result(p1_idx,p2)
    finally:
        print('Game over.')


rock_paper_scissors()
