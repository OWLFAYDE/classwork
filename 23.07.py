#1
# num1 = int(input("введите число: "))
# num2 = int(input("введите 2 число: "))
# num3 = int(input("введите 3 число: "))
# num4 = int(input("введите 4 число: "))
# if num1 == num2 and num1 == num3 and num1 == num4:
#     print("Числа равны")
# else:
#     max_num = num1
#     if num2 > max_num:
#         max_num = num2
#     if num3 > max_num:
#         max_num = num3
#     if num4 > max_num:
#         max_num = num4
#     print("Наибольшее число", max_num)

#2
# a = int(input("введите начало диапозона: "))
# b = int(input("введите конец диапозона: "))
# for i in range(a,b,-1):
#     if a > b:
#         a,b = b,a
#     grade = i
#     print(i, end=" ")

#3
# n = int(input("Введите сторону квадрата: "))
# for p in range(n):
#     for j in range(n):
#         if j >= p and j <= n - 1 - p:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#4
# simvol = input("введите символ: ")
# if simvol == simvol.:
#     print("yes")
# else:
#     print("no")

#5
# list = []
# for i in range(0,len(list)):
#     list.append(i * 3)
# print(list)

#6

#7

#8

#9
# def grade(number: list[int]):
#     for num in number:
#         if num % 2 != 0:
#             yield num
#
# ls = [2,3,5,1,5,7,54,2,5,7,20,5,34]
# print(list(grade(ls)))

#10

#11
# def count_numbers(num):
#     numbers = num.split()
#     count = 0
#     for i in numbers:
#         if i.isdigit():
#             count += 1
#
#     return count

#12
