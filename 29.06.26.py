marks = [2,3,4,7,5]
for i in marks:
    if i < 0:
        print(i, end=" ")

for i in range(len(marks)):
    if marks[i] < 0:
        marks[i] *= -1
        print(marks[i],end=" ")
for i in range (len(marks)//2):
    marks[i],marks[len(marks)] marks[len(marks) - (i+1)],marks[i]
print(marks,end=" ")

data = "Всем привет!"
for i in data:
    print(i, end=" ")

a = 678
b = str(a)
print(int(b[2]+b[1]+b[0])*2)

names = ["Иван","Петя","Коля","Ольга","Ева"]
print(names[0][0])
flag = True
for i in range (len(names)):
    for j in range (len(names)):
        if len(names[i]) != len(names[j]):
            flag = False
            break
print(flag and "равны" or "разные")

for i in names:
    if i[len(i)-1]== "а":
        print(i,end=" ")
print()


students = [[2,3,4,3],
            [3,4,3,5],
            [4,4,4,5]]
for i in range(len(students)):
    print(f"student {i+1}: ", end="")
    summa = 0
    for j in students[i]:
        summa += j
        print(j,end=" ")
    print("/",summa/len(students[i]))

sp = [[2,3,4],
      [3,1,7]]

for i in range(len(sp)):
    summa = 0
    for j in sp[i]:
        summa += j
        print(j,end="\t")
    print("=",summa)
result = 0
for i in range(len(sp[0])):
    total = 0
    for j in range (len(sp)):
        total += sp[j][i]
    result += total
    print(total,end="\t")
print("=",result)