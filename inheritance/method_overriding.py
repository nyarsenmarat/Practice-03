class Shape:
    """Базовая фигура."""
    def area(self):
        return 0

    def describe(self):
        print(f"This shape has area {self.area()}")


class Circle(Shape):
    """Круг переопределяет area()."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Square(Shape):
    """Квадрат переопределяет area()."""
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


if __name__ == "__main__":
    shapes = [Circle(5), Square(4), Shape()]

    for shape in shapes:
        shape.describe()
