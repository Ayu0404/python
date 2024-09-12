t1=10.0
t2=12.0
t3=15.0
t4=20.0
total_amt=0.0

amt=float(input('Enter the total bill amount '))
tip=float(input(f'How much percent of Total Bill Amount will you tip - {t1}, {t2}, {t3} or {t4}. '))
num_friends=int(input('The total amount will be divided among how many people? '))

match tip:
    case 10:
        total_amt=amt+(t1/100)*amt
    case 12:
        total_amt=amt+(t2/100)*amt
    case 15:
        total_amt=amt+(t3/100)*amt
    case 20:
        total_amt=amt+(t4/100)*amt

individual_amt = total_amt/num_friends
print(f'Total Amount to be paid by you - {round(individual_amt,2)}')
