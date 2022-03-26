class Acount:
    def __init__(self, login, password, secret_key):
        self.login = login
        self._password = password
        self.__sk = secret_key

    def balance(self, summary):
        return f'Summary{summary}$'

    def __str__(self):
        return f'Login: {self.login}\n' \
               f'pass: {self.password}\n' \
               f'sk: {self.sk}'

acc = Acount(login='Radomi@gmail.com', password=12345, secret_key='12jvjnvsdk#$&*(!))*$&)@!_')
print(acc.__balance(1234))
print(acc.sk)
print(acc.password)

