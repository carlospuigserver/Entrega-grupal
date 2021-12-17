n=int(input("Escribe de cusntos pisos quieres que sea la escalera   "))
def staircase(dimension):
    for fila_actual in range(1,dimension+1):
        num_espacios= dimension-(fila_actual)
        # Imprime espacios iniciales
        for e in range(0,int(num_espacios)/2):
            print("",end="")

        # Imprime hastag
        for e in range(0, dimension-num_espacios):
            print("#",end="")

        # Pasar a la linea siguietne
        print()
    print()