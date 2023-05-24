#  генератор списка
list_1 = [i for i in range(2, 10, 2)]
print(list_1)
print('')

#  генератор множества
set_1 = {i for i in range(2, 10, 2)} #  уникальные значения
print(set_1)
print('')

#  генератор словаря
dict_1 = {i: i*2 for i in range(2, 10, 2)}
print(dict_1)
print('')

#  выражение генератор
f = (x for x in range(10))
print(next(f))
print(next(f))
print(next(f))
print('')

#  функция генератор
def generate_ints():
    for i in range(10):
        yield i

func = generate_ints()
print(next(func))
print(next(func))
print(next(func))
