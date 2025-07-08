def amount():
    print(f'The balence amount is :${balence}')

def deposit():
    dep=float(input('Enter an amount to deposit :'))
    if dep<0:
        print('amount cant be less than zero')
    else:
        return dep

def withdraw():
    wd=float(input('Enter an amount to withdraw : '))
    if wd<0:
        print('wd amount cant be less than zero')
    elif wd>balence:
        print(('Insuffucient balence'))
    else:
        return wd

balence=100
running= True
while running:
    print('The banking program')
    print('1. to check the balence')
    print('2. to enter the deposit amount')
    print('3.To check the wd amount')
    print('4. Exit')
    options=float(input('select a number from 1 to 4 :'))
    if options==2:
        balence+=deposit()
    elif options==1 :
        amount()
    elif options==3:
        balence-=withdraw()
    elif options == 4:
        running = False
    else:
        print('Invalid entry')
print('Thanks for banking.. Have a nice day..!')
