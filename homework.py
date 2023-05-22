# --------------------------------------------------------Задача 2--------------------------------
# Найдите сумму цифр трехзначного числа.
# number = int(input("Input three digits number: "))
# if number > 99 and number < 1000:
#     print(f'Sum of digits in {number} is {number%10 + number//10%10 + number//100}')
# else:
#     print("Error")

# --------------------------------------------------------Задача 4---------------------------------------------------

# sum = int(input("Input how many cranes children was made: "))
# if sum < 4:
#     print("You underestimate their power")
# elif sum%6!=0:
#     print("Error")
# else:
#     print(f'Petya and Seryozha made {sum/6} cranes each, Katya made {sum/3*2}')

# -------------------------------------------------------Задача 6-----------------------------------------------------

# ticketnumber = int(input("Input six digits of your ticket number: "))
# if ticketnumber > 999999 or ticketnumber < 1:
#     print("Error")
# else:
#     leftsum = ticketnumber // 100000 + ticketnumber // 10000 % 10 + ticketnumber // 1000 % 10
#     rightsum = ticketnumber // 100 % 10 + ticketnumber // 10 % 10 + ticketnumber % 10
#     if leftsum == rightsum:
#         print("Your ticket is happy")
#     else:
#         print("Your ticket is not happy")

# -------------------------------------------------------Задача 8-----------------------------------------------------

# lenght = int(input("What is the lenght of your chocolate bar: "))
# width = int(input("What is the width of your chocolate bar: "))
# slices = int(input("How many slices you want to break off: "))
# if slices >= lenght*width:
#     print("You are greedy")
# else:
#     if slices % lenght ==0 or slices % width== 0:
#         print ("It's possible")
#     else:
#         print("Mission impossible. Call to Ethan Hunt.")

