"""
Registro=[["alejandro",19579869],["Pedro",1245678],["katherine",14567890]]


for elemento in Registro:

    for contenido in elemento:
        print(contenido)

    print("\n")
    """

per1=["alejandro",19579869]
per2=["Pedro",1245678]
per3=["katherine",14567890]

Registro=[per1,per2,per3]

print(Registro)

print("\n\n")

for personas in Registro:
    
    print(f"Elemento {Registro.index(personas)} de la Lista principal\n")

    for item in personas:

        print(f"Elemento {personas.index(item)}= {item}")


    print("\n")

