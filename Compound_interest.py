rate=0
time=0
principle=0
while principle<=0:
    principle= int(input("enter a principle amount  :"))
    if principle<0:
        print('value cant be less than 0')

while rate<=0:
    rate= int(input("enter a rate value  :"))
    if rate<0:
        print('value cant be less than 0')


while time<=0:
    time= int(input("enter a time period  :"))
    if time<0:
        print('value cant be less than 0')

totle= principle*pow((1+rate/100),time)
print(f'The compound interst is ${totle:.2f} ')