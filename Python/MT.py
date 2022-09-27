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

    #----------CASILLAS MATRIZ AFD---------
    # S
    if e =="S":
        if c in letras:
            accion = 2
            estadoSig = "A"
        if c in digitos:
            accion = 5
            estadoSig = "C"
        if c == 95:
            accion = 6
            estadoSig = "C"
        if c == 34:
            accion = 9
            estadoSig = "K"
        if c == 47:
            accion = 8
            estadoSig = "E"  #-->--->---->POR AQUI<-----<----<--
    

    # A
    if e =="A":
        if c == 111:
            accion = 3
            estadoSig = "C"
        if c == 97:
            accion = 4
            estadoSig = "Otra"

    # B
    # C
    # D
    # E
    # F
    # G
    # H
    # I
    # J
    # K
    # L
    # M
    # N
    # O
    # P
    # Q
    # R
    # T
    # U
    # V
    # W
    # X
    # Y



    
    return accion,estadoSig, "hola"


print("funciona")