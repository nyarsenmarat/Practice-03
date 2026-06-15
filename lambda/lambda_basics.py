double = lambda x: x * 2
print("double(5) =", double(5))

add = lambda a, b: a + b
print("add(3, 4) =", add(3, 4))

say_hi = lambda: "Hi!"
print(say_hi())


def multiplier(n):
    """Возвращает функцию, умножающую свой аргумент на n."""
    return lambda x: x * n


times3 = multiplier(3)
times5 = multiplier(5)
print("times3(10) =", times3(10))
print("times5(10) =", times5(10))


def square_func(x):
    """Возводит число в квадрат."""
    return x ** 2


square_lambda = lambda x: x ** 2
print("square_func(6) =", square_func(6))
print("square_lambda(6) =", square_lambda(6))
