import random
options = ['apple', 'banana', 'orange', 'pineapple', 'watermelon','isna', 'potato', 'onion', 'cherry']
choose = random.choice(options).lower()
hangman_art = {
    0: ('     ',
        '     ',
        '     ',
        '     '),
    1: ('  o  ',
        '     ',
        '     ',
        '     '),
    2: ('  o  ',
        '  |  ',
        '     ',
        '     '),
    3: ('  o  ',
        '  |\\ ',
        '     ',
        '     '),
    4: ('  o  ',
        ' /|\\ ',
        '     ',
        '     '),
    5: ('  o  ',
        ' /|\\ ',
        '   \\ ',
        '     '),
    6: ('  o  ',
        ' /|\\ ',
        ' / \\ ',
        '     ')
}

hint = ['_'] * len(choose)
guessed_letters = []
wrong_guesses = 0
max_tries = len(hangman_art) - 1

print('Welcome to the Hangman game!')
print('Your hint is:', ' '.join(hint))

while wrong_guesses < max_tries and '_' in hint:
    user_guess = input('Enter a letter to guess: ').lower()

    if not user_guess.isalpha():
        print('Please enter an alphabetic letter.')
        continue
    elif len(user_guess) > 1:
        print('You should enter a single character.')
        continue
    elif user_guess in guessed_letters:
        print('This letter has already been guessed.')
        continue

    guessed_letters.append(user_guess)

    if user_guess in choose:
        print(' Your guess is correct!')
        for i in range(len(choose)):
            if choose[i] == user_guess:
                hint[i] = user_guess
    else:
        wrong_guesses += 1
        print(f' Wrong guess! You have {max_tries - wrong_guesses} tries left.')
        for line in hangman_art[wrong_guesses]:
            print(line)

    print('Guessed letters:', ' '.join(guessed_letters))
    print('Word:', ' '.join(hint))

    if '_' not in hint:
        print(' Congrats! You guessed the word:', choose)
        break

if '_' in hint:
    print(' Game over! The word was:', choose)