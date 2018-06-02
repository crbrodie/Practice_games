attempt = 0
points = 0
user_answer = ''
def check_answer(x):
    global points
    global attempt
    global user_answer
    

    if x.lower() == real_answer.lower():
        print(f'Good job! \nYou scored', 3 - int(attempt), 'points!')
        points = points + 3 - attempt
        attempt = 0
       

    else:
        attempt = attempt + 1


        if attempt >= 3:
            print('\nSorry, you are out of tries! \nThe correct answer was', real_answer, '\nYou have', points, 'points!')
            user_answer = real_answer.lower()
            attempt = 0

        else:
            print('Sorry, thats not right.  You have', 3-int(attempt), 'more live(s).')
        


#Question 1
print('Guess the Animal!')

real_answer = 'Polar Bear'
while user_answer != real_answer.lower() and attempt < 3:
    user_answer = input('\nWhich bear lives at the north pole?:  ')
    check_answer(user_answer)


#Question 2
print('\n\nQuestion 2: \n \n')

real_answer = 'Cheetah'
while user_answer != real_answer.lower() and attempt < 3:
    user_answer = input('Which is the fastest land animal?:  ')
    check_answer(user_answer)

#Question 3

print('\nQuestion 3: \n \n')

real_answer = 'Blue Whale'
while user_answer != real_answer.lower() and attempt < 3:
    user_answer = input('Which is the largest animal?:  ')
    check_answer(user_answer)

print('Your final score is', str(points) + '!')
