def is_leap_year(year):
    if year%4==0:
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else: 
        return False


def days_in_month(month,is_leap):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap and month == 2:
        return days[month-1]+1
    return days[month-1]


year=int(input('Enter the year '))
month=int(input('Enter the month (1 for January, 2 for February, ..... 12 for December. )'))
is_leap=is_leap_year(year)
print(days_in_month(month,is_leap))