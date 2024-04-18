

#Parametros
"""
name= "Pedro"
def nombre():

    print(f"Mi nombre es {name}")

nombre()

"""

"""name="pedro"

def nombre(name1):
    print(f"Nombre: {name1}")


nombre("Alejandro")
nombre("Jesus")"""


"""
def nombre(name):
    print(f"Mi nombre es {name}")


name1 = input("Ingresa tu nombre: ")
nombre(name1)
"""


def graduacion(nombre,notas,salir):
    global running

    print(f"\nNombre estudiante: {nombre}")

    if salir != "si":

        if (notas>=12) and (notas<=20) :
            print("AJA mi panita te puedes graduar")

        else:
            if notas<12:
                print("Raspaste, debes repoetir la materia")
            
            if notas>20:
                print("Este no es un numero valido")

    else:
        print("Vuelva pronto")
        running =False


running = True
while running:

    salir=input("Deseas salir: ")

    name=input("Ingresa el nombre del estudiante: ")
    notas=int(input(f"Ingresa las notas de {name} :"))
    

    graduacion(name,notas,salir)


    




