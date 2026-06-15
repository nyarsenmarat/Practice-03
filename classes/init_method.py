class Person:
    """Человек с именем и возрастом."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Представляет человека."""
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


class Book:
    """Книга. Год издания по умолчанию неизвестен."""
    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        year_text = self.year if self.year else "unknown year"
        print(f"'{self.title}' by {self.author} ({year_text})")


class Temperature:
    """Температура в градусах Цельсия."""
    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"


class Rectangle:
    """Прямоугольник; площадь считается при создании."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height


if __name__ == "__main__":
    p = Person("Dauren", 20)
    p.introduce()

    b1 = Book("1984", "George Orwell", 1949)
    b2 = Book("Untitled", "Anonymous")
    b1.info()
    b2.info()

    t = Temperature(36)
    print(t)

    r = Rectangle(4, 5)
    print("Rectangle area:", r.area)
