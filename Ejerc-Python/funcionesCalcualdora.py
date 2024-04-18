



def calculadora(num1, num2, basico=False):

    suma=num1 + num2
    resta=num1-num2
    multi=num1*num2
    divi=num1/num2

    cadena=""

    if basico ==False:
        cadena += "suma "+str(suma)
        cadena += "\n"
        cadena += "resta "+str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion "+str(multi)
        cadena += "\n"
        cadena += "division "+str(divi)
        cadena += "\n"
        

    return cadena


print(calculadora(5,6, True))

"""def Calculadora(num1,num2):
    
    retorno=""

    retorno += str(num1 + num2)
    retorno += str()
    retorno += str(num1-num2)

    return retorno
    


print(Calculadora(3,4))"""