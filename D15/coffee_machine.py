from data import MENU, RESOURCES,ACCEPTED_COINS, MESSAGE

def calculate_payments(pennies,nickles,dimes,quarters,order):
    cost=MENU[order]['cost']
    total_amount=ACCEPTED_COINS['penny']*pennies + ACCEPTED_COINS['nickle']*nickles + ACCEPTED_COINS['dime']*dimes + ACCEPTED_COINS['quarter']*quarters

    if cost>total_amount:
        return -1
    elif cost<total_amount:
        print(f'Total amount paid: {round(total_amount,2)}')
        return total_amount-cost
    else:
        return 0


def get_resources():
    print(f'Water: {RESOURCES["water"]} ml')
    print(f'Milk: {RESOURCES["milk"]} ml')
    print(f'Coffee: {RESOURCES["coffee"]} gms')


def prepare_drink(order):
    if order == 'espresso':
        RESOURCES["water"]-=MENU[order]['ingredients']['water']
        RESOURCES["coffee"]-=MENU[order]['ingredients']['coffee']
    else:
        RESOURCES["water"]-=MENU[order]['ingredients']['water']
        RESOURCES["milk"]-=MENU[order]['ingredients']['milk']
        RESOURCES["coffee"]-=MENU[order]['ingredients']['coffee']
    
    print(f'{order} prepared. Enjoy your drink.')
    get_resources()


def should_prepare_coffee(order):
    if order=='espresso' and \
        RESOURCES["water"] >= MENU[order]['ingredients']['water'] and \
            RESOURCES["coffee"]>=MENU[order]['ingredients']['coffee']:
        return True
    
    if (order=='latte' or  order=='cappuccino') and \
        RESOURCES["water"] >= MENU[order]['ingredients']['water'] and \
            RESOURCES["coffee"]>=MENU[order]['ingredients']['coffee'] and \
                RESOURCES["milk"]>=MENU[order]['ingredients']['milk']:
        return True

    return False


def coffee_machine():
    is_working=True

    while is_working:
        order=input('What would you like? (espresso/latte/cappuccino)? ').lower()
        
        if order == 'resources':
            get_resources()
        
        if order == 'off':
            is_working=False
            print('Machine turned off.')

        elif should_prepare_coffee(order):    
            print(f'Pay ${MENU[order]['cost']}. We only accept coins - pennies, nickles, dimes and quarters.')
            pennies=int(input('Enter Pennies: '))
            nickles=int(input('Enter Nickles: '))
            dimes=int(input('Enter Dimes: '))
            quarters=int(input('Enter Quarters: '))
            
            balance=calculate_payments(pennies,nickles,dimes,quarters,order)
            if balance==-1:
                is_working=False    
                print(f'{MESSAGE['failure']}')
            elif balance==0:
                print(MESSAGE['success'])
                prepare_drink(order)
            else:
                print(f'{MESSAGE['success']} Balance amount: ${round(balance,2)}')
                prepare_drink(order)

        elif RESOURCES["water"] < MENU[order]['ingredients']['water']:
            is_working=False
            print('Not enough water. Try again later.')

        elif RESOURCES["milk"] < MENU[order]['ingredients']['milk']:
            is_working=False
            print('Not enough milk. Try again later.')

        elif RESOURCES["coffee"] < MENU[order]['ingredients']['coffee']:
            is_working=False
            print('Not enough coffee. Try again later.')



coffee_machine()
