# -------------------------------------------------------Задача 26-----------------------------------------------------
def in_power(base, power):
    if power == 0:
        return 1
    else:
        return base*in_power(base, power-1)

# print(in_power(int(input("Input base: ")), int(input(("Input power: ")))))

# -------------------------------------------------------Задача 28-----------------------------------------------------

def my_sum (first_digit, second_digit):
    if second_digit == 1:
        return first_digit+1
    else:
        return my_sum(first_digit+1, second_digit-1)

# print(my_sum(10, 999))

# -------------------------------------------------------Задача 28.2-----------------------------------------------------
def binary(number):
    if number//2 >=1:
        print(int(number%2))
        return str(binary(number/2))+ str(int(number%2))
    else:
        return 1

# print(binary(258))

# -------------------------------------------------------Задача 34-----------------------------------------------------

def find_rythm(sometext: str):
    vowelsalphabet = ['а','е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    somelist = sometext.split()
    result = []
    for i in somelist:
        result.append(len(list(filter(lambda x: x.lower() in vowelsalphabet, i))))
    return ("Парам пам-пам (ритм есть)" if result.count(result[0])==len(result) else "Пам парам (ритма нет)")

# print(find_rythm("парам пим пэм"))
# print(find_rythm("ПУМ-парам бири-рАм пим-пяк-чмяк"))

# -------------------------------------------------------Задача 36-----------------------------------------------------
from typing import Callable

def print_operation_table(operation: Callable, num_rows=6, num_columns=6):
    horizont = [(i+1) for i in range(num_columns)]
    for j in range(num_rows):
        templist = [operation(horizont[i], j+1) for i in range(num_columns)]
        print(*templist, sep='\t')

# print_operation_table(lambda x, y: x*y, 10, 10)