import random
# product = {
#     "name": "mouse",
#     "price": 1200.50,
#     "count": 120,
#     "colors": ["red", "blue"]
# }
#
# product["name"]="keyboard"
# product["category"]="accessories"

disciplines = ["eng","math","rus","lit"]

def create_student():
    st1 = {}
    for i in disciplines:
        st1[i] = []
        for j in range(random.randint(3,9)):
            st1[i].append(random.randint(2,5))
    return st1

def avg(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)


def best_discipline(st):
    max = 0
    disc_name = "unnamed"
    for i in st.keys():
        avg_mark = avg(st[i])
        if max < avg_mark:
            max = avg_mark
            disc_name = i
    return disc_name



def discipline(st):
    max = 0
    disc_name = "unnamed"
    for i in st.keys():
        avg_mark = len(st[i])
        if max < avg_mark:
            max = avg_mark
            disc_name = i
    return disc_name

def max_discipline(st):
    result_list = []
    for i in st.keys():
        if len(st[i]) > 0:
            avg_mark = sum(st[i]) / len(st[i])
            if avg_mark >= 3:
                result_list.append(i)
    return result_list


st1 = create_student()
print(st1,best_discipline(st1))
print(f"list discipline {max_discipline(st1)})")
