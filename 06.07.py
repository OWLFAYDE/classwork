# def limit_min(list):
#     mix_index = 0
#     minimum = list[0]
#     for i in range(len(list)):
#         if list[i] < minimum:
#             minimum = list[i]
#             mix_index = i
#     return mix_index
#
# list = [1,2,3,4,5,6,7,8,-12,10]
# print(limit_min(list))

# a = int(input())
# b = int(input())
# if a > b: a,b = b,a

# list = [4,2]
# if list[0] > list[1]:
#     list[0],list[1] = list[1],list[0]
# print(list)

def swap(list,index1,index2):
    list[index1],list[index2]=list[index2],list[index1]

list = [2,1,4,5,3,4,67,2,6,7,4,3,5,2,6,7,3,67,6,43,7,34,65,34,6,3,5,3]

#Bubble sort - сортировка пузыриками
# for j in range(len(list)-1):
#     flag = True
#     for i in range(len(list)-1-j):
#         if list[i] > list[i+1]:
#             flag = False
#             swap(list,i,i+1)
#     if not flag:
#         break
# print(list)

#insertion sort - сортировка вставками
# for i in range(1,len(list)):
#     for j in range(i,0,-1):
#         if list[j] < list[j - 1]:
#             list[j],list[j - 1] = list[j - 1],list[j]
#         else:
#             break
# print(list)

# def name_function():
#     print("win")
#     global a
#     a-= 1
#     if a > 0:
#         name_function()
#
# name_function()


# def show():
#     num = int(input("введите число: "))
#     if num == 0:
#         return 0
#     else:
#         return num + show()
# total = show()
# print(total)