def  gameOfStones ( n ): # 
    # Escribe tu código aquí 
    n  =  n % 7  if  n % 7  !=  0  else  7 
    if  n  ==  1 : 
        return  "Second" 
    elif  2 <= n <= 6 : 
        return  "First"  
    elif  n  ==  7  or  n  ==  8 : 
        return  "econd"