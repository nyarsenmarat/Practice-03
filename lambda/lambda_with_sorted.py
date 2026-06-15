words = ["banana", "kiwi", "apple", "fig"]
by_length = sorted(words, key=lambda w: len(w))
print("By length:", by_length)

students = [
    {"name": "Anna", "grade": 88},
    {"name": "Boris", "grade": 95},
    {"name": "Clara", "grade": 72},
]
by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print("By grade (high to low):")
for s in by_grade:
    print(f"  {s['name']}: {s['grade']}")

points = [(1, 5), (3, 2), (2, 8)]
by_second = sorted(points, key=lambda p: p[1])
print("By second value:", by_second)

names = ["bob", "Alice", "charlie", "Dave"]
case_insensitive = sorted(names, key=lambda n: n.lower())
print("Case-insensitive:", case_insensitive)
