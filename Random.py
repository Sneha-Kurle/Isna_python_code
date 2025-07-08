import random
low=0
high=10
num=random.randint(low,high)
while True:
    lis=int(input(f'Guess a number from {low} to {high}:'))
    if lis<0 or lis>10:
        print('Not valid')
        print(f'Please enter a number from {low} to {high} ')
    elif lis<num:
        print('Too less...! try again')
    elif lis>num:
        print('Too high...!try again')
    else:
        print(f'The guess {lis} is correct')
        break