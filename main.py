# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

import random
def sum_numbers(number_a, number_b):
    if number_b == 0:
        return number_a
    else:
        return 1 + sum_numbers(number_a, number_b - 1)

number_a = int(random.randint(1, 100))
print(number_a)
number_b = int(random.randint(1, 100))
print(number_b)
print(sum_numbers(number_a, number_b))