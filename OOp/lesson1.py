class Person:
    def __init__(self, name, age, gender, height, hobby):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('name should be str')


        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('age should be int')


        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('gender should be str')


        if isinstance(height, float):
            self.height = height
        else:
            raise ValueError('height should be float')


        if isinstance(hobby, bool):
            self.hobby = hobby
        else:
            raise ValueError('hobby should be bool')


    def whtyourname(self):
        return f'My name is {self.name}'

    def age_yo(self):
        return f'I am {self.age} YO'

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Gender: {self.gender}\n' \
               f'Height: {self.height}m\n' \
               f'Hobby: {self.hobby}'

human1 = Person(name='Radomir', age=24, gender='male', height=1.84, hobby=True)
print(human1)
print('-'*50)
human2 = Person(name='Ivan', age=12, gender='male', height=1.50, hobby=False)
print(human2)
print('-'*50)
print(human1.whtyourname(), human1.age_yo())
print(human2.whtyourname(), human2.age_yo())


# Создать класс Watch + 4 атрибута + 1 свой метод

