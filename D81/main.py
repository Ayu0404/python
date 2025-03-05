from code import MORSE_CODE

str = input("Enter text").strip().upper()
print(str)
ans = ''
for s in str:
    if s in MORSE_CODE:
        ans += MORSE_CODE[s]

print(ans)

# neat version
# print(' / '.join(' '.join(MORSE_CODE.get(c, '')
#       for c in word) for word in str.split()))
