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

    