class French:
    def __init__(self, lang):
        self.lang = lang

    def greeting(self):
        return f'Bonjour'

class English:
    def __init__(self, lang):
        self.lang = lang

    def greeting(self):
        return f'Hello'

class Japan:
    def __init__(self, lang):
        self.lang = lang

    def greeting(self):
        return f'Koonichiwa'

french = French(lang='French')
eng = English(lang='English')
jap = Japan(lang='Japan')
print(french.greeting(), eng.greeting(), jap.greeting())



# class Animal:
#     def __init__(self, name, size, weight, color):
#         self.name = name
#         self.size = size
#         self.weight = weight
#         self.color = color
#     def __str__(self):
#         return \
#             f'Название: {self.name}\n'\
#             f'Размер: {self.size}\n'\
#             f'Вес: {self.weight}\n'\
#             f'Цвет: {self.color}\n'
# bear = Animal(name='Медведь', size='Большой', weight=120, color='Коричневый')
# wolf = Animal(name='Волк', size='Средний', weight=90, color='Серый')
# cat = Animal(name='Кошка', size='Маленький', weight=20, color='Рыжий')
#
# class Birds(Animal):
#     def __init__(self, name, size, weight, color,wingspan,predator,sing, show):
#         super().__init__(name,size,weight,color)
#         self.wingspan = wingspan
#         self.predator = predator
#         self.sing = sing
#         self.show = show
#
#     def __str__(self):
#         return \
#             f'Размах крыльев: {self.wingspan}\n'\
#             f'Хищник(да/нет): {self.predator}\n'\
#             f'Пение(да/нет): {self.sing}\n'\
#             f'Выступление: {self.show}\n'
# parrot = Birds('Попугай', 'Маленький', 5,'Голубо-Зеленый','30-35cm','нет','да','бегать по канату и петь')
# eagle = Birds('Орёл', 'Большой', 50,'Бело-Серый','2 метра','да','нет', 'выполнять трюки в воздухе')
# penguin= Birds('Пингвин', 'Средний', 33,'Черно-Белый','-' ,'нет','нет','прыгать и хлопать')
# print(parrot)

# class Zoo_show:
#     def __init__(self,zoo):
#         self.zoo = zoo
#         self.ticket = 0
#         if zoo.name == 'Попугай':
#             self.ticket = '12$'
#
#         if zoo.name == 'Орёл':
#             self.ticket = '25$'
#
#         if zoo.name =='Пингвин':
#             self.ticket = '50$'
#
#     def result(self):
#         return f'Шоу будет стоить: {self.ticket}'
#
#
#     def __str__(self):
#         return \
#             f'{self.zoo.name} будет {self.zoo.show}'
# parrot_show = Zoo_show(parrot)
# eagle_show = Zoo_show(eagle)
# penguin_show = Zoo_show(penguin)
#
# print(parrot_show)
# print(parrot_show.result())
# print('-'*50)
# print(penguin_show)
# print(penguin_show.result())
# print('-'*50)
# print(eagle_show)
# print(eagle_show.result())
#


