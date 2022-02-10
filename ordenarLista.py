list = [3, 1, 5, 2, 4]
aux=0

for x in range(0,len(list)):
    for j in range(0,len(list)):
        if list[x] < list[j]:
            aux=list[j]
            list[j] = list[x]
            list[x] = aux
print(list) 




