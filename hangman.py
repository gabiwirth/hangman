import random


wordbank = {
    4: ["poop", "stub"],
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
    h1 = ["  O       Wrong guesses:", "/", "|" , '\\','  |', " /", "\\"]
    wrong_blanks = ''
    new_blanks = ' '
    for i in wrong_guesses:
        wrong_blanks += i
        wrong_blanks += ','
    wrong_blanks = wrong_blanks[:-1]
    for j in blanks:
        new_blanks += j
        new_blanks += ' '

    # while i < range(len(wrong_blanks)):
        # h1 = ' '

    print(h1[0],wrong_blanks)
    print(h1[1],h1[2],h1[3])
    print(h1[4])
    print(h1[5], h1[6])
    print(new_blanks)
