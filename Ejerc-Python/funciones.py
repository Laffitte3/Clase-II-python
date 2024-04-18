
def mostrarnombre(name,edad):
    print(f"tu nombre es:  {name} ")

    if edad>18:
        print("No puedes pasar")



name= input("Ingresa tu nombre ")
edad=int(input("Ingresa tu edad"))

mostrarnombre(name,edad)
    