import math
import os
import random
import re
import sys


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print("Escribe la dimanesión de la matriz")
    ar_count = int(input().strip())
    print("Escribe los números separados por espacios")
    ar = list(map(int, input().rstrip().split()))





def simpleArraySum(ar):
    suma=0
    for i in ar:
        suma=suma+i
        return suma 
    print("La suma de todos los elementos de la matriz es:",suma)



result = simpleArraySum(ar)
fptr.write(str(result) + '\n')


