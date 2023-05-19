import decimal

a = None  # неопределенное значение

# Numeric Type
i: int = 100   # целое число
f: float = 1.10  # вещественное число (с плавающей запятой)

dec: decimal = 1.12345  # число с определенным количеством симболов после запятой
com: complex = 1 + 2j

# Text Sequence Type
s: str = "Hello, i'm string"

# Boolean Type - True/ False
b1: bool = True
b2: bool = False

# Sequence Type
l: list = [1, 2, 3, "a", "b", "c"]  # СПИСОК
t: tuple = (1, 2, 3, "a", "b", "c")  # КОРТЕЖ, нельзя изменять, меньше занимает места на диске

# Set Types
se: set = {1, 2, 3, "a", "b", "c"}  # МНОЖЕСТВО, только уникальные значения и не имеет порядка
fr: frozenset = {1, 2, 3, "a", "b", "c"}  # НЕИЗМЕНЯЕМОЕ МНОЖЕСТВО

# Mapping Types
d: dict = {"key": "value"}  # СЛОВАРЬ, ключ: значение. Не имеет порядка

# Constants
CONST = "Hello"  # константы пошутся апперкейсом

# Mutable и Immutable obj (Изменяемы и неизменяемый  обьект)
# изменяемый объект можно изменить после его создания, а неизменяемый – нет
# list, set, dict - изменяемые
# int, float, frozenset, bool, str, tuple - неизменяемыe