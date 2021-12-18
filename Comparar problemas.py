from math import atan2
from random import randint

l1=randint(0,10)
l2=randint(0,10)
l3=randint(0,10)
c1=randint(0,10)
c2=randint(0,10)
c3=randint(0,10)

print("Los puntos de Lucía son:")
print("\nClaridad del problema={}".format(l1))
print("\nOriginalidad={}".format(l2))
print("\nDificultad={}".format(l3))

print("Los puntos de Carlos son:")
print("\nClaridad del problema={}".format(c1))
print("\nOriginalidad={}".format(c2))
print("\nDificultad={}".format(c3))

def compareTiplets ():
    puntosL=0
    puntosC=0

    if l1<c1:
        puntosC+=1
    elif l1>c1:
        puntosL+=1
    else:
        pass
    if l2<c2:
        puntosC+=1
    elif l2>c2:
        puntosL+=1
    else:
        pass
    if l3<c3:
        puntosC+=1
    elif l3>c3:
        puntosL+=1
    else:
        pass
    
    print("Los puntos totales de Lucía son:",l1+l2+l3)
    print("Los puntos totales de Carlos son:",c1+c2+c3)
    return
if l1+l2+l3>c1+c2+c3:
    print("Por tanto la ganadora es Lucía")
else:
    print("Por tanto el ganador es Carlos")




