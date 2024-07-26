# num = int(input("Введите число "))
# if num % 2 == 0:
#     print("Вы ввели четное число")
# if num % 2 == 1:
#     print("Вы ввели нечетное число")
    

# if num == 0:
#     print("Вы ввели ноль")
# elif num % 2 == 0:
#     print("Вы ввели четное число")
# else:
#     print("Вы ввели нечетное число")


# for i in range(10):
#     num = int(input("Введите число "))
#     if num == 0:
#         print("Вы ввели ноль")
#     elif num % 2 == 0:
#         print("Вы ввели четное число")
#     else:
#         print("Вы ввели нечетное число")


# while True:
#     num = int(input("Введите число для анализа, для выхода введите ноль "))
#     if num == 0:
#         print("Вы ввели ноль")
#         break
#     elif num % 2 == 0:
#         print("Вы ввели четное число")
#     else:
#         print("Вы ввели нечетное число")

# Задача №1. Решение в группах

# def factorial(n):
#     if n == 0:
#         return 1
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result

# # Пример использования
# n = 5
# print(factorial(n))  # Output: 120

# Задача №2. Решение в группах

# def find_fibonacci_index(A):
#     if A <= 1:
#         return -1
    
#     # Начальные значения
#     fib1, fib2 = 0, 1
#     n = 1
    
#     # Поиск числа Фибоначчи
#     while fib2 < A:
#         fib1, fib2 = fib2, fib1 + fib2
#         n += 1
    
#     # Проверка, является ли A числом Фибоначчи
#     if fib2 == A:
#         return n + 1  # +1, так как последовательность Фибоначчи начинается с 1, но мы считаем с 0
#     else:
#         return -1

# # Пример использования
# A = 5
# print(find_fibonacci_index(A))  # Output: 6

# def find_fibonacci_index(A):
#     if A <= 1:
#         return -1
    
#     # Начальные значения
#     fib1, fib2 = 0, 1
#     n = 1
    
#     # Поиск числа Фибоначчи
#     while fib2 < A:
#         fib1, fib2 = fib2, fib1 + fib2
#         n += 1
    
#     # Проверка, является ли A числом Фибоначчи
#     if fib2 == A:
#         return n + 1  # +1, так как последовательность Фибоначчи начинается с 1, но мы считаем с 0
#     else:
#         return -1

# # Запрос числа у пользователя
# A = int(input("Введите натуральное число A (>1): "))

# # Вывод результата
# index = find_fibonacci_index(A)
# print(index)  # Вывод результата


# def find_numbers(s, p):
#     # Создаем список для хранения всех подходящих пар чисел
#     result = []
#     # Перебираем все возможные значения для X от 1 до 1000
#     for x in range(1, 1001):
#         # Вычисляем соответствующее значение Y
#         y = s - x
#         # Проверяем, чтобы y было натуральным числом и чтобы произведение X и Y равнялось P
#         if y >= x and x * y == p:
#             result.append((x, y))
#     return result

# # При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию
# # s = 12
# # p = 27
# # pairs = find_numbers(s, p)
# # for pair in pairs:
# #     print(pair[0], pair[1])

# # Пример использования
# s = 12
# p = 27
# pairs = find_numbers(s, p)
# for pair in pairs:
#     print(pair[0], pair[1])  # Ожидаемый вывод: 3 9

"""
a = int(input("введите число:"))
first = 1
second = 0
current = first+second
n = 3
while current < a:
    n += 1
    second = first
    first = current
    current = first+second

if a != current:
    print("-1")
else:
    print("n=",n)
"""
    
# def longest_thaw_period(temperatures):
#     max_thaw = 0
#     current_thaw = 0
    
#     for temp in temperatures:
#         if temp > 0:
#             current_thaw += 1
#             if current_thaw > max_thaw:
#                 max_thaw = current_thaw
#         else:
#             current_thaw = 0
    
#     return max_thaw

# # Запрос числа дней у пользователя
# N = int(input("Введите количество дней (1 ≤ N ≤ 100): "))

# # Запрос температур у пользователя
# temperatures = []
# for _ in range(N):
#     temp = int(input())
#     temperatures.append(temp)

# # Вывод результата
# longest_thaw = longest_thaw_period(temperatures)
# print(longest_thaw)


"""
dop zadachca 1

def count_digits(number):
    # Учитываем знак числа
    number = abs(number)
    
    # Избавляемся от дробной части
    str_num = str(number)
    
    # Убираем точку из строки и считаем длину
    if '.' in str_num:
        digits_count = len(str_num) - 1
    else:
        digits_count = len(str_num)
    
    return digits_count

# Запрос числа  пользователя
number = float(input("Введите число: "))

# Вывод количества цифр в числе
print(count_digits(number))

"""


"""
dop zadachca 2

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

# Примеры использования
numbers = [23436, 190187200, 380457890232]

for number in numbers:
    print(f"Делители числа {number}: {find_divisors(number)}")

"""
