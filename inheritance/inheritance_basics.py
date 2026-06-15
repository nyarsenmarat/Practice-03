class Animal:
    """Базовый класс животного."""
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    """Собака наследует Animal и добавляет своё."""
    def bark(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    """Кошка наследует Animal."""
    def meow(self):
        print(f"{self.name} says Meow!")


if __name__ == "__main__":
    dog = Dog("Rex")
    dog.eat()
    dog.sleep()
    dog.bark()

    cat = Cat("Whiskers")
    cat.eat()
    cat.meow()

    print("dog is Animal?", isinstance(dog, Animal))
    print("Dog subclass of Animal?", issubclass(Dog, Animal))
