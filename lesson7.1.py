import datetime
start = datetime.datetime.now()
while 1:
    name = input('What is your name? ')
    print(f'Hello {name}')
    print(f'Time out {datetime.datetime.now()-start}')











# import random
# from random import randint,choice,sample,randrange
#
# #радомные значения со списком choise
# lst = ['alex', 'radomir', 'denis', 'islam', 'ivan','anna', 'jack']
# print(choice(lst))
# #randint случаяные числа
# numbers = randint(1,100)
# print(numbers)
# #sample любые 4 значения из нашего списка
# print(sample(lst,4))
# print(randrange(1,20,4))








# from lesson7 import sum as summa
# print(summa(2,3,4))
