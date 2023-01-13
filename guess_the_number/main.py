from random import randint

while True:
    n = int(input('Enter number of tries(more - easier): '))

    number = randint(1, 100)

    for i in range(n):
        guess = int(input('Enter your guess: '))
        if guess < number:
            print('Too low!')
        elif guess > number:
            print('Too high!')
        else:
            print('You win!')
            break
    else:
        print('You lost!')

    play = input('Play again? [Y/N]').strip().lower()
    if play in ('y', 'yes'):
        continue
    else:
        break
