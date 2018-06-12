from random import choice as r
play_main = True
while play_main == True:
    with open("wordlist.txt") as f:
        word_list = f.read().splitlines()
    word = list(r(word_list))
    lives_left = 10
    heart = ' \u2764 '
    users_word_together = ''.join(word).upper()
    users_word = list('?'*len(users_word_together))
    unknown_letters_past = int(len(users_word_together))
    unknown_letters_present = 1
    incorrect_guesses=[]
    


    def count_unknown():
        global unknown_letters_present
        question_marks = 0
        for x in users_word:
            if x == '?':
                question_marks += 1 
        unknown_letters_present = question_marks

    def compare(guess):
        global last_guess
        global users_word
        global word_guess
        if len(guess) == 1:
            last_guess = guess
            index = 0
            while index < int(len(users_word_together)):
                if word[index] == guess.lower():
                    users_word[index] = word[index].upper()
                index += 1
        elif len(guess) == int(len(users_word_together)):
            word_guess = guess
            last_guess = word_guess
            if word_guess.upper() == ''.join(word).upper():
                users_word = word
            else:
                None


        
    while unknown_letters_present != 0 and lives_left >= 1:
        lives = heart * lives_left
        print(f'I am thinking of a {len(users_word_together)} letter word, can you guess what it is?\nGuess a letter or the word if you think you know it... \nLives: {lives}')
        print(''.join(users_word)) 
        if len(incorrect_guesses) > 0:
            print('Incorrect Guesses: '+', '.join(incorrect_guesses))

        compare(input('Guess a letter: '))
        print("\n" * 100)
        count_unknown()
        if unknown_letters_past == unknown_letters_present and last_guess.upper() not in incorrect_guesses and last_guess.upper() not in users_word_together:
            lives_left -= 1
            lives = heart * lives_left
            print(f'Sorry {last_guess.upper()}, is incorrect.')
            incorrect_guesses.append(last_guess.upper())
        else:
            unknown_letters_past = unknown_letters_present

    while unknown_letters_present == 0 or lives_left == 0:
        if unknown_letters_present == 0:
            play_again = input(f"Congradulations! You correctly guessed the word.  \nYour word was {''.join(word).upper()}\nYou guessed it with {lives_left} lives remaining!\nPlay Again(y/n)?: ")
            if play_again.lower()[0] == 'y':
                unknown_letters_present = 1
            elif play_again.lower()[0] == 'n':
                play_main = False
                break
            else:
                continue
        if lives_left == 0:
            play_again = input(f"Aww! You ran out of lives! \nYour word was {''.join(word).upper()}\nPlay Again(y/n)?: ")
            if play_again.lower()[0] == 'y':
                print("\n" * 100)
                lives_left = 1
            elif play_again.lower()[0] == 'n':
                play_main = False
                break
            else:
                continue

    continue
    

