import random, sys

print('ROCK, PAPER, SCISSORS')

#These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:
    print("%s Wins, %s Losses, %s Ties "%(wins,losses,ties))
    while True:
        print("Enter your move : (r)ock (p)aper (s)cissors or (q)uit ")
        playermove = input()
        if playermove == 'q':
            sys.exit()
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break
        print("Type one of r, p, s, or q.")

    #Display what the player chose:
    if playermove == 'r':
        print('ROCK versus ...')
    elif playermove == 'p':
        print('PAPER versus ...')
    elif playermove == 's':
        print('SCISSORS versus ...')

    #Display what the computer choose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove == 's'
        print('SCISSORS')

    #Display and record the win/loss/tie:
    if playermove ==  computerMove:
        print('It is a tie! ')
        ties = ties + 1
    elif playermove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playermove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playermove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playermove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playermove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playermove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1