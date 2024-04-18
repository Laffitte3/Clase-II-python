


def suma(num1,num2):

    suma = num1 + num2

    return suma

def resta(num1,num2):
    
    resta = num1 - num2

    return resta

def operaciones(num1,num2):

    resultado = [resta(num1,num2),suma(num1,num2)]

    return resultado



num1=int(input("Numero 1"))
num2=int(input("Numero 1"))

#print(f"{suma(5,7)} + {resta(10,6)}")

print(operaciones(num1,num2))




