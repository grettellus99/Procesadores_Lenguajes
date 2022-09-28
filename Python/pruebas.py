from ast import List
import re
import array

"""
letras = list(range(97,122+1)) + list(range(65,90+1))

for n in letras:
    print(chr(n))

digitos = range(0,9+1)

for n in digitos:
    print(n)


barrabaja = 95
asterisco = 42
mas = 43
palabrasReservadas = ["switch", "case", "default", "break", "let", "int", 
                    "boolean", "string", "if", "function", 
                    "input", "print", "return" "eof"]
def esreservada(palabra):
    esreservada= False
    for p in palabrasReservadas:
        if(p==palabra):
            esreservada = True
    
    return esreservada
"""
c1 = list(range(33,42)) + list(range(43,126+1)) + list(range(130,131))
c2 = list(range(33,42)) + list(range(43,47)) + list(range(48,126+1))
c3 = list(range(33,34)) + list(range(35,126+1))



c= 131

if c in c1:
    print("bien")
else:
    print("mal")

print("xao")




