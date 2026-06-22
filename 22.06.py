# st = [4,5,3,4,2,4,5,3]
# summa = 0
# for i in range(8):
#     if st[i] % 2 == 0:
#         print(st[i] , end=" ")
from sys import flags

# st = [4,5,3,4,2,4,5,3]
# for i in range(7, -1, - 1):
#         print(st[i], end=" ")

# st = [4,5,3,4,2,4,5,3]
# max = st[0]
# for i in range(1,8):
#     if st[i] > max:
#         max = st[i]
#         print(max , end=" ")

# st = [4,5,3,4,2,4,5,3]
# max = st[0]
# for i in range(1,len(st)):
#     if st[i] > max:
#         max = st[i]
#         print(max , end=" ")

# st = [4,5,3,4,2,4,5,3]
# for i in range(1,len(st)):
#     print(st[i], end=" ")

# st = [4,5,3,4,2,4,5,3]
# for i in range(len(st)):
#     if st[i] % 10 == 5:
#         st[i] -=1
#     print(st[i], end=" ")

# st = [4,5,3,4,2,4,5,3]
# for i in range(8):
#     if st[i] % 2 == 0:
#         print(i , end=" ")

# st = [4,5,3,4,2,4,5,3]
# max = st[0]
# max_index = st[0]
# min = st[0]
# min_index = st[0]
# for i in range(len(st)):
#     if max < st[i]:
#         max = st[i]
#         max_index = i
#     if min > st[i]:
#         min = st[i]
#         min_index = i
# print(f"максимальное число: {max} c индексом:  {max_index}")
# print(f"минимальное значение: {min} c индексом {min_index}")

# st = [4,5,3,1,2,6,9,10]
# for i in st:
#     if i % 2 == 0:
#         print(i,end=" ")

# st = [4,5,3,1,2,6,9,10]
# summa = 0
# for i in st:
#     summa +=i
# print(summa,end=" ")

# st = [4,5,3,1,2,6,9,10]
# for i in range(len(st)-1,-1,-1):
#     print(st[i],end=" ")

# ls = [2,3,5,60,89]
# for i in range(len(ls)):
#
#     flag = True
#     for j in range(len(ls)):
#         if i==j:
#             continue
#         if ls[i]==ls[j]:
#             flag = False
#             break
#     if flag:
#         print(ls[i],end=" ")

# ls = [2,3,5,60,89,2,5,60]

# for i in range(len(ls)):
#     flag = True
#     for j in range(i):
#         if ls[i] == ls[j]:
#             flag = False
#             break
#
#     if flag==False:
#         continue
#     for j in range(i + 1, len(ls)):
#         if ls[j] == ls[i]:
#             print(ls[j],end=" ")
#             break
# ls1 = [2,3,5,60,89,2,5,60]
# ls2 = [2,3,5,60,89,2,5,60]
# if len(ls1) != len(ls2):
#     flag = False
# else:
#     flag = True
#     for i in range(len(ls1)):
#         if ls1[i] != ls2[i]:
#             flag = False
#             break
# print(flag,"равны" or "не равны")
