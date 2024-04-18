"""Pedir 2  numeros al usuario y hacer las operaciones basicas de una calculadiora"""


print("*********Operaciones Aritmeticas***********\n\n")

print("Opciones disponibles \n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n")



i=0

while(i<=50):

    opcion=int(input("Ingrese su opcion: "))

    num1=int(input("Ingrese le primer numero: "))
    num2=int(input("Ingrese le segundo numero: "))

    if(opcion==1):
        suma=num1+num2
        print(suma)
        
    
    if(opcion==2):
        resta=num1-num2
        print(resta)
        

    if(opcion==3):
        multipli=num1*num2
        print(multipli)
        
    
    if(opcion==4):
        division=num1/num2
        print(division)
        
    i +=1

    