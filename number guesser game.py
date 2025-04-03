import random

while True:
    x, y = map(int, input('choose ur range: ').split())
    z = random.randint(x, y)
    player1 = int(input('guess the no: '))
    chances=4
    while player1 != z and chances>=1:
        chances-=1
        if player1 > z:
            print('ur guess is too high')
        elif player1 < z:
            print('ur guess too low')
        player1 = int(input('try again: '))
    if player1==z:
        print('u r correct')
    else:
        print('u lost. the correct ans was '+str(z))
    play_again=input('wanna play again: ')
    if play_again != 'yes':
        print('bye')
        break