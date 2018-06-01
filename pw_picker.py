import random
import string

verbs = ['run', 'hide', 'jump', 'kick', 'scream', 'talk', 'yell', 'share', 'look', 'laugh', 'lick', 'love', 'drink', 'drop', 'drip', 'diss', 'miss', 'catch', 'throw', 'yell', 'shoot']
nouns = ['dog', 'cat', 'soccerball', 'football', 'mouse', 'desk', 'chair', 'screen', 'book', 'water', 'bottle', 'laptop', 'wallet', 'key', 'pen', 'pencil', 'pad', 'room', 'couch']
number = random.randrange(0,1000)
verb = random.choice(verbs)
noun = random.choice(nouns)
punctuation = random.choice(string.punctuation)

print('Welcome to the password picker!')
answer = input("Would you like me to pick a password for you?:  ")
   
while answer[0].lower() != 'y' and answer[0].lower() != 'n':
    answer = input("I'm sorry please respond with yes or no. \nWould you like me to pick a password for you?:  ")

while answer[0].lower() == 'y' or answer[0].lower() == 'n':
    if answer[0].lower() == 'y':
        number = random.randrange(0,1000)
        verb = random.choice(verbs)
        noun = random.choice(nouns)
        punctuation = random.choice(string.punctuation)
        print(verb + noun + str(number) + punctuation)
        answer = input("Would you like another password?:  ")
    if answer[0].lower() == 'n':
        print('Thanks for playing!')
        break
    else:
        while answer[0].lower() != 'y' and answer[0].lower() != 'n':
            answer = input("I'm sorry please respond with yes or no. \nWould you like me to pick a password for you?:  ")

    

   



