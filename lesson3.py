# #Сортировка
# numbers = [3, 5, 1, 4, 5, 66, 78, 999, 655, 4332, 66788, 6454, 66]
# numbers.sort()
# print(numbers)
# print(len(numbers))

# Списки  LIST
# data_types = ['Name', 1, 2, 5.5, 34.55, 'Hello', "World", True, False]
# data_types3 = []

# #For Цикл в списках
# for i in data_types:
#     if i == 'Name' or i == 'Hello':
#         data_types3.append(i)
#     else:
#         print(i)
# print(data_types)
# print(data_types3)

# data_types2 = []
# print(f'Our list - {data_types}\n')
#
# # Метод перемещения из одного списка в другой
# data_types2.append(data_types.pop(0))
# data_types2.append(data_types.pop(5))
# data_types2.append(data_types.pop(6))
# print('1dt',data_types)
# print('2dt',data_types2)
#
# #Метод обновления
# data_types[2] = 3.0
# data_types[3] = 4.0
# data_types[4] = 5.0
# print('update list ', data_types)
#
# #Метод расширения
# data_types.extend(data_types2)
# print(data_types)
#
# #Метод вывода значений через индекс
# print(data_types[-3])


# #методы добавления append insert
# data_types.append('Good Morning')
# data_types.append(12345)
# data_types.insert(6, 'Alexander')
# print(f'Append_datatypes{data_types}\n')


# #методы удаления clear
# # data_types.clear()
# # print(f'data_types_clear-{data_types}')
# data_types.remove(1)
# print(f'data_types_remove-{data_types}')
# del data_types[0]
# print('index_delete', data_types)


