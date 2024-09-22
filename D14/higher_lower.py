import random as r
from data import data


def higher_lower():
    size=len(data)
    high_score=0
    is_playing=True

    while is_playing:
        print('Who is more popular on Instagram? ')
        index1=r.randint(1,size)
        index2=r.randint(1,size)
        print(f'1. {data[index1]['name']}: a {data[index1]['description']}, from {data[index1]['country']}.')
        print(f'2. {data[index2]['name']}: a {data[index2]['description']}, from {data[index2]['country']}.')
        ans=int(input('Enter your choice 1 or 2? '))

        if (data[index1]['follower_count']>data[index2]['follower_count']) and (ans==1):
            high_score+=1
            print(f'Your High score: {high_score}')
        else:
            is_playing=False
            print('You lose.')
    


higher_lower()