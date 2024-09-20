import random as r
MAX_SCORE=21

def calculate_score(cards):
    #Blackjack condition
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>MAX_SCORE:
        cards.remove(11)
        cards.append(1) 
    return sum(cards)


def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return r.choice(cards)


def compare(user_score,dealer_score):
    if user_score==dealer_score:
        return 'Draw.'
    elif dealer_score==0:
        return 'You lose. Dealer has a blackjack.' 
    elif user_score==0:
        return 'BlackJack. You won.'
    elif user_score>MAX_SCORE:
        return 'You went over 21. You lose.'
    elif dealer_score>21:
        return 'Dealer went over 21. You win.'
    elif user_score>dealer_score:
        return 'You won.'
    else: return 'You lose.'
    

def blackjack():
    user_cards=[]
    dealer_cards=[]
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    # For user
    while not is_game_over:
        user_score=calculate_score(user_cards)
        dealer_score=calculate_score(dealer_cards)

        print(f'Your cards {user_cards}. Your score is: {user_score}.')
        print(f'Dealer First Card: {dealer_cards[0]}')

        if user_score==0 or user_score>MAX_SCORE or dealer_cards==0:
            is_game_over=True
        else:
            choice=input('Draw another card? Y or N. ').upper()
            if choice=='Y':
                user_cards.append(deal_card())
            else:
                is_game_over=True

    # For dealer
    while dealer_score!=0 and dealer_score<17:
        dealer_cards.append(deal_card())
        dealer_score=calculate_score(dealer_cards)
    
    print(f'Your final hand {user_cards} and final score {user_score}')
    print(f'Dealer\'s final hand {dealer_cards} and final score {dealer_score}')
    print(compare(user_score,dealer_score))


blackjack()


is_play_again=input('Do you want to play again? Y or N. ').upper()
if is_play_again=='Y':
    blackjack()
else:
    print('Goodbye.')
