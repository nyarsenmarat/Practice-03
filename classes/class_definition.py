class Dog:
    """Класс, описывающий собаку."""
    pass


class Car:
    """Класс автомобиля."""
    pass


class Calculator:
    """Простой калькулятор."""
    def add(self, a, b):
        """Складывает два числа."""
        return a + b


class Point:
    """Точка с координатами x и y."""
    def show(self):
        print(f"Point({self.x}, {self.y})")


if __name__ == "__main__":
    d = Dog()
    print("Dog object:", d)

    my_car = Car()
    my_car.brand = "Toyota"
    my_car.year = 2020
    print(f"{my_car.brand}, {my_car.year}")

    calc = Calculator()
    print("2 + 3 =", calc.add(2, 3))

    p1 = Point()
    p1.x, p1.y = 1, 2
    p2 = Point()
    p2.x, p2.y = 5, 6
    p1.show()
    p2.show()
