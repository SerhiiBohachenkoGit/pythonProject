""" Исключения """

try: #  попробуй сделать
    2/0
except ZeroDivisionError: #  если получишь такую ошибку то сделай
    print("Ошибка")
else: #  сделай если ошибка не появится
    print("Ошибки нет")
finally: #  выполнится в любом случае
    print("Выполнится в любом случае")
