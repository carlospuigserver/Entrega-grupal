matriz=[
    [1,3,4],
    [3,2,4],
    [6,7,8]
]

suma_filas=[]
suma_columnas=[]

for f in matriz:
    suma_filas.append(sum(f))
    
print(suma_filas)


for j in range(len(matriz[0])):
    suma_columna=0

    for i in range(len(matriz)):
        suma_columna+=matriz[i][j]
        suma_columnas.append(suma_columna)
        
print(suma_columnas)