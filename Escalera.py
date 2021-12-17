###
#FUNCIONES
###
def staircase(dimension):
    for fila_actual in range(1,dimension+1):
        num_espacios= dimension-(fila_actual)
        # Imprime espacios iniciales
        for e in range(0,int((num_espacios)/2)):
            print(" ",end="")

        # Imprime hastag
        for e in range(0, dimension-num_espacios):
            print("#",end="")


        # Pasar a la linea siguietne
        print()

    print()

def pedir_dimension():
    dimension=int(input("Insertar dimension: "))
    return dimension

###
#INICIO PROGRAMA
###
dimension=pedir_dimension()

if dimension>0:
    staircase(dimension)
else:
    print("Introduzca un numero valido: ")
