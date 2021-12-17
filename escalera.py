def staircase(dimension):
    for  fila_actual in range(1, dimension+1):
        num_espacios = dimension - (fila_actual)

        # Imprime espacios inicales
        for e in range(0, int((num_espacios)/2)):
            print(" ", end="")

        # Imprime hashtag
        for e in range(0, dimension-num_espacios):
            print("#", end="")

        # Pasar a la linea siguiente
        print()
        
    print()

def pedir_dimension():
    dimension = int(input("Insertar dimension: "))
    return dimension

dimension = pedir_dimension()
