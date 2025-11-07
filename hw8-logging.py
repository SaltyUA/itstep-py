import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"⏱ Function '{func.__name__}' executed in {duration:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_add(a, b):
    time.sleep(0.5)  # Симуляція затримки
    return a + b

#test.py
import unittest

class TestTimingDecorator(unittest.TestCase):
    def test_result_correctness(self):
        self.assertEqual(slow_add(2, 3), 5)

    def test_execution_time(self):
        start = time.time()
        result = slow_add(10, 20)
        end = time.time()
        self.assertEqual(result, 30)
        self.assertGreaterEqual(end - start, 0.5)  # Має бути щонайменше 0.5 сек

if __name__ == "__main__":
    unittest.main()
