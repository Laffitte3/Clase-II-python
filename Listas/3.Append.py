
"""
closet=["short","franela","medias"]

print(closet)


closet=["short","franela","medias","perfume"]

print(closet)

closet.append("perro")

print(closet)

"""

animales =["jirafa","tigre","hipopotamo"]
running=True

while running:

    print("Opciones\n1.Añadir animal\n2.Mostrar lista\n3.Borrar\n4.Salir")

    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
      
      animal=input("Ingrese el animal: ")
      animales.append(animal)

    if opcion == 2:
       print(animales)

    if opcion == 3:
       borrar=int(input("Ingrese el nuemro de animal que desea borrar"))
       animales.pop(3)

    if opcion == 4:
       running = False

    print("\n")



