name = input("What is your name?")
age = input('How old are you?')
height_ft = input('How tall are you(ft)?')
height_in = input('How tall are you(in)?')
height = int(height_in) + (int(height_ft) *12)
print(height)
if int(age) >= 8 and int(height) >= 55:
    print("Come on and ride,", name + "!")
elif int(age) < 8:
    age_needed = 8- int(age)
    print(f"Sorry,", name, "come back when you're", age_needed, "years older")
if int(height) < 55:
    print('Sorry,', name, 'you are not tall enough to ride.')