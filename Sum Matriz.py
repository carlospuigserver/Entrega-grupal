import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    suma=0
    l=len(ar)
    for i in range(l):
        suma=suma+i
        return suma 
    print("La suma de todos los elementos de la matriz es:",suma)

              
        

def main():
    os.environ['OUTPUT_PATH']='Solucion.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print("Escribe la dimanesión de la matriz")
    ar_count= int(input().strip())
    print("Escribe los números separados por espacios")
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()

