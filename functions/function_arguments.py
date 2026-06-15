def full_name(first, last):
    """Объединяет имя и фамилию."""
    return f"{first} {last}"


def power(base, exponent=2):
    """Возводит base в степень exponent (по умолчанию в квадрат)."""
    return base ** exponent


def make_user(username, age, city):
    """Создаёт описание пользователя."""
    return f"{username}, {age} years old, from {city}"


def total_price(prices):
    """Возвращает сумму списка цен."""
    return sum(prices)


if __name__ == "__main__":
    print(full_name("John", "Smith"))
    print(power(5))
    print(power(2, 10))
    print(make_user(age=25, city="Almaty", username="dauren"))
    print("Total:", total_price([10, 20, 30]))
