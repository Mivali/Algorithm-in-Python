size=int(input("Introduce a number")) 
first_number=0
second_numer=1

def fibonacci(number):
    if(number == first_number):
        return first_number
    elif(number == second_numer):
        return second_numer
    else:
        return (fibonacci(number - 1) + fibonacci(number - 2))
        
for size in range (0, size):
    print(fibonacci(size))

