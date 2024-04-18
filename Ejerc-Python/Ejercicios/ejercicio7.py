

num1= int(input("Ingrese un primer numero: "))
num2= int(input("Ingrese un segundo numero: "))


if(num1<num2):

    for i in range(num1,num2+1):

         if(i%2==0):

            print(i)

else:
    print("el segundo numero no puede ser menor al primer numero")

