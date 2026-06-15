numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

values = [-5, 3, -2, 8, 0, -1, 7]
positives = list(filter(lambda x: x > 0, values))
print("Positive numbers:", positives)

words = ["cat", "elephant", "dog", "giraffe", "ant"]
long_words = list(filter(lambda w: len(w) > 4, words))
print("Long words:", long_words)

items = ["apple", "", "banana", "", "cherry"]
non_empty = list(filter(lambda s: s != "", items))
print("Non-empty:", non_empty)
