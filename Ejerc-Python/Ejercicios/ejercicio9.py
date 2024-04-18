"""Programa que le pida al usuario un numero indefinidamente hasta que ingrese el numero 111"""



while(True):

    num=int(input("Ingrese un numero"))
    if(num!=111):
        print(num)
    else:
        break
