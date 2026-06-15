def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


def min_max(numbers):
    """Возвращает минимальное и максимальное значение из списка."""
    return min(numbers), max(numbers)


def safe_divide(a, b):
    """Делит a на b. Если b == 0, возвращает None."""
    if b == 0:
        return None
    return a / b


def log_message(msg):
    """Печатает сообщение. Явного return нет, поэтому вернёт None."""
    print(f"LOG: {msg}")


if __name__ == "__main__":
    print("Sum:", add(7, 8))

    low, high = min_max([4, 1, 9, 3])
    print(f"min={low}, max={high}")

    print("10 / 2 =", safe_divide(10, 2))
    print("10 / 0 =", safe_divide(10, 0))

    result = log_message("hello")
    print("log_message returned:", result)
