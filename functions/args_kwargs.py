def sum_all(*numbers):
    """Складывает любое количество переданных чисел."""
    total = 0
    for n in numbers:
        total += n
    return total


def print_profile(**info):
    """Печатает произвольный набор данных пользователя."""
    for key, value in info.items():
        print(f"{key}: {value}")


def order(item, *toppings, **details):
    """Оформляет заказ: основной товар, добавки и детали."""
    print(f"Item: {item}")
    print("Toppings:", ", ".join(toppings) if toppings else "none")
    for key, value in details.items():
        print(f"{key}: {value}")


def coordinates(x, y, z):
    """Печатает три координаты."""
    print(f"x={x}, y={y}, z={z}")


if __name__ == "__main__":
    print("Sum:", sum_all(1, 2, 3, 4, 5))

    print_profile(name="Dauren", age=20, city="Astana")

    print("---")
    order("Pizza", "cheese", "mushrooms", size="large", delivery=True)

    print("---")
    point = [1, 2, 3]
    coordinates(*point)

    data = {"x": 10, "y": 20, "z": 30}
    coordinates(**data)
