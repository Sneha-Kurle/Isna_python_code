import time
time_st =int(input('enter a time stramp  :'))
for i in reversed(range(0, time_st)):
    print(f'00:00:{i}')
    time.sleep(1)

print('Times upp...!')
