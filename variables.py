import decimal

a = None  # неопределенное значение

# Numeric Type
i: int = 100
f: float = 1.10
dec: decimal = 1.123

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