import random
def spin():
    opt=['🍎', '🍍', '🍉', '🍊', '⭐']
    sym=[]
    for i in range(3):
        sym.append(random.choice(opt))
        run=(' | '.join(sym))
    print('Spinning......')
    print("**************")
    print(run)
    print("**************")
    return sym
def pay(run,bet):
    if run[0]==run[1]==run[2]:
        if run[0] == '🍎':
            return bet * 2
        elif run[1] == '🍍':
            return bet * 3
        elif run[2] == '🍉':
            return bet * 4
        elif run[3] == '🍊':
            return bet * 10
        elif run[4] == '⭐':
            return bet * 20
    return 0


def main():
    balence = 100
    print('************************************')
    print('Welcome to the Slot Matching Game...!')
    print('Symbols: 🍎 🍍 🍉 🍊 ⭐')
    print('************************************')

    while balence>0:
        print(f'The totle balance is :{balence}')
        bet=input('Enter an amount :')
        if not bet.isdigit():
            print('Invalid amount entered')

        elif int(bet) > balence:
            print('Insufficient amount')
        else:
            balence-=int(bet)
        run= spin()
        payout=pay(run, bet)
        if payout>0:
            print(f'You won the game: {payout} coins! ')
        else:
            print('You lost..')
        balence+=payout
    print('Game over')

if __name__=='__main__':
    main()