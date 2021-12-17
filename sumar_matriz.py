import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    suma=0
    for number  in ar:
        suma=suma+number
    return  suma

ar=list(map(int,input().rstrip().split()))
print(ar)
result=simpleArraySum(ar)
print("La suma vale", result)