class Phone:
    def __init__(self, name, cost, color, memory, camera, cpu):
        self.name = name
        self.cost = cost
        self.color = color
        self.memory = memory
        self.camera = camera
        self.cpu = cpu

    def call_to_someone(self, number):
        return f'This phone calling this number{number}'

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Cost: {self.cost}$\n' \
               f'Color: {self.color}\n' \
               f'Memory: {self.memory}\n' \
               f'Camera: {self.camera}\n' \
               f'CPU:{self.cpu}'


class Iphone(Phone):
    def __init__(self, name, cost, color, memory, camera, cpu):
        super().__init__(name, cost, color, memory, camera, cpu)

    def info(self):
        if self.name == 'Iphone13':
            return f'Best of camera at moment'
        elif self.name == 'Iphone5':
            return  f'This is Legend'
        elif self.name == 'Iphone2':
            return f'This is old phone'


    def __str__(self):
        return super(Iphone, self).__str__()


iphone13 = Iphone(name='Iphone13', cost=1200, color='black', memory=1024,camera=16,cpu=2.4)
iphone5 = Iphone('Iphone5', 200, 'black', 64, 10, 2.0)
print(iphone13.info())
print(iphone13)
print(iphone5)
print('-'*40)

class Nokia(Phone):
    def __init__(self, name, cost, color, memory, camera, cpu):
        super().__init__(name, cost, color, memory, camera, cpu)

    def unstopable(self, object):
        return f'crashed-{object}'

    def __str__(self):
        return super(Nokia, self).__str__()


nokia3310 = Nokia(name='3310', cost=20, color='blue', memory=8, camera=0, cpu=1.0)
print(nokia3310.unstopable('floor'))
print(nokia3310)
print('-'*30)


