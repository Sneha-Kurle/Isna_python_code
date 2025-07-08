import random
actions=('paper','rock','scessor')
player='None'
computer=random.choice(actions)
playing= True
while playing:
    while player not in actions:
        player=input('Enter your choice :')
    print(f'player : {player}')
    print(f'computer : {computer}')
    if player==computer:
        print('its a tie')
    elif player=='paper' and computer=='scessor':
        print('you won..!')
    elif player== 'rock' and computer=='paper':
        print('Youu won..!')
    else :
        print('You lose...!')
    play_again=input('want to play again ..?Y/N')
    if play_again=='n':
        break
print('Thanks for playing')
