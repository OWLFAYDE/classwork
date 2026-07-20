# int float bool str
# list tuple set dict

# def even_odd(a):
#     if a % 2 == 0:
#         return "odd"
#     else:
#         return "even"

# def fact(n):
#     if n > 1:
#         return n*fact(n-1)
#     else:
#         return 1
#
# print(fact(5))

# ls = [1,2,3,4,5,23.2,"lif"]
# ls[2] = 89
# for i in range(len(ls)):
#     print(ls)

# str = "qweq asdfaf asd qweq xcds asd"
# def simvol(str):
#     words = str.split(" ")
#     result = set()
#     for i in words:
#         if len(i)< 3:
#             result.add(i)
#     return result

# ls1 = [2,123,3,4,1,2,4,1,4,1]
# ls2 = [3,4,2,4,5,1,3,5,1,4,1]
# def join_ls(ls1,ls2):
#     result = set()
#     for i in ls1:
#         if i in ls2:
#             result.add(i)
#     return return
#
# print(set(ls1).intersection(set(ls2)))

str = "   qweqrq  safaoosj    aaaslfj a dada   sanaf   sadlf   waijifjfakf  adam"

def count_words(str):
    words = str.split()
    return len(words)

print(count_words(str))
