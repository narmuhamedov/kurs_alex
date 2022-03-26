coca_cola = 25
cola_05l = 0
cola_1l = 0
cola_15l = 0
brak = 0
print(f'Колличество бутылок {coca_cola}')
while coca_cola!= 0:
    coca_cola -= 1
    answer = int(input('какой литр \n 1 - 0.5л\n 2 - 1 л\n 3 - 1,5л\n 4-brak  '))

    if answer == 1:
        cola_05l += 1
        print(f'кола 0.5 = {cola_05l}')
        print(f'Колличество бутылок {coca_cola}')
    elif answer == 2:
        cola_1l +=1
        print(f'кола 1.0 = {cola_1l}')
        print(f'Колличество бутылок {coca_cola}')
    elif answer == 3:
        cola_15l +=1
        print(f'кола 1.5 = {cola_15l}')
        print(f'Колличество бутылок {coca_cola}')
    elif answer == 4:
        brak += 1
        print(f'кола brak {brak}')
        print(f'Колличество бутылок {coca_cola}')



print(f'Колличество бутылок колы {coca_cola}')
print(f'Колличество 0.5 {cola_05l}')
print(f'Колличество 1.0 {cola_1l}')
print(f'Колличество 1.5 {cola_15l}')
print(f'Бракованная кола {brak}')

# enter_number = int(input('Загадайте число от 1 до 100: '))
# left = 0
# right = 101
# attemps = 0

# while 1:
#     result  = (right + left) // 2
#     attemps +=1
#     print(f'Попытки {attemps}')
#     print(f'Компьютер сказал число {result}')
#
#     if result == enter_number:
#         print('Ура я нашел число!! ')
#         break
#
#     elif result > enter_number:
#         right = result
#
#     elif result < enter_number:
#         left = result
#
# print(f'Колличество всех попыток {attemps}')
#
#
