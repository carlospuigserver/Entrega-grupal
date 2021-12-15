# Suma matrices

a=[
8,3,4,
6,9,5,
3,4,3
]

b=[
1,3,5,
6,6,2,
3,2,9,
]


def suma(matriz1,matriz2):
    l=len(matriz1)
    s=len(matriz2)
    if l==s and len(matriz1[0])==len(matriz2[0]):
        matriz3=[]
        for i in range(matriz1):
            matriz3.append([])
        for j in range(matriz1[0]):
            matriz3.append(matriz1[i][j]+matriz2[i][j])
        
        
