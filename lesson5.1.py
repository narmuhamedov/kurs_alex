univer = []
technikum = []
army = []
married = []

abuturient = [
    {'name': 'Radomir', 'OPT':110, 'gender':'male'},
    {'name': 'Alexader', 'OPT':110, 'gender':'male'},
    {'name': 'Denis', 'OPT':90, 'gender':'male'},
    {'name': 'Islam', 'OPT':80, 'gender':'male'},
    {'name': 'Victorya', 'OPT':200, 'gender':'female'},
    {'name': 'Masha', 'OPT':50, 'gender':'female'},
    {'name': 'Angelina', 'OPT':0, 'gender':'female'},
    {'name': 'Alexey', 'OPT': 0, 'gender':'male'},
    {'name': 'Vlad', 'OPT':0, 'gender':'male'},
    {'name': 'Olga', 'OPT':0, 'gender':'female'}
]

def all_abit(lst):
    for i in lst:
        for k, v in i.items():
            print(f'{k}-{v}')


all_abit(abuturient)


def selection(lst,univer:list, technikum:list, army:list, married:list):
    for i in lst:
        if i['OPT'] >= 110:
            univer.append(i)

        elif i['OPT']<=100 and i['OPT']>=45:
            technikum.append(i)

        elif i['OPT'] <= 45 and i['gender'] =='male':
            army.append(i)

        elif i['OPT'] == 0 and i['gender'] =='female':
            married.append(i)

selection(abuturient, univer, technikum, army, married)

print('-'*50)
print(f'V Univer{univer}\n'
      f'V Technikum{technikum}\n'
      f'V Armi{army}\n'
      f'Zamyj{married}')