
i=0
z=0

print("*********Tabla Multiplicar***********\n\n")

num= int(input("Ingresa un nuemro: "))

print("Tabla de multiplicar del numero{num} \n")


if(num<0):
    print("Ingrese un numero mayor  0")

else:
    for i in range(0,11):

        z= num * i
    
        print(f"{num} * {i} = {z}\n")
        
