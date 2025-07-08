foods=[]
prices=[]
total=0
while True:
    food=input('enter a food or quite q  :')
    if food== 'q':
        break
    else:
        price = int(input('enter a price  :'))
        foods.append(food)
        prices.append(price)

print('__________YOUR CART IS READY_________')
for i in foods:
    print(i, end= ' ')
print()

for i in prices:
    total+=price
print(f'the price of the foods are {total}')