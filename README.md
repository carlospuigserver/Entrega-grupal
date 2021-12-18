# Entrega-grupal

Ejercicio suma simple de una matriz:

La dirección GitHub de este repositorio es: https://github.com/carlospuigserver/Entrega-grupal.git

Para este código, ha sido fundamental ser capaces de crear una lista, y lo más importante, sumar los elementos de la lista y a partir de esta conseguir un número entero.

El código que hemos empleado para resolver el programa es el siguienta:
```
import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    suma=0
    for number  in ar:
        suma=suma+number
    return suma

n=int(input("Intrduzca una lista de dimension de la matriz: "))
print("Introduzca una lista de numeros", end="")
ar=list(map(int,input().rstrip().split()))
print(ar)
result=simpleArraySum(ar)
print("La suma vale", result)
