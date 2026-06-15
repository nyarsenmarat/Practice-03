class Engine:
    """Добавляет поведение двигателя."""
    def start_engine(self):
        print("Engine started.")


class Radio:
    """Добавляет поведение радио."""
    def play_radio(self):
        print("Playing radio.")


class Car(Engine, Radio):
    """Автомобиль наследует Engine и Radio."""
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is driving.")


class A:
    def who(self):
        print("I am A")


class B(A):
    def who(self):
        print("I am B")
        super().who()


class C(A):
    def who(self):
        print("I am C")
        super().who()


class D(B, C):
    def who(self):
        print("I am D")
        super().who()


if __name__ == "__main__":
    car = Car("BMW")
    car.drive()
    car.start_engine()
    car.play_radio()

    print("---")
    d = D()
    d.who()
    print("MRO:", [cls.__name__ for cls in D.__mro__])
