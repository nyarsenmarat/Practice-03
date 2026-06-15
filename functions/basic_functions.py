def greet():
    """Печатает приветствие."""
    print("Hello from a basic function!")


def greet_person(name):
    """Принимает имя и печатает персональное приветствие."""
    print(f"Hello, {name}!")


def square(number):
    """Возвращает квадрат переданного числа."""
    return number * number


def describe_square(number):
    """Использует square() и выводит результат."""
    result = square(number)
    print(f"The square of {number} is {result}")


if __name__ == "__main__":
    greet()
    greet_person("Dauren")
    print("3 squared =", square(3))
    describe_square(5)
    help(square)
