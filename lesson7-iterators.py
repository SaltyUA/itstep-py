#  Ітератори
# my_list = [1, 2, 3]
# iterator = iter(my_list)

#  Ручний перебір ітератора
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

#  Пройтись ітератором можна також через цикл
# for elem in iterator:
#     print(elem)

# Ітеровані об'єкти
# Метод __iter__() має повертати посилання на об'єкт ітератора
# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
    
# count = Counter(5)

# for elem in count:
#     print(elem)

# Можна окремо викликати кожен із методів __iter__() та __next__(), котрі поводитимуться аналогічно функціям iter() та next()
# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#     def __repr__(self):
#         return f"Counter(max_number={self.max_number}, current={self.i})"
    
# count = Counter(5)

# print(count.__next__())
# print(count.__iter__()) 
# print(next(count))
# print(iter(count))
# print(next(count))

# Робота з генераторами. Виклик і замикання функцій
# def raise_to_the_degrees(number, max_degree):
#     i=0
#     for _ in range(max_degree):
#         yield number**i
#         i+=1
 
# res = raise_to_the_degrees(2, 500)

# print(res)
# for _ in res:
#     print(_)

#Завдяки «лінивим» обчисленням генератор може працювати нескінченно й не перевантажувати обчислювальну машину
# def raise_to_the_degrees(number):
#     i=0
#     while True:
#         yield number**i
#         i+=1
# res = raise_to_the_degrees(122345)
# print(res)
# for _ in res:
#     print(_)

#оператор return, який «під капотом» Python генерує виняток StopIteration
# def raise_to_the_degrees(number):
#     i=0
#     while True: 
#         result = number**i
#         yield result
#         if result > 100**20:
#             return
#         i+=1

# res = raise_to_the_degrees(122345)
# print(res)

# for _ in res:
#     print(_)

#Виклик об'єктів і замикання функцій
#Метод __call__()

# class Helper:
#     def __init__(self, work):
#         self.work = work
#     def __call__(self, work):
#         return f"I will help you with your {self.work}. Afterwards I will help you with {work}"
    
# helper = Helper("homework")
# print(helper("cleaning"))

#Таке саме, але тільки з функцією
# def helper(work):
#     work_in_memory = work
#     def helper(work):
#         return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
#     return helper
# helper = helper("homework")
# print(helper("cleaning"))
# print(helper("driving"))

# #Робота з декораторами
# Перевірка роботи функції через замикання
# def checker(function):
#     def checker(*args, **kwargs):
#         try:
#             result = function(*args, **kwargs)
#         except Exception as exc:
#             print(f"We have problems {exc}")
#         else:
#             print(f"No problems. Result - {result}")
#     return checker

# def calculate(expression):
#     return eval(expression)

# calculate = checker(calculate)
# calculate("2+2")

#В Python є «синтаксичний цукор», який робить ту саму операцію замикання, зменшуючи кількість коду
# def checker(function):
#     def checker(*args, **kwargs):
#         try:
#             result = function(*args, **kwargs)
#         except Exception as exc:
#             print(f"We have problems {exc}")
#         else:
#             print(f"No problems. Result - {result}")
#     return checker

# @checker
# def calculate(expression):
#     return eval(expression)

# calculate("2+2")

#Давайте спробуємо модифікувати нашу програму та створити декоратор вищого рівня, який буде ловити лише вказані типи помилок:
# def checker(*exc_types):
#     def checker(function):
#         def checker(*args, **kwargs):
#             try:
#                 result = function(*args, **kwargs)
#             except (exc_types) as exc:
#                 print(f"We have problems {exc}")
#             else:
#                 print(f"No problems. Result - {result}")
#         return checker
#     return checker

# @checker(NameError, TypeError, SyntaxError)
# def calculate(expression):
#     return eval(expression)

# calculate("2+2")

#Практика

# Ітератор, який повертає парні числа до заданого ліміту

# class EvenNumbers:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while self.current < self.limit:
#             if self.current % 2 == 0:
#                 even_number = self.current
#                 self.current += 1
#                 return even_number
#             self.current += 1
#         raise StopIteration

# even_iterator = EvenNumbers(10)
# for num in even_iterator:
#     print(num)

# # Генератор, який повертає випадкові координати на ігровому полі

# import random

# def coordinate_generator():
#     while True:
#         yield random.randint(0, 100), random.randint(0, 100)

# coord_gen = coordinate_generator()

# for _ in range(5):
#     x, y = next(coord_gen)
#     print(f"X: {x}, Y: {y}")


# # Декоратор, який логує виклики функції, аргументи та результат

# def logging_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} called with arguments: {args}, {kwargs}")
#         print(f"Result: {result}")
#         return result
#     return wrapper

# @logging_decorator
# def add(a, b):
#     return a + b

# add(5, 10)
# add(20, 30)
