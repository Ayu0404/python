DECADE=10
MONTHS=12
WEEK=4
DAYS=7

def print_range(rows,cols,rem):
    for __ in range(rows):
        for __ in range(cols):
            print('•',end=' ')
        print()
    
    if rem>0:
        for __ in range(rem):
            print('•',end=' ')

def get_life_calender(age):
    print('Every • represents a year of your life lived.')
    if(age<=10):
        print_range(1,age,0)
    else:
        rows=int(age/DECADE)
        rem=int(age%DECADE)
        print_range(rows,DECADE,rem)


def get_months_calender(age):
    months=age*MONTHS
    print(f'\n{age} years means {months} months.')
    rows=int(months/12)
    rem=int(months%12)
    print_range(rows,MONTHS,rem)

def get_weeks_days(age):
    weeks=age*MONTHS*WEEK
    days=weeks*DAYS
    print(f'{weeks} weeks.')
    print(f'{days} days.')


age=int(input('Enter your age '))
get_life_calender(age)
get_months_calender(age)
get_weeks_days(age)