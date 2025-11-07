# Ітерований об'єкт, який при ітерації повертає генератор парних чисел

class EvenSequence:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return (i for i in range(self.limit) if i % 2 == 0)

# Використання
even_numbers = EvenSequence(10)
for num in even_numbers:
    print(num)

# Декоратор, який обробляє помилки та логує результат

def safe_calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
        except Exception as e:
            print(f"❌ Помилка: {e}")
            return None
        else:
            print(f"✅ Вираз: {expression} = {result}")
            return result
    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)

calculate("2 + 2")
calculate("10 / 0")     
calculate("invalid + 5")  
