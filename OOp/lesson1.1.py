class Car:
    def __init__(self, brand, speed, color, cost, transmission):
        self.brand = brand
        self.speed = speed
        self.color = color
        self.cost = cost
        self.trans = transmission

    def tunning(self, cost_tunnig):
        summary = cost_tunnig+self.cost
        return f'Итоговая цена за тюнниг машины{summary}'

    def __str__(self):
        return f'Бренд:{self.brand}\n' \
               f'Скорость:{self.speed} км/ч\n' \
               f'Цвет:{self.color}\n' \
               f'Цена:{self.cost}$\n' \
               f'Коробка передач:{self.trans}'

car1 = Car(brand='Lexus 570', speed=300, color='Черный', cost=15000, transmission='automatic')
print(car1.tunning(10000))
print('-'*30)
print(car1)
print('-'*30)

class Electric_Car(Car):
    def __init__(self, brand, speed, color, cost, transmission, fuel, date):
        super().__init__(brand, speed, color, cost, transmission)
        self.fuel = fuel
        self.date = date

    def __str__(self):
        return super(Electric_Car, self).__str__()+f'\nТопливо:{self.fuel}\n' \
                                                   f'Дата:{self.date}'


electrik1 = Electric_Car(brand='Testa_car', speed=400, color='gray', cost=1000000, transmission='robot', fuel=False,
                         date='20-03-2020')

electrik2 = Electric_Car('Tesla_car2', 500, 'red', 30000, 'robot', False, '20-20-2020')

print(electrik1.tunning(6000))
print(electrik1)
print('-'*30)
print(electrik2)