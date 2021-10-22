print('Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach!')

min_num = 0
max_num = 1000
test = 0 #  made for check if choise is corect

for i in range(11):
    guess = int((max_num - min_num) / 2) + min_num
    while True:
        if i == 10:
            if min_num == 999: # fix for users who picked 1000 because int(0.5)==0
                guess = 1000
            print(f'Twoja liczba to {guess}!!!')
            break
        try:
            print(f'\n Próba {i + 1},\n\n Zgaduję: {guess}')
            answer = input('\nWpisz cyfrę odpowiedzi:\n  1  Za dużo\n  2  Za mało\n  3  Zgadłeś\n\n  ')
            test = int(answer)
            if answer == '1':
                max_num = guess
                break
            elif answer == '2':
                min_num = guess
                break
            elif answer == '3':
                print('Wygrałem!\n')
                break
            else:
                print('Nie oszukuj!')
                continue

        except ValueError:
            print('\nTo nie jest poprawny wybór! spróbuj jeszcze raz\n')
            continue
