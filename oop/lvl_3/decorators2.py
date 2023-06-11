from datetime import datetime as dt


class Player:
    """
    Геретеры и сетеры используются для работы с инкапсулируемыми данными
    """

    __LVL, __HELTH = 1, 100
    __slots__ = ['__lvl', '__helth', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL  # к инкапсулируемым переменным можем получить доступ только через Имя_класса.имя_переменной
        self.__helth = Player.__HELTH
        self.__born = dt.now()

    @classmethod  # метод который взаимодействует только с данным классом, а не с его экземплярами
    def set_cls_field(cls, lvl=1, helth=100):  # в параметр cls будет попадать имя класса который запускается
        cls.__LVL = Player.__typeTest(lvl)   # ----------------------------- вот тут staticmethod
        cls.__HELTH = Player.__typeTest(helth)   # ----------------------------- вот тут staticmethod

    """
    работа с гетерами и сетарами с помощтю пропертей:
    1) сетера не модет быть без гетера
    2) гетер может быть без сетера
    3) имена функций должны быть одинаковыми 
    """
    """
    метод getter, нужен для того что бы получить данные с инкапсулированной переменной
    """
    @property  # это и есть геттер
    def lvl(self):
        return self.__lvl

    """
    метод setter, нужен для того что бы изменять данные в инкапсуриемой переменной
    """
    @lvl.setter  # имя функции.сетер - это и есть сетер
    def lvl(self, numeric):  # numeric - на какое число увеличить лвл
        self.__lvl += Player.__typeTest(numeric)  # ----------------------------- вот тут staticmethod

    @staticmethod  # не работает не с классом не с его экземпляром
    def __typeTest(value):  # поверяем на инт
        if isinstance(value, int):
            return value
        else:
            return TypeError('Должен быть int')


"""
работа с декораторами
"""
y = Player()
print(y.lvl)  # если просто вызываем - то это гетер
y.lvl = 2  # если присваиваем значение - то это сетер
print(y.lvl)


"""
работа с @classmethod
"""
Player.set_cls_field(10)  # пишем имя нашего @classmethod
x = Player()
print(x.lvl)

Player.set_cls_field()
y = Player()
print(y.lvl)
