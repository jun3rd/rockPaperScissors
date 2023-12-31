import random

def play():
    user = input(f"'r' for rock, 'p' for paper, 's' for scissors?")
    computer = random.choice(['r', 'p', 's'])
    print(f"You: {user}; computer: {computer}")
    if user == computer:
        return 'It\'s a tie'
    
    # r > s, s > p, p > r
    if isWin(user, computer):
        return 'You won!'

    return 'You lost.'

def isWin(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or \
        (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
        return True

    return False

print(play())
