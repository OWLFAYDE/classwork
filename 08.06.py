# num1 = int(input("введите число: "))
# num2 = int(input("введите число: "))
# num3 = int(input("введите число: "))
# if num2>num1 and num2>num3 :
#     print(num2)
# elif num1>num2 and num1>num3:
#     print(num1)
# else:
#     print(num3)
#
# number = int(input("введите число: "))
# if number/2:
#     print("число четное")
# else:
#     print("число не четное")
#
# number = int(input("введите число"))
# if number//10==3 or number %10==3:
#     print("в числе есть (3)")
# else:
#     print("в числе нет (3)")
#
# number = int(input())
# if 10<=number<=20:
#     print("yes")
# else:
#     print("no")
#

# a = int(input())
# b = int(input())
# if a > b:
#     a, b = b, a
# while a <= b:
#     print(a, end=" ")
#     a+=2

# a = int(input())
# b = int(input())
# if a > b: a, b = b, a
# if a %2: a +=1
# while a <= b:
#     print(a, end=" ")
#     a +=2

n = int(input())
k = 0
while n>0:
    num = int(input())
    k+=num
    n-=1
print(k)