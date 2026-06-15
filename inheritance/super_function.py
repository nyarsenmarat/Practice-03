class Vehicle:
    """Базовый класс транспортного средства."""
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"{self.brand}, max speed {self.speed} km/h")


class Car(Vehicle):
    """Автомобиль; добавляет количество дверей."""
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def describe(self):
        super().describe()
        print(f"It has {self.doors} doors.")


class ElectricCar(Car):
    """Электромобиль; добавляет ёмкость батареи."""
    def __init__(self, brand, speed, doors, battery_kwh):
        super().__init__(brand, speed, doors)
        self.battery_kwh = battery_kwh

    def describe(self):
        super().describe()
        print(f"Battery: {self.battery_kwh} kWh")


if __name__ == "__main__":
    tesla = ElectricCar("Tesla", 250, 4, 100)
    tesla.describe()
