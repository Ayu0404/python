a=4
b=5

# Swapping without using a third variable
c=a
a=b
b=c
print(f'a: {a}, b: {b}')

# Swapping using a third variable
a=a+b
b=a-b
a=a-b
print(f'a: {a}, b: {b}')