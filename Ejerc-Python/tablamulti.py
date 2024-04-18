

num=int(input("Ingresa el numero del que deseas saber su tabla \n"))


def tablamul(num):
    print(f"#####TABLA DE MULTIPLICAR {num} #####")

    for i in range(0,11):
        
        resultado=num * i

        print(f"{num} * {i} = {resultado} \n")


tablamul(num)