#Def guess is for user - 02
#def computer_guess is for computer - 03



import random

def guess(x):
    random_number= random.randint(1,x)
    guess=0
    while guess != random_number:
        guess =int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number:
            print('Number too low')
        elif guess > random_number:
            print('Number too high')
    print(f"Correct,The answer is {random_number}. You win")

def computer_guess(x):
    low=1
    high= x
    feedback= ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # low could also equal high
        feedback= input(f'Is {guess} too high(h), too low (l) or correct (c)')
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1

    print (f'Correct, Computer guessed the number {guess} correctly. Computer wins')



computer_guess(10)

#Try to automate function where is doesnt require feedback it just compare number selected to the range itself and continues to guess.