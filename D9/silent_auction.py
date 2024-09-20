players={}

def get_winner():
    winner=''
    amount=0
    for key,val in players.items():
        if val>amount:
            amount=val
            winner=key
    
    print(f'The winner is {winner} bidding at USD {amount}.')


def get_bidding_data():
    while True:
        person_name=input('Enter your name ')
        try:
            bid=int(input('Enter you bid price USD: '))
            players[person_name]=bid
        except ValueError as e:
            print(e)
            continue
        
        choice=input('Do you want to add another name? Yes or No. ').strip().lower()
        if choice in ('n','no'):
            break
    get_winner()
    print('Auction concluded.')

get_bidding_data()
