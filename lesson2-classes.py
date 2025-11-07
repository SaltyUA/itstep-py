#Робота з класами. Створення конструктора класу. Оголошення атрибутів класу. Простір імен та область видимості класів

# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         print("I am alive!")
# first_student = Student()

# class Student:
#     print("Hi")
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students += 1

# nick = Student()
# kate = Student (height=170)
# print(nick.height)
# print(kate.height)


# class Student:
#     height = 160
#     def __init__(self,):
#         print("self.height")
#         self.height += 10

# nick = Student()
# kate = Student()

# class Student:
#     def __init__(self):
#         self.height = 170
#     height = 160
#     def printer(self):
#         print(self.height)
# nick = Student()
# nick.printer()

#Робота з методами класу

#grow() дозволяє змінювати значення зросту студента
# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=1
#     def grow(self, height=1):
#         self.height+=height
# nick = Student()
# kate = Student(height=170)
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)

#Метод __str__ дозволяє визначити як буде виглядати print() екземпляру
# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def __str__(self):
#         return f"I am a student. My name is {self.name}."
# nick = Student(name = "Nick")
# print(nick)

# Метод __del__() автоматично запускається наприкінці програми
# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def __del__(self):
#         print("Training is over. I am now an expert!")
# nick = Student()

# class Student:
#     def __init__(self, name=None, height=160):
#         self.name = name
#         self.height = height
#     def __bool__(self):
#         return self.name != None
#     def __len__(self):
#         return self.height
# nick = Student()
# print(nick.__len__())
# print(nick.__bool__())
# print(len(nick))
# print(bool(nick))