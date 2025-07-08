Menu= { 'Pizza':'30.70',
        'Burger':'67.875',
        'Fries':'76.644',
        'Soda':'84.826',
        'Chips':'98.735',
        'Popcorn':'57.08'
}
print('-----Your Menu------')
for key, values in Menu.items():
    print(f'{key:10}:{values}$')
cart=[]
totle=0
while True:
    item= input('Enter an item or q to quite  :')
    if item=='q':
        break
    elif item is not None:
        cart.append(item)
print(cart)