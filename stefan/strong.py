password = input('pass?\n')
points = 0
from random import randint

if len(password) >= 5:
    points += 3

for x in [ '!', '@', '$', '%', '^', '&', '*' ]:
    if x in password:
        points += 3

for x in [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]:
    if x in password:
        points += 3

if not password.islower() and not password.isupper():
    points += 3

strong = 'S'

for char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '$', '%', '^', '&', '*' 'A', 'm', 'S', 'c', 'b', 'Z', 'Y', 'W', 'O']:
       pos = randint(0, len(strong) - 1)
       strong = "".join((strong[:pos], char, strong[pos:]))

print('\n rate: ' + str(points) + ' out of 57 (concludes all numbers, special chars  etc)\n')
print('if your password is >= 10, that means its good. >=20 and up its godlike\n')
print('strongly high suggested password: ' + strong)
better = input('want a better password?\n')

if better.lower() == 'y':
    betterpass = password

    for char in ['#', '2', '%', 'W', 'S']:
       pos = randint(0, len(betterpass) - 1)
       betterpass = "".join((betterpass[:pos], char, betterpass[pos:]))
    
    print(betterpass)
    print('Added at random positions special chars, numbers, and uppercase letters.')

