from random import randint

comp_num = randint(1, 100)
min_value = 1
max_value = 100
while True:

    try:
        usr_num = int(input(f'Guess the number from {min_value} to {max_value}: '))
    except ValueError:
        print("It's not a number!\n")
        continue

    if usr_num == comp_num:
        print("Congratulations! You guessed the number!")
        break
    elif usr_num < comp_num:
        print('Too small!\n')
        min_value = usr_num
    else:
        print("Too big!!\n")
        max_value = usr_num

