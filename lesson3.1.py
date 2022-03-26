ru = 'white', 'blue', 'red'
gr = 'black', 'red', 'yellow'
it = 'white', 'green', 'red'

our_colors = []
while len(our_colors)!= 3:
    cls = str(input('Напиште  цвет '))
    our_colors.append(cls)
    print(cls)
    print(our_colors)

if tuple(our_colors) == ru:
    print('Russia')
elif tuple(our_colors) == gr:
    print('Germany')
elif tuple(our_colors) == it:
    print('Italy')
else:
    print('This Flag unknown')




# name = str(input('Назовите ваше имя? '))
# age = int(input('Введите ваш возраст '))
# email = str(input('Напишите ваш Email '))
# gender = str(input('Укажите ваш пол '))
# number_phone = str(input('Наш номер '))
# hobby = str(input('Ваше хобби? '))
# height = float(input('Ваш рост '))
# bad = bool(input('Вредные привычки? '))
#
# lst_myself = []
#
# lst_myself.append(name.title())
# lst_myself.append(age)
# lst_myself.append(email)
# lst_myself.append(gender)
# lst_myself.append(number_phone)
# lst_myself.append(hobby)
# lst_myself.append(height)
# lst_myself.append(bad)
#
# myself_tuple = tuple(lst_myself)
#
# print(f'Наши данные {myself_tuple}')














# names = (1, 3, 44.55, 'Hello', 'World', True, False, 1, 22, 1, 1, 1, 1)
# print(names)
# #по колличеству значений
# print(names.count(1))
# print(names.index('World'))
#
# # Изменение кортежа через список
# names_list = list(names)
# print(names_list)
# names_list.append('Good Morning!')
# print(names_list)
# names_tuple = tuple(names_list)
# print(names_tuple)


