while 1:
    try:
        first_num = float(input('Write first number: '))
        answer = input('write your operation: + - * / ')
        second_num = float(input('Write second number: '))
    except:
        print('Please write only numbers ')
        continue

    if answer == '+':
        print(f'Result - {first_num + second_num}')


    elif answer == '-':
        print(f'Result - {first_num - second_num}')

    elif answer == '*':
        print(f'Result - {first_num * second_num}')

    elif answer == '/':
        print(f'Result - {first_num / second_num}')

    else:
        print('указана не верная операция повторите!!!')
        continue

    exit = str(input('Хотите продолжить?y/n '))
    if exit == 'y':
        continue
    elif exit == 'n':
        break
    else:
        print('Команда введена не правильно')


# try:
#     a = 12
#     b = 12
#     print(a+b)
# except:
#     print('Операция не верна ')




