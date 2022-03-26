auto = dict(brand= 'BMW', model= 'e34', color= 'black', volume= 3.0)
print(auto)
#добавления2
auto.update(year = 1995)
print(auto)
#Отображение через цикл
# for keys, value in auto.items():
#     print(f'{keys}-{value}')

#Копирование словаря
# auto2 = auto.copy()
# print(f'Copy dict - {auto2}')
# auto2.update(crash = True)
# print(auto2)

# #Получение значений через ГЕТ функцию
# print(auto.get('brand'))


# #вывод только ключей и значений по отдельности
# print(auto.keys())
# print(auto.values())

# student = {
#     'name': 'John',
#     'age': 24,
#     1997: 'Cow Year',
#     'height': 1.80,
#     'education': True,
#     'hobby': ['Guitar', 'Programming', 'Sleep']
# }

#Удаление из словаря
# del student[1997]
# print(student)

#Вывод словаря значение через индекс
# print(student['hobby'][1])

#измение значений в словаре
# student['age'] = 25
# print(student)


# #Расширение(добавление) словаря
# student['zp'] = 20000
# student[123] = False
# print(student)
# #Вывод значения через ключ
# print(student['age'])
