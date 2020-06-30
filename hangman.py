import random

# TODO: change to load wordbank w/ this datastructure from a file.
wordbank = {
    4: ["poop", "stub", "knob"],
    5: ["jacob", "dumpy"],
    6: ["butter", "animal"]
}

def word_picker(length):
    if length > 6 or length < 4:
        return -1
    return random.choice(wordbank[length])

def blank_filler(guess,blanks,goal_word):
    for i in range(len(blanks)):
        if guess == goal_word[i]:
            blanks[i] = guess
    return blanks

def display(guess, wrong_guesses, blanks):
    h1 = ["     O       Wrong guesses:", "   /", "|" , '\\','     |', "    /", "\\"]
    wrong_blanks = ''
    new_blanks = ' '
    for i in wrong_guesses:
        wrong_blanks += i
        wrong_blanks += ','
    wrong_blanks = wrong_blanks[:-1]
    for j in blanks:
        new_blanks += j
        new_blanks += ' '
    for i in range(len(h1)):
        if i >= len(wrong_guesses):
           h1[i] = ' '
    # while i < range(len(wrong_blanks)):
        # h1 = ' '

    print(h1[0],wrong_blanks)
    print(h1[1],h1[2],h1[3])
    print(h1[4])
    print(h1[5], h1[6])
    print(new_blanks)

def main():
    word_length = input('Enter the length of the word you want (4-6): ')
    word_length = int(word_length)
    goal_word = word_picker(word_length)
    blanks = ['_'] * word_length
    turns_left = 7
    wrong_guesses = []
    while turns_left >= 0:
        guess = input('Enter your guess: ')
        old_blanks = blanks.copy()
        blank_filler(guess,blanks,goal_word)
        if old_blanks == blanks:
            wrong_guesses.append(guess)
            turns_left -= 1
        display(guess, wrong_guesses, blanks)
        guesses_string = ''.join(blanks)
        if guesses_string == goal_word:
            print('You won the game!')
            break
        if turns_left == 0:
            print('You ran out of guesses! Game over.')
            play_again = input("Would you like to play again? (yes/no) ")
            play_again = play_again.lower()
            if play_again == 'yes':
                main()
            else:
                print('Thanks for playing!')
                break
