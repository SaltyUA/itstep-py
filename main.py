# import logging

# logging.basicConfig(level=logging.DEBUG, 
#                     filename="logs.log", 
#                     filemode="w",
#                     format="We have next loggingmessage:%(asctime)s:%(levelname)s - %(message)s")

# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exception")

# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

# logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 
# logging.info('Програма успішно запущена')

# logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s') 

# def divide(a, b): 
#     try: 
#         result = a / b 
#         return result 
#     except ZeroDivisionError as e:
#         logging.error(f'Division error: {e}') 

# divide(10, 0)

#Тести. Модуль doctest - доктести. Модуль unittest - Unit-тести.

# if 2+2 == 4:
#     print("In fact, 2 + 2 equals 4")

# assert 2 + 2 == 5, 'wrong assert'


# #Доктести
# """
# >>> assertion
# result
# """
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

# """
# >>> 2+2
# 5
# """
 
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

# #Unit-тести
# def adder(*args, **kwargs):
#     result = 0
#     for _ in args:
#         result += _
#     for _ in kwargs.values():
#         result += _
#     return result

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result+=float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result+=int(_)
                continue
            except (ValueError, TypeError):
                pass
    for _ in kwargs.values():
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
    return result