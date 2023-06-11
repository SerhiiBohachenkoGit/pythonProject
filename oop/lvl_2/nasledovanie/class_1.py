class Varification:  # класс Родитель

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()  # можем прямо в конструкторе запускать нужные нам методы

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError('слабый пароль')

    def pr(self):
        print(f'Save acc: {self.login}, {self.password}')
