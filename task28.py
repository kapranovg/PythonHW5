# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4

def sum(a = int(input('add A: ')), b = int(input('add B: '))):
    if b == 0:
        return a
    return 1 + sum(a, b-1)

print(sum())