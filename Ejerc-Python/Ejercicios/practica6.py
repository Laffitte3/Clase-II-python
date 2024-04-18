

"""Mostrar todas las tablas de multiplicar del 1 al 10
Mostrando el titulo de la tabla y luego las multiplicaciones"""




for j in range(1,11):

    print(f"\nTabla de multiplicar del numero {j} \n")
    
    for i in range(0,11):

        z=j*i
    
        print(f"{j} * {i} = {z}")