import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    suma=0
    for i in ar:
        suma=suma+i
        return suma
    print("La suma de todos los elementos de la matriz es:",suma)

def main():
    os.environ['OUTPUT_PATH']='Solución.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print("Escribe la dimensión de la matriz")
    ar_count = int(input().strip())
    print("Escribe los números separados por espacio")
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()

if __name__=='__main__':
    main()