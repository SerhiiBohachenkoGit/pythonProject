"""
map(func, *iterable) - принемает:
 1.функцию обработчик
 2.итерируемый обьект(один или много)(например list)
    Возврашает map обьект, который является итератором
 """


def upper(string):
    return string.upper()


l = ['one', 'two', 'three']

new_list = map(upper, l)  # передаем в map функцию обработчик и то что мы будем обрабатывать

print(new_list)  # получаем map обькт

print(list(new_list))  # можем приобразовать его в list
