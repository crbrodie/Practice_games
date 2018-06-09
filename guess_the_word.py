from random import choice as r

words = ['actor', 'adopt', 'ahead', 'adult', 'agent', 'agree', 'admit', 'album', 'beach', 'begun', 'bench', 'blind', 'birth', 'bread', 'bound', 'build', 'brake', 'cream', 'cover', 'cycle', 'daily', 'crown', 'death', 'drama', 'dream', 'drink', 'dying', 'earth', 'enemy', 'enter', 'fight', 'first', 'frame', 'fraud', 'fruit']
word = r(words)
lives_left = 10
heart = ' \u2764 '
lives = heart * lives_left
users_word = ['?','?','?','?','?']
length_left = 0
unknown_letters = 5
x=-1
lose_life = 'no'

def count_unknown():
    global unknown_letters
    global lose_life
    global lives
    q_marks = 5
    if unknown_letters != 0:
        for x in users_word:
            if x == '?':
                q_marks = q_marks
            else:
                q_marks = q_marks - 1
    else:
        q_marks = 0
    if unknown_letters == q_marks and q_marks != 0:
        lose_life = 'yes'
    else:
        unknown_letters = q_marks

def guess_func():
    global unknown_letters
    global x
    global users_word
    print('Lives: ', lives, '\n\nYour word is ', users_word)
    user_guess = input('\nGuess a letter or the word if you know it: ')
    if len(user_guess) == 1: 
        x = -1
        while unknown_letters > 0 and x<4:
            x =  x + 1
            if user_guess.lower() == word[x]:
                users_word[x] = user_guess.lower()
                
                if users_word[0] + users_word[1] +users_word[2] + users_word[3] + users_word[4]== word:
                    unknown_letters = 0
    elif len(user_guess) == 5:
        if user_guess.lower() == word:
            unknown_letters = 0
        else:
            print("I'm sorry, thats incorrect")
            count_unknown()
            guess_func()
    else:
        print('Sorry, you can only guess one letter at a time or the whole word! Please enter your guess: ')
        guess_func()
        


while unknown_letters > 0:
    lose_life = 'no'
    guess_func()
    count_unknown()
    
    if lose_life == 'yes':
        
        lives_left = lives_left - 1
        lives = heart * lives_left
    if lives_left <= 0:
        print('Sorry, you are out of lives... your word was', word.upper())
        
if unknown_letters == 0:
    print('Good job, you guessed all the letters in your word!, and with', lives_left, 'lives to go!')
    print('Your word was', word.upper())



    


    
    
    