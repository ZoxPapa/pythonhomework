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

# -------------------------------------------------------Задача 10-----------------------------------------------------

# qty = int(input("How many coins on the table: "))
# if qty <2:
#     print("Need more gold")
# else:
#     heads = 0
#     tails = 0
#     for i in range(qty):
#         temp = int(input(f"Input heads (1) or tails (0) for the {i+1} coin: "))
#         if temp == 1:
#             heads+=1
#         elif temp ==0:
#             tails +=1
#         else:
#             print("Error")
#             break
#     if heads > tails:
#         print(f"We need to turn {tails} coins")
#     elif tails >heads:
#         print(f"We need to turn {heads} coins")
#     else:
#         print(f"We need to turn a half of all coins - {tails}. ")

# -------------------------------------------------------Задача 12-----------------------------------------------------

# print("Come up with two numbers between 1 and 1000")
# s = int(input("Input sum of them: "))
# p  = int(input("Input product of them: "))
# if p<1 or p>1000:
#     print("Error")
# else:
#     flag = True
#     for i in range(s):
#         firstNumber = s-i
#         secondNumber = i
#         if firstNumber*secondNumber == p and flag:
#             flag = False
#             print(f'So, your numbers are: {firstNumber}, {secondNumber}')
        
# -------------------------------------------------------Задача 14-----------------------------------------------------

# number = int(input("Input some positive number: "))
# i = 0
# while 2**i <= number:
#     print(2**i)
#     i+=1

# -------------------------------------------------------Задача 16-----------------------------------------------------

# from random import randint
# listsize = int(input("Input list size: "))
# somelist = [randint(1,4) for i in range(listsize)]
# number_to_find = int(input("Input number from 1 to 4 to find it's quantity in list: "))
# counter = 0
# print(somelist)
# for i in range(len(somelist)):
#     if somelist[i] == number_to_find:
#         counter +=1
# print(f'{number_to_find} is appears in the list {counter} times')

# -------------------------------------------------------Задача 18-----------------------------------------------------
# from random import randint
# listsize = int(input("Input list size: "))
# somelist = [randint(1,100) for i in range(listsize)]
# number_to_find = int(input("Input some number from 1 to 100. I'll try to find the closest number in the list: "))
# print(somelist)
# diff_list = [abs(somelist[i]- number_to_find) for i in range(listsize)]
# result = diff_list.index(min(diff_list))
# print(somelist[result])

# -------------------------------------------------------Задача 20-----------------------------------------------------
# alphabet = [
#             {'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т' : 1 },
#             {'D, G, Д, К, Л, М, П, У ': 2 },
#             {'B, C, M, P, Б, Г, Ё, Ь, Я': 3 },
#             {'F, H, V, W, Y, Й, Ы': 4 },
#             {'K, Ж, З, Х, Ц, Ч': 5 },
#             {'J, X, Ш, Э, Ю': 8 },
#             {'Q, Z, Ф, Щ, Ъ': 10}
#             ]
# v.1

# word = str(input("Input the word: ")).upper()
# result = 0
# for character in word:
#     for i in range(len(alphabet)):
#         for items in alphabet[i].items():
#             for j in str(items):
#                 if j == character and i <5:
#                     result +=i+1
#                 if j== character and i ==5:
#                     result += 8
#                 if j == character and i == 6:
#                     result+= 10
# print(result)  

#v.2

# word = str(input("Input the word: ")).upper()
# result = 0
# for character in word:
#     for i in range(len(alphabet)):
#         for k, v in alphabet[i].items():
#             for n in k:
#                 if character == n:
#                     result += v
# print(result)  

# -------------------------------------------------------Задача 22-----------------------------------------------------

# from random import randint
# n = int(input("Input size of the first list: "))
# m = int(input("Input size of the second list: "))
# first_list = [int(input(f'Input {i+1} element of the first list: ')) for i in range(n)]
# second_list = [int(input(f'Input {i+1} elemen of the second list: ')) for i in range(m)]
# result_list = [i for i in first_list if i in second_list]
# print(*sorted(result_list))

# -------------------------------------------------------Задача 24-----------------------------------------------------

# from random import randint

# qty_bushes = -1
# while qty_bushes <4:
#     qty_bushes = int(input("How many bushes in the bed: "))
# berry_list = [randint(0, 400) for i in range(qty_bushes)]
# # print(berry_list)
# bush_number = len(berry_list)
# max_qty_3berries = berry_list[0] + berry_list[-1] + berry_list[-2]    #max - if we stay opposite last bush
# for i in range(len(berry_list)-1):
#     current_qty_3berries = berry_list[i] + berry_list[i-1] + berry_list[i+1]
#     #print(current_qty_3berries)
#     if current_qty_3berries > max_qty_3berries:
#         max_qty_3berries = current_qty_3berries
#         bush_number = i + 1
# print(f'We need to stay opposite bush № {bush_number} to collect maximum: {max_qty_3berries}.')