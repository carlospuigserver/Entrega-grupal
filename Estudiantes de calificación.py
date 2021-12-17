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
    

if __name__ == '__main__':
    os.environ['OUTPUT_PATH']='Solution.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

 
 
 
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
