#  Выведите все элементы, которые меньше 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []
for i in a:
    if i < 5:
        b.append(i)
print(b)

print(list(filter(lambda i: i < 5, a)))

print([i for i in a if i < 5])

#  Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = list(filter(lambda elem: elem in b, a))
result2 = [elem for elem in a if elem in b]
result3 = list(set(a) & set(b))
print(result)
print(result2)
print(result3)
