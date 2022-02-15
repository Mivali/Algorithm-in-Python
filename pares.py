#numeros pares hasta el 20

num= input("Introduce un numero: ")
num= int(num)
c=0

for i in range(num):
    
    if i % 2 == 0:
        print(str(i)+ " es numero par")
    c+=1

print("Hay "+str(c)+ " numeros pares.")
    
