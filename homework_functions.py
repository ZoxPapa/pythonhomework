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

print(my_sum(10, 999))