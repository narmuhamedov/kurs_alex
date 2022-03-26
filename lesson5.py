# def menu(**kwargs):
#     return kwargs
#
# monday = menu(breakfast = 'яичница', lunch = 'Борщ', dinner = 'Кабачковая икра с хлебом')
# print(monday)
# print(type(monday))


#args преобразовывает в кортеж ключевая часть это символ звездочка *
# def result(*args):
#     return args
#
# a = result(3,4,5,6,7,7,765,4,4,4,5,6,67,7,7,77,7, 'hello', True, False)
# print(a)
# print(type(a))


# def about_myself(name, hobby, gender, age='25'):
#     return name + hobby + gender + age
#
# a = about_myself(input('Write your name'), input('write your hobby'),
#                  input('your gender'))
#
# print(a)


# #return
# def plus(a,b,c):
#     return a + b + c
#
# print(plus(2,3,4) + plus(3,4,5))

#Argument по умолчанию пример
# def plus (a,b,c=3):
#     d = a+b+c
#     print(d)
#
# plus(2,3,4)


# # Аргумент по умолчанию
# def greeting(name='Alexander'):
#     print(f'Hello {name}')
#
# greeting('Radomir')
# greeting()


# def greeting(name):
#     print(f'Hello {name}')
#
#
# greeting('Radomir')
# greeting('Alexander')
# greeting('Islam')
# greeting('Denis')


# def square(a, b):
#     c = a+b
#     print(f'Result-{c}')
#
# square(12, 12)
# square(1, 2)