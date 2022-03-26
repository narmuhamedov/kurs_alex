borsh = {'мясо', 'капуста', 'свекла', 'картошка', 'специи', 'лук', 'сметана'}
lagman = {'мясо', 'лапша','специи', 'лук', 'редька', 'джусай'}

#находит похожее значение
print(lagman.intersection(borsh))
print(lagman & borsh)

#находит микс значений
print(lagman.union(borsh))
print(lagman | borsh)

#не совпаддение между значениями
print(lagman.difference(borsh))
print(lagman-borsh)

#вывод не одинаковых значений
print(lagman.symmetric_difference(borsh))
print(lagman^borsh)

list1 = [1,2,3,4,5,6,7,8,9,1,1,1,1,22,3,3,4,4]
list_set = set(list1)
print(list_set)






# nominal = [1, 3, 5, 10, 20, 50, 100, 200, 500, '1k', '2k', '5k']
# person = ['nothing', 'nothing', 'nothing', 'nothing', 'Togolok M.', 'K.Datka',
#           'Satylganov', 'Osmonov', 'Karalaev', 'Balasagun', 'Chokmorov', 'Burana']
#
# banknotes = dict(zip(nominal, person))
# del banknotes[1]
# del banknotes[3]
# del banknotes[5]
# del banknotes[10]
# for i,j in banknotes.items():
#     print(f'{i} - {j}')
#
#