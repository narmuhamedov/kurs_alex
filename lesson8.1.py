from random import randint
from datetime import datetime
cash = 500
while cash > 0:
    start = datetime.now()
    try:
        bet = int(input(f'Доступно-{cash}$ \nКакую сумму хотите поставить? или нажмите 0 для выхода '))
        if bet == 0:
            print(f'Вы нас бросили Адиос! Ваш счет {cash}$ ')
            break
    except:
        print('Не пиши буквы Алкаш пиши цифры!!!')
        continue

    if bet>cash or bet<1:
        print(f'Ставка не должна быть больше {cash} или меньше 0 ')
        continue

    computer = randint(1,6)
    user = randint(1,6)
    print(f'У вас {user}\nУ компа{computer}')

    if computer>user:
        print('Вы проиграли')
        cash-= bet
        with open('bone_game.txt', 'a', encoding='UTF-8')as game:
            game.write(f'У  К:{computer}, U:{user}, Ставка{bet}! Game Over Остаток{cash}')


    elif computer<user:
        print('Вы выйграли')
        cash+= bet
        with open('bone_game.txt', 'a', encoding='UTF-8')as game:
            game.write(f'У  К:{computer}, U:{user}, Ставка{bet}! You win Остаток{cash}')


    else:
        print('ничья')
        with open('bone_game.txt', 'a', encoding='UTF-8')as game:
            game.write(f'У  К:{computer}, U:{user}, Ставка{bet}! Draw Остаток{cash}')

with open('bone_game.txt', 'a', encoding='UTF-8')as game:
    game.write(f'\n TimeGame{datetime.now()-start} ')




