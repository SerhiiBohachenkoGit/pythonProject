class Test:
    def __init__(self):
        self.open_data = 500
        self._close_data = 500
        self.__very_close_data = 500
        """
        В случае когда мы имеем 2 подчеркивания, мы имеем доступ к этой переменной только из ее класса
        """
    def pr(self):
        print(self.open_data)
        print(self._close_data)
        print(self.__very_close_data)


x = Test()

# x. ...  инкапсулируемая переменная даже не будет отображаться в списке методов и переменых класса
x.open_data = 10  # получаем доступ к переменной класса Test
x._close_data = 10  # получаем доступ, но не отображается в списке методов
x.__very_close_data = 10  # вообще не получаем доступа к переменной класса Test

x.pr()
