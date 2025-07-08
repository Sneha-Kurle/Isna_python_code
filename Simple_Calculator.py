a=float(input('Enter frst value  :'))
b=float(input('Enter second value  :'))
operator= input('whats the oeprator?? +,-,*,/ ')
if operator== '+':
    result=a+b
    print(round(result,3))
elif operator=='-':
    result=a-b
    print(result)
elif operator=='*':
    result = a * b
    print(result)
elif operator=='/':
    result = a/b
    print(result)
elif operator== '%':
    result = a % b
    print(result)
else:
    print(f'operator {operator} is not valid')
