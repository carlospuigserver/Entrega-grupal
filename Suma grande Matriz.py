import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    suma=0
    for number in ar:
        suma=suma+number
        return suma

n=int(input("Introduce una lista de las dimensiones de la matriz"))
print("Introduzca una lista de numeros", end="")
ar = list(map(int, input().rstrip().split()))
print(ar)
result=aVeryBigSum(ar)
print("La suma tiene un valor de",result)        