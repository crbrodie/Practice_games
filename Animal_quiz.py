attempt = 0
points = 0

def check_answer(user_answer):
    global points
    global attempt
    global wtf
    global player

    if user_answer.lower() == real_answer.lower():
        print(f'Good job! \nYou scored', 3 - int(attempt), 'points!')
        points = points + 3 - attempt
        attempt = 0
        wtf=user_answer.lower()

    else:
        attempt = attempt + 1
        wtf=user_answer.lower()

        if attempt == 3:
            print('\nSorry, you are out of tries! \nThe correct answer was', real_answer, '\nYou ended with', points, 'points!')
            player = 'idiot'
            attempt = 0

        if attempt < 3 and player != 'idiot':
            print('Sorry, thats not right.  You have', 3-int(attempt), 'more live(s).')
        


#Question 1
print('Guess the Animal!')

wtf = ''
player = ''
real_answer = 'Polar Bear'
while wtf != real_answer.lower() and attempt < 3 and player!='idiot':
    
    check_answer(user_answer = input('\nWhich bear lives at the north pole?:  '))


#Question 2
print('\n\nQuestion 2: \n \n')
wtf = ''
player = ''
real_answer = 'Cheetah'
while wtf != real_answer.lower() and attempt < 3 and player!='idiot':
    
    check_answer(user_answer = input('Which is the fastest land animal?:  '))

#Question 3

print('\nQuestion 3: \n \n')
wtf = ''
player = ''
real_answer = 'Blue Whale'
while wtf != real_answer.lower() and attempt < 3 and player!='idiot':
    
    check_answer(user_answer = input('Which is the largest animal?:  '))

print('Your final score is', str(points) + '!')