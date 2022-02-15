list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
i=0
j=len(list)
num=int(input("Introduce un numero: "))
medio = len(list)//2
while(list[medio]!=num):
    medio=(i+j)//2
    if list[medio]>num:
        j=medio
    elif list[medio]<num:
        i=medio
print(medio)