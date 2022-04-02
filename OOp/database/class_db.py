import sqlite3
from random import randint

database1 = sqlite3.connect('server.sqlite7')
sql = database1.cursor()

sql.execute(
    """CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    cash INT 
    )    
    """
)
database1.commit()


def register_user():
    while 1:
        global user_login, user_password, balance
        user_login = input('Login: ')
        user_password = input('Password: ')
        number = randint(1, 2)


        for i in sql.execute(f"SELECT cash FROM users WHERE login = 'user_login' "):
            balance = i[0]

        sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
        if sql.fetchone() is None:
            sql.execute(f'INSERT INTO users VALUES (?, ?, ?)', (user_login, user_password, 0))
            database1.commit()
            print('User registered')
            for value in sql.execute("SELECT * FROM users"):
                print(value)
        else:
            if number == 1:
                sql.execute(f"UPDATE users SET cash {120+ balance} WHERE  login = '{user_login}'")
                print('You Win money')
                database1.commit()
            for value in sql.execute("SELECT * FROM users"):
                print(value)
            else:
                print('You lose')
            for value in sql.execute("SELECT * FROM users"):
                print(value)

        message = str(input('Con...?? y/n'))
        if message == 'y':
            continue
        else:
            break


if __name__ == '__main__':
    register_user()
