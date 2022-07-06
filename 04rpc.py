import random

def play():
    user = input("Select your choice ?'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer :
        return 'draw'

# rules r > s, p > r , s > p
    if is_win(user, computer):
        return 'You won'

    return 'You lost'


def is_win(player, opponent):
    # return true id player wins
    # rules r > s, p > r , s > p
    if (player == 'r' and opponent == 's' ) or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(play())

### Add a score board
### Add a loop where it is first to 3 wins the round
### may add more user function
### look at true and false statements, loops and conditonal statements