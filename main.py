import random

def bubble_sort():
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]


print ("how big list you want?")
x = int(input())
list = []
for i in range(x):
    list.append(random.randrange(0,100))
print(list)

bubble_sort()
print(list)
