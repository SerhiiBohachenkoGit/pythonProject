"""
Наследуемся от класса Varification
1) импортируем класс
2) передаем наш класс Родитель в на наш класс Чаилд
"""
from oop.lvl_2.nasledovanie.class_1 import Varification


class V2(Varification):  # класс Чаилд

    # Varification.pr(self) - обращение к методу класса Родителя
    # super().pr() - обращение к методу класса Родителя. Не указывает self
    # при множественном наследовании метод super() ищет в классе выше, если там нет, то идет еще на класс выше и тд
    # super(нужный_класс, self) - если нам нужно получить метод определенного класса

    """
    Пайтон при вызове метода сначала смотрит его в классе Чаилде и если 
    там его нет, тогда идет в класс Родитель.
    Таким образом ПЕРЕОПРЕДЕЛЕНИЕ метода - это метод в классе Чаилде
    с таким же именем как и в классе Родителе
    Точно таким же образом мы можем переопределить метод __init__
    """
    def pr(self):  # переопределение метода класса родителя Varification
        print("я уже переопределен в классе Чаилде  и могу содержать другой функционал")

    def show(self):  # расширяем класс родитель Varification
        print(self.login, self.password)


"""
Так как мы унаследовались от класса Varification, мы уже имеем доступ 
ко всем его поляем и фукциям
"""
y = V2('Jonny', '123456789')  # создаем экземпляр класса V2 который наследован от класса Varification
y.pr()  # метод унаследован от класса Varification(переопределен в классе Чаилде)
y.show()  # метод созданный уже в классе Чаилде V2



