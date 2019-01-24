"""
Hangman.

Authors: Haiden Smith and Alex Tabuyo.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

# Do NOT attempt this assignment before class! #######
import random


def main():
    a = random_word()
    c = list(len(a) * '-')
    n = 5
    while True:
        n = word_guess(a, c, n)
        if list(a) == c:
            print("You won!")
            break
        if n == 0:
            print('You lose! The word was', '"', a, '"')
            break


def random_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    r = random.randrange(0, len(words) - 1)
    word = words[r]
    return word


def guess():
    return str(input('What letter do you want to try?'))


def word_guess(a, c, n):
    b = guess()
    if b in a:
        for k in range(len(a)):
            if b == a[k]:
                c[k] = b
    else:
        n = n - 1
        print('You have guessed incorrectly!', n, 'remaining guesses.')

    for k in range(len(c)):
        print(c[k], end='')
    print()
    return n


main()