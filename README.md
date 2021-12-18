# Entrega-grupal

Ejercicio "Suma simple de una matriz":

La dirección GitHub de este repositorio es: https://github.com/carlospuigserver/Entrega-grupal.git

Para este código, ha sido fundamental ser capaces de crear una lista, y lo más importante, sumar sus elementos y a partir de esta operación conseguir un número entero.

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
```





Ejercicio "Compara los problemas":

La dirección GitHub de este repositorio es : https://github.com/carlospuigserver/Entrega-grupal.git

Para realizar este código, hemos creado unos ciertos apartados los cuales tienen una calificación aleatoria(0-10) para dos personas, y a partir de los if, hemos sido capaces de ir comparando las notas de los diferentes apartados de ambos, y finalmente declarar quien ha conseguido más puntos.

El código que hemos empleado para llevar a cabo este programa es el siguiente:
```
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
```



Ejercicio "Una suma muy grande":

La dirección GitHub de este repositorio es: https: https://github.com/carlospuigserver/Entrega-grupal.git

Para realizar este código, hemos empleado la misma estructura que en el primer ejercico, la clave ha sido crear una lista, y haber sido capaces de realizar una suma de los elementos de esta y que nos devuelva un número entero, pero en este ejercicio, a diferencia del primero, hay que tener en cuenta que algunos de los elementos de la lista pueden ser números muy grandes.

El código que hemos llevado a cabo para realizar el programa es el siguiente:

```import math
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
```



Ejercicio "La Escalera":

La dirección GitHub de este repositorio es: https://github.com/carlospuigserver/Entrega-grupal.git

Para llevar a cabo este programa, hemos tenido que crear una escalera de un cierto tamaño(número entero), dibujada con símbolos y espacios, y la altura y la base de esta tiene que ser igual al tamaño que hayamos seleccionado. Para realizarla nos hemos guiado de dos bucles for, uno que tenga en cuenta las dimensiones de la escalera, y otro que tenga en cuenta los espacios.


El código que hemos empleado para realizar el programa es el siguiente:

```
def staircase(dimension):
    for  fila_actual in range(1, dimension+1):
        num_espacios = dimension - (fila_actual)

        # Imprime espacios inicales
        for e in range(0, int((num_espacios)/2)):
            print(" ", end="")

        # Imprime hashtag
        for e in range(0, dimension-num_espacios):
            print("#", end="")

        # Pasar a la linea siguiente
        print()


    print()


def pedir_dimension():
```



Ejercicio "Juego de piedras":

La dirección GitHub de este repositorio es: https://github.com/carlospuigserver/Entrega-grupal.git

Para la realización de este código ha sido fundamental la realizacion de un bucle. Cada jugador juega con un numero inicial de piedras, juegan de manera alterna 
y hay unas reglas especificas.

Código:

```
for i in range(0,int(input())):
    stones=int(input())
    if stones%7<2:
        print("Second") 
    else:
        print("First")   
        
 ```

Ejercicio "Estudiantes de calificacion":

La dirección GitHub de este repositorio es: https://github.com/carlospuigserver/Entrega-grupal.git

Hemos realizado un programa para redondear las notas de la universidad, es clave entender que para poder redondearlo hay que llegar al número base(es el múltiplo de cinco más cercano pero MENOR) y a partir de ahí o se le añadirá el múltiplo de cinco más cercano pero MAYOR,el valor que se añadirá a la lista de resultados es el numero_base + 5 o se añadirá el numero base.  No todos los numeros se redondean, solo los mayores de 40 que estaran suspendidos.


Código:
```
import math
import os
import random
import re
import sys

def gradingStudents(grades):
    results=[]
    for nota in grades:
        if nota<40:
            print(nota)
            results.append(nota)
        else:
            resto= nota%5
            num_base=nota-resto
            if (nota%5)>=3:
                num_redondeado=num_base+5
                results.append(num_redondeado)
            else:
                results.append(num_base)
                
    return results
    


   

grades_count = int(input("Numero de estudiantes? ").strip())
grades = []

 
 
 
for _ in range(grades_count):
    grades_item = int(input("Nota ").strip())
    grades.append(grades_item)

print(grades)
print()

result = gradingStudents(grades)
print(result)

```
      

Ejercicio "Manzana y naranja":

La dirección GitHub de este repositorio es: https://github.com/carlospuigserver/Entrega-grupal.git

El ejercicio consiste en determinar las manzanas y naranjas que caen en la casa de Sam, mediante el espacio que ocupa la casa y las distancias d.

Código:

```
import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    totalapples=totaloranges=0
    for i in range(len(apples)):
        if s<= a+apples[i]<=t:
            totalapples+=1
    for i in range(len(oranges)):
        if s<= b+oranges[i]<=t:
            totaloranges+=1 
    print("En total han caído",str(totalapples),"manzanas")
    print("En total han caído",str(totaloranges),"naranjas")    


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
    
   
