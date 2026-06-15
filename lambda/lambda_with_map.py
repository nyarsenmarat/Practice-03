numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print("Fahrenheit:", fahrenheit)

words = ["python", "lambda", "map"]
upper_words = list(map(lambda w: w.upper(), words))
print("Upper:", upper_words)

list_a = [1, 2, 3]
list_b = [10, 20, 30]
sums = list(map(lambda a, b: a + b, list_a, list_b))
print("Element-wise sum:", sums)
