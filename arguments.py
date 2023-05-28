"""
*args - * применяется с любым итерируемым объектом (кортежем, списком и строками)
**kwargs - ** можно использовать только со словарями
"""

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6


def func_1(*args):  # принимает аргументы и пакует их в list
    print(args)
    print(args[1])


def func_2(**kwargs):  # принимает аргументы в виде k=v и пакует их в dict
    print(kwargs)
    print(kwargs.get('a'))


func_1(a, b, c, d, e, f)
func_2(a=b, c=d, e=f)
