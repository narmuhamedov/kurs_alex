from random import randint
import datetime
name = str(input('Как вас зовут? '))
attempts = 0
attempts = int(input('Сколько хотите попыток? '))
start = datetime.datetime.now()

while 1:
    num1 = randint(1, 9)
    num2 = randint(1, 9)
    action = num1 * num2
    print(f'Сколько будет {num1}*{num2} = ?' ,end=' ')
    result = int(input())
    print(action)
    attempts-=1

    if attempts == 0:
        print(f'Имя{name}\n'
              f'Время{datetime.datetime.now()-start}\n'
              f'Колличество попыток{attempts}')
        break