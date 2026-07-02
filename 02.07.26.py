import random
#1
# list1 = [0,0,0,0,0,0,0,0,0,0]
# list2 = [0,0,0,0,0,0,0,0,0,0]
# a = int(input("введите диапазон от:"))
# b = int(input("введите диапазон до:"))
# for i in range(len(list1)):
#     list1[i] = random.randint(a,b)
# print(list1)
# n = 0
# max = list1[0]
# max_index = 0
# for i in range(len(list1)):
#     if list1[i] > max:
#         max = list1[i]
#         max_index = i
# for i in range(len(list1)):
#     if list1[i] % 2 == 0:
#         list2[n] = list1[i]
#         n+=1
# for i in range(len(list1)):
#     if list1[i] % 2 != 0:
#         list2[n] = list1[i]
#         n+=1
# print(f"max:{max} index:{max_index}")
# print(list2)

# ФУНКЦИИ
# def show_list():
#     for i in list:
#         for j in i:
#             print(j, end="\t")
#         print()
#
# list = [[65,6,4,5,7,8,9,0],
#         [23,313,46,7,6,756],
#         [12,3,4,5,7,9,5,2]]
#
# show_list()
# def start_program():
#     print("-start program-")
#
# start_program()
# print("n1")
# start_program()
# print("n2")
# start_program()
# print("n3")

# def aver(a,b,c,d):
#     return (a+b+c+d)/4
#
# cl1 = aver(2,3,5,2)
# cl2 = aver(4,4,5,4)
# cl3 = aver(5,3,5,3)
# cl4 = aver(4,3,5,3)
#
# res = aver(cl1,cl2,cl3,cl4)
# print(res)

# def change_list(a):
#     a[0]=2
#
# list1 = [5,6,4]
# change_list(list1)
# print(list1)

# def aver(list1):
#     summ = 0
#     for i in list1:
#         summ += i
#     return summ/len(list1)
#
#
# school = [[2,3,4,4,2,3,4,5],
#           [3,4,5,5,3],
#           [2,3,4,5,5,5,3]]
#
# summa = 0
# for i in school:
#     summa += aver(i)
# print(summa/len(school))

def maximum(list1):
    maximum=list1[0]
    for i in range(len(list1)):
        if list1[i] > maximum:
            maximum = list1[i]
    return  maximum


school = [[2,3,4,4,2,3,4,5],
          [3,4,5,5,3],
          [2,3,4,5,10,5,3]]

max = 0
index_max = 0
for i in range(len(school)):
    if max < maximum(school[i]):
        max = maximum(school[i])
        index_max = i
    print(index_max)