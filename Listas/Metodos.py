
i=0



personas=[1,3,5,2,4,9,7]

netflix=[]

print(personas)

personas.sort()

print(personas)

personas.append(8)

print(personas)

personas.insert(4,"Numero de personas")

print(personas)
#
personas.remove("Numero de personas")

print(personas)
#
personas.sort()

print(personas)

personas.reverse()

print(personas)

personas.insert(1,6)

print(personas)


cantidad_personas= len(personas)

print("La cantidad de personas es de: "+ str(cantidad_personas))

print("\n")

    
limite=int(input("Ingrese la cantidad d eveces que desea agregar elementos: "))

for agregar in range(limite):

    agregar=input("Agrega tus peliculas: ")

    netflix.append(agregar)


print(netflix)

netflix.append("Juegos del hambre")

print(netflix)

cantidad_peliculas=len(netflix)

print("La cantidad d epeliculas es de: "+str(cantidad_peliculas))


print("\nUnir listas:\n")



