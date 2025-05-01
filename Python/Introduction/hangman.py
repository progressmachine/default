import random
from collections import Counter

some_words = '''pen space desk water bottle laptop blue hexagon zebra mouse death life bag pink'''
some_words = some_words.split(' ')

word = random.choice(some_words)

if __name__ == '__main__':
    print("Guess the word!")
    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letters_guessed = ''
    chances = len(word) * 2
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Only enter a letter.')
                continue

            if not guess.isalpha():
                print('Only enter a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letters_guessed:
                print('You have already guessed that letter')
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letters_guessed += guess

            for char in word:
                if char in letters_guessed and (Counter(letters_guessed)) != Counter(word):
                    print(char, end=' ')
                    correct += 1
                elif (Counter(letters_guessed)) == Counter(word):
                    print("The word is:", word)
                    flag = 1
                    print("Congratulations! You won!")
                    break
                else:
                    print("_", end=" ")

        if chances == 0 and (Counter(letters_guessed)) != Counter(word):
            print("You lost.")
            print(f"The word was {word}.")
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()