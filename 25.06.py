#1
# name = input("Введите ваше имя: ")
# age = int(input("Введите ваш возраст: "))
# print(f"Ваше имя: {name} Ваш возраст: {age}")

#2
# num1 = int(input("Введите число :"))
# num2 = int(input("Введите число :"))
# num3 = int(input("Введите число :"))
# num4 = int(input("Введите число :"))
# if num1 > num2 and num1 > num3 and num1 > num4:
#     print("Наибольшее число: ",num1)
# elif num2 > num1 and num2 > num3 and num2 > num4:
#     print("Наибольшее число: ",num2)
# elif num3 > num1 and num3 > num2 and num3 > num4:
#     print("Наибольшее число: ",num3)
# elif num4 > num1 and num4 > num2 and num4 > num3:
#     print("Наибольшее число: ",num4)
# elif num1 == num2 and num1 == num3 and num1 == num4:
#     print("Числа равны")

#3
# figure = input("Выберите фигуру- square,rectangle?: ")
# if figure == "square":
#     a = int(input("Введите параметры квадрата: "))
#     print(f"площадь квадрата:{a * 4} ")
# elif figure == "rectangle":
#     a = int(input("Введите параметры прямоугольника: "))
#     b = int(input("Введите параметры прямоугольника: "))
#     if a < b:
#       a,b = b, a
#     print(f"Площадь прямоугольника: {a * b}")

#4
# a = int(input("Введите начальное число: "))
# b = int(input("Введите конечное число: "))
# if a < b: a,b=b,a
# for i in range(a, b+1):

#
#     print(i, end=" ")

#5
# total = 0
# while True:
#     num = int(input("Введите число: "))
#     if num != 0:
#         total += num
#     else:
#         print(f"вы ввели ноль, сумма всех чисел {total}")
#         break

#6
# a = int(input("введите начало: "))
# b = int(input("введите конец: "))
# for i in range(b,a,-1):
#     if i % 3 == 0:
#         print(i)
#7
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}*{j}={i * j}")

#8
n = int(input("введите сколько чисел вы хотите ввести: "))
num = int(input("введите числа: "))
max = num
min = num

for i in range(n-1):
    num = int(input("введите числа: "))
    if num < max:
        min = num
    else:
        max = num
print(f"максимальное число:{max} минимальное число{min}")