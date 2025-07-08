import random
import string
char=''+ string.punctuation+string.digits+string.ascii_letters
char=list(char)
keys=char.copy()
print(f'char is :{char}')
random.shuffle(keys)
print(f'keys are :{keys}')
user_text=input('Enter a text ........... :')
cipher_text=' '
for letter in user_text:
    index=char.index(letter)
    cipher_text+=keys[index]
print(f'cipher text for given text is: {cipher_text}')