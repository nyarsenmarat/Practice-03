# Practice 3: Python Functions and Object-Oriented Programming

Учебные примеры по функциям, lambda-выражениям, классам и наследованию в Python.

## Структура проекта

```
Practice-03/
├── functions/
│   ├── basic_functions.py      # определение и вызов функций, докстринги
│   ├── function_arguments.py   # позиционные, именованные, аргументы по умолчанию
│   ├── return_values.py        # возврат одного/нескольких значений, ранний return
│   └── args_kwargs.py          # *args и **kwargs, распаковка
├── lambda/
│   ├── lambda_basics.py        # синтаксис lambda, lambda vs обычная функция
│   ├── lambda_with_map.py      # lambda + map() для преобразования
│   ├── lambda_with_filter.py   # lambda + filter() для отбора
│   └── lambda_with_sorted.py   # lambda + sorted() для своей сортировки
├── classes/
│   ├── class_definition.py     # определение класса, создание объектов
│   ├── init_method.py          # конструктор __init__, __str__
│   ├── class_methods.py        # методы, self, изменение/удаление атрибутов
│   └── class_variables.py      # переменные класса vs экземпляра
├── inheritance/
│   ├── inheritance_basics.py   # родитель/потомок, isinstance, issubclass
│   ├── super_function.py       # вызов методов родителя через super()
│   ├── method_overriding.py    # переопределение методов, полиморфизм
│   └── multiple_inheritance.py # множественное наследование, MRO
└── README.md
```

## Как запускать

Каждый файл — самостоятельный и запускается отдельно. Из папки `Practice-03`:

```bash
python functions/basic_functions.py
python lambda/lambda_with_map.py
python classes/init_method.py
python inheritance/super_function.py
```

## Изученные темы

1. **Функции** — определение, аргументы (позиционные, по умолчанию, `*args`, `**kwargs`), возврат значений, докстринги.
2. **Lambda** — анонимные функции с `map()`, `filter()`, `sorted()`.
3. **Классы и объекты** — `__init__`, `self`, методы, переменные класса и экземпляра.
4. **Наследование** — `super()`, переопределение методов, множественное наследование.

## Ресурсы

- [W3Schools Python Functions](https://www.w3schools.com/python/python_functions.asp)
- [W3Schools Python Lambda](https://www.w3schools.com/python/python_lambda.asp)
- [W3Schools Python Classes](https://www.w3schools.com/python/python_classes.asp)
- [W3Schools Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)
