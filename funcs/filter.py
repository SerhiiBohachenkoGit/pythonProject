# filter(func, iterable)

def has_o(string):
    return "o" in string


l = ["one", "two", "three", "four", "five"]

new_l = filter(has_o, l)  # в функцию фильтр мы передаем фильтрующую функцию и то что мы будем фильтровать

print(new_l)  # получаем фильтр обьект
print(list(new_l))  # можем приобраховать его в список
