import random as r

def lucky_draw():
    names=input('Enter the names who will pay the bill for tonight\'s dinner. ' )
    names=names.split(',')
    
    rand=r.randint(0,len(names)-1)
    print(f'{names[rand].strip()} will pay tonight\'s bill. ')
    
    # Pass the list in choice(). It performs line 7 and 8 in one function.
    print(f'{r.choice(names)} will pay tonight\'s bill. ')


lucky_draw()