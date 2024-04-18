

"""Hcer un programa que imprima todos los numeros que existen entre dos numeros que digite el usuario"""


num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

if(num1<num2):

    for i in range(num1,num2+1):
    
        print(i)

else:
    print("El numero 2 debe ser mayor al 1")
