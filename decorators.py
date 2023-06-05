from datetime import datetime


def timeit(func):
    def wr():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wr


@timeit
def one():
    l = []
    for i in range(10):
        if i % 2 == 0:
            l.append(i)
    return l


@timeit
def two():
    l = [x for x in range(10) if x % 2 == 0]
    return l


l1 = one()
l2 = two()
