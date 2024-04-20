


def suma(num1,num2):

    suma = num1 + num2

    return suma

def resta(num1,num2):
    
    resta = num1 - num2

    return resta

def operaciones(num1,num2):

    resultado = f"{suma(num1,num2)} , {resta(num1,num2)}"

    



num1=int(input("Numero 1: "))
num2=int(input("Numero 2: "))

print(f"{suma(num1,num2)} , {resta(num1,num2)}")

print(operaciones(num1,num2))






