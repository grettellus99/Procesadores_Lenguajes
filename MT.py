import re
import array


# TIPOS de caracteres que pueden entrar
letras = list(range(97,122+1)) + list(range(65,90+1))
digitos = range(0,9+1)
#32=espacio 
delimitadores = [32]
palabrasReservadas = ["switch", "case", "default", "break", "let", "int", 
                    "boolean", "string", "if", "function", 
                    "input", "print", "return" "eof"]
c1 = list(range(33,42)) + list(range(43,126+1)) 
c2 = list(range(33,42)) + list(range(43,47)) + list(range(48,126+1))
c3 = list(range(33,34)) + list(range(35,126+1))

for n in letras:
    print(chr(n))

for n in digitos:
    print(n)


# Funcion: saber si la palabra es reservada
def esreservada(palabra):
    esreservada= False
    for p in palabrasReservadas:
        if(p==palabra):
            esreservada = True
    
    return esreservada



# ***MATRIZ AFD***
lexema="" #Vaciarlo cuando se genere el token 
valor=0   # ""

def MatrizTransicciones(e,c):

    accion=0
    estadoSig=e
    estadoFinal = False

    #----------CASILLAS MATRIZ AFD---------
    # S
    if e =="S":
        if c in letras:
            accion = 2
            estadoSig = "A"
        if c in digitos:
            accion = 5
            estadoSig = "C"
        if c == 95:       #if c == _
            accion = 2
            estadoSig = "A"
        if c == 34:       #if c == ""
            accion = 9
            estadoSig = "K"
        if c == 47:       #if c == /
            accion = 8
            estadoSig = "E"  
        if c == 59:       #if c == ;
            accion = 24
            estadoSig = "W"
        if c == 44:       #if c == , 
            accion = 25
            estadoSig = "X"
        if c == 42:       #if c == *
            accion = 15
            estadoSig = "M"
        if c == 43:       #if c == +
            accion = 26
            estadoSig = "Y"
        if c == 38:       #if c == &
            accion = 18
            estadoSig = "P"
        if c == 40:       #if c == (
            accion = 20
            estadoSig = "R"
        if c == 41:       #if c == )
            accion = 21
            estadoSig = "T"
        if c == 123:       #if c == {
            accion = 22
            estadoSig = "U"
        if c == 125:       #if c == }
            accion = 23
            estadoSig = "V"
        if c == 61:       #if c ==   =
            accion = 12
            estadoSig = "H"
        if c in delimitadores:
            accion = 21 
            estadoSig = "S"
        else:
            print("El caracter", c," no es valido para el estado", e)
    # A
    if e =="A":
        if c in letras:
            accion = 3
            estadoSig = "A"
        if c in digitos:
            accion = 3
            estadoSig = "A"
        if c == 95:       #if c == _
            accion = 3
            estadoSig = "A"
        #OTHER CHARACTER CASO
            #accion = 4
            #estadoSig = "B"
        else:
            accion=4
            estadoSig = "B"
    # B
    if e =="B":
        estadoFinal= True
        #vaciar Lexema y valor
    

    # C
    if e =="C":
        if c == 95:       #if c == _
            accion = 6
            estadoSig = "C"
        else:
            accion = 7
            estadoSig = "D"

    # D
    if e =="D":
        estadoFinal = True

    # E
    if e =="E":
        if c == 42:       #if c == *
            accion = 8
            estadoSig = "F"
        else:
            print("El caracter", c," no es valido para el estado", e)

    # F
    if e =="F":
        if c in c1:       #if c ==  C1
            accion = 8
            estadoSig = "F"
        if c == 42:       #if c == *
            accion = 8
            estadoSig = "G"
        else:
            print("El caracter", c," no es valido para el estado", e)
        
    # G
    if e =="G":
        if c in c2:       #if c ==  C2
            accion = 8
            estadoSig = "F"
        if c == 47:       #if c == /
            accion = 8
            estadoSig = "S"
        if c == 42:       #if c == *
            accion = 8
            estadoSig = "G"
        else:
            print("El caracter", c," no es valido para el estado", e)

    # H
    if e =="H":
        
        if c == 41:       #if c ==   =
            accion = 13
            estadoSig = "I"
        else:
            accion= 14
            estadoSig = "J"

    # I
    if e =="I":
        estadoFinal = True
    
    # J
    if e =="J":
        estadoFinal = True

    # K
    if e =="K":
        if c in c3:       #if c ==  C3
            accion = 10
            estadoSig = "K"
        if c == 34:       #if c == ""
            accion = 11
            estadoSig = "L"
        else:
            print("El caracter", c," no es valido para el estado", e)

        
    # L
    if e =="L":
        estadoFinal = True


    # M
    if e =="M":

        if c == 41:       #if c ==   =
            accion = 16
            estadoSig = "N"
        else:
            accion = 17
            estadoSig = "O"
    
    
    # N
    if e =="N":
        estadoFinal = True

    # O
    if e =="O":
        estadoFinal = True
    
    # P
    if e =="P":
        if c == 38:       #if c == &
            accion = 19
            estadoSig = "Q"
        else:
            print("El caracter", c," no es valido para el estado", e)

    # Q
    if e =="Q":
        estadoFinal = True

    # R
    if e =="R":
        estadoFinal = True

    # T
    if e =="T":
        estadoFinal = True

    # U
    if e =="U":
        estadoFinal = True  

    # V
    if e =="V":
        estadoFinal = True

    # W
    if e =="W":
        estadoFinal = True

    # X
    if e =="X":
        estadoFinal = True

    # Y
    if e =="Y":
        estadoFinal = True
    
    #Z
    if e == "Z":
        estadoFinal = True


    
    return accion,estadoSig, estadoFinal


print("funciona")