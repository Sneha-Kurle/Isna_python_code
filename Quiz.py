questions=('1. How many elements are there in periodic table?:',
           '2. which animal lays the largest eggs?: ',
           '3. What is the most abundant gas in the earths atmospeare',
           '4. What is the hottest planet in the solar system')

options=(("A. 116",'B. 117','C. 118','D. 119'),
         ("A. Whale",'B. Crow','C. Parrot','D. Ostritch'),
         ("A. Na",'B. O','C. C02','D. He'),
         ("A. Earth",'B.Venus','C.Jupyter','D. Mars'))
result=('A','D','A','B')
guess=[]
i=0
score=0
print('--------------------------------------------------')
for que in questions:
    print(que)
    for op in options[i]:
        print(op)
    print('------------------------------------------------')
    gues= input('enter your answer:')
    guess.append(gues)
    if gues==result[i]:
        score+=1
        print('Your answer is correct')
    else:
        print('Incorrect')
        print(f'The correct answer is {result[i]}')
    print()
    i+=1

print('-------------------------------------')
print('                RESULT               ')
print('-------------------------------------')
print(f'The actual correct answers are {result}')
print(f'The guessed answers are {guess}')
score=score/i*100
print(f'Your score is {score} %')