# zip(inter1, inter2 ...) -> zip obj

l_1 = [1, 3, 5, 7, 9]
l_2 = [2, 4, 6, 8, 10]

new_l = zip(l_1, l_2)  # берет по одному инстансу с каждого и возвращает кортежи

print(zip(new_l))  # получаем zip обькт
print(list(new_l))  # преобразуем в список кортежей
