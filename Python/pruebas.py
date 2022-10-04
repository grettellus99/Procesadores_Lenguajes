from ast import List
import re
import array

""" pruebas valores caraceteres
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
"""

#---------CLASE TOKENS----------
class Token():
    def __init__(self, parte1, parte2):
            self.p1 = parte1
            self.p2 = parte2


#-------Acciones semanticas:---------

listaTokens = []

def accionSemantica(a,ctr):

    global lexema
    global valor
    global listaTokens

    c=chr(ctr)

    if a == 0:
        print("Accion no valida") 
    if a == 1:
        print("leer")
    if a == 2:
        lexema= c
    if a == 3:     
        lexema= lexema + c
    if a == 4:
        lexema= c #POR HACER
    if a == 5:
        valor = c 
    if a == 6:
        valor= valor *10 + c
    if a == 7:
        if valor > 1000:
            print("ERROR")
        else:
            print("genTOKEN  <cteEntera,valor>" )# <----------POR AQUI!!!!!!!!!
             #POR probar

            token = Token("hola", 3)

            listaTokens.append(token)

    if a == 8:
        print("leer")
    if a == 9:
        lexema= "" 
    if a == 10:
        lexema= lexema + c
    if a == 11:
        if lexema.length() > 64:
            print("ERROR")
        else:
            print("genTOKEN  <cadena,lexema>")
    if a == 12:
        print("leer")
    if a == 13:
        print("genTOKEN  <asig,->")
    if a == 14:
        print("genTOKEN  <opRelacional,1>")
    if a == 15:
        print("leer")
    if a == 16:
        print("genTOKEN  <asigMult,->")
    if a == 17:
        print("genTOKEN  <opAritmetico,1>")
    if a == 18:
        print("leer")
    if a == 19:
        print("genTOKEN  <opLogico,1>")
    if a == 20:
        print("genTOKEN  <abrirParantesis,->")
    if a == 21:
        print("genTOKEN  <cerrarParantesis,->")
    if a == 22:
        print("genTOKEN  <abrirCorchete,->")
    if a == 23:
        print("genTOKEN  <cerrarCorchete,->")
    if a == 24:
        print("genTOKEN  <ptoComa,->")
    if a == 25:
        print("genTOKEN  <coma,->")
    if a == 26:
        print("genTOKEN  <opAritmetico,2>")



lexema = ""
valor = 0

nacc=2
caracter = 104

print("LEXEMA:",lexema)
accionSemantica(nacc,caracter)

nacc=3
caracter= 105
print("LEXEMA:",lexema)
accionSemantica(nacc,caracter)
print("LEXEMA:",lexema)

tokenPrueba = Token("hola","-")
listaTokens.append(tokenPrueba)

print(listaTokens[0].p1)
print(listaTokens[0].p2)

