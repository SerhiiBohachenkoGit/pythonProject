if True:
    print("Если условие True,то срабатывает все что в модуле if")

elif True:
    print("Если  условие if не True, то выполняется условие в  модуле elif")

else:
    print("Если ниодно условие в модулях if и elif не сработало, тогда выполняется условие в модуле else")


"""
Switch Case 
появился с пайтон 3.10
"""
http_code = "418"

match http_code:  # обьект с которым работаем
    case "200":  # что ищем
        print("OK") # действие
        do_something_good()
    case "404":
        print("Not Found")
        do_something_bad()
    case "418":
        print("I'm a teapot")
    case _:     # действие которое будет выполнено если ниодион из кейсов не сработает
        print("Code not found")
