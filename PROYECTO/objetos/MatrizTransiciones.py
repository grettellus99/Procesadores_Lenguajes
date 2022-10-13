from objetos.datos import *
from objetos.GestorError import Error

def matrizTransiciones(e,cct):
    accion=0
    estadoSig=""
    estadoFinal = False
    c=cct
    error=False
    
    #CASILLAS MATRIZ AFD:
    # S
    if e =="S":
        if c in letras:
            accion = 2
            estadoSig = "A"
        elif c in digitos:
            accion = 5
            estadoSig = "C"
        elif c == 95:       #if c == _
            accion = 2
            estadoSig = "A"
        elif c == 34:       #if c == "
            accion = 15
            estadoSig = "K"
        elif c == 47:       #if c == /
            accion = 8
            estadoSig = "E"  
        elif c == 59:       #if c == ;
            accion = 30
            estadoSig = "W"
        elif c == 44:       #if c == , 
            accion = 31
            estadoSig = "X"
        elif c == 42:       #if c == *
            accion = 15
            estadoSig = "M"
        elif c == 43:       #if c == +
            accion = 33
            estadoSig = "Z"
        elif c == 38:       #if c == &
            accion = 24
            estadoSig = "P"
        elif c == 40:       #if c == (
            accion = 26
            estadoSig = "R"
        elif c == 41:       #if c == )
            accion = 27
            estadoSig = "T"
        elif c == 123:       #if c == {
            accion = 28
            estadoSig = "U"
        elif c == 125:       #if c == }
            accion = 29
            estadoSig = "V"
        elif c == 61:       #if c ==   =
            accion = 18
            estadoSig = "H"
        elif c == 32 or c == 10 or c == 13 or c == 11:       #if c == del (espacio en blanco, salto de linea, retorno de carro o tab)
            accion = 1 
            estadoSig = "S"
        elif c == 58:       #if c == :
            accion = 32
            estadoSig= "Y"
        else:
            mensaje= f"El carácter {c} no es válido para el estado {e}"
            print(mensaje)
            error=Error("", mensaje ,"")
    # A
    elif e =="A":
        if c in letras:
            accion = 3
            estadoSig = "A"
        elif c in digitos:
            accion = 3
            estadoSig = "A"
        elif c == 95:       #if c == _
            accion = 3
            estadoSig = "A"
        #OTHER CHARACTER CASO
            #accion = 4
            #estadoSig = "B"
        else:
            estadoSig = "B"
            accion = 4
    # B ( ESTADO FINAL ) 
    elif e =="B":
        accion=0
        estadoFinal = True
        estadoSig = "S"
        #vaciar Lexema y valor
    
    # C
    elif e =="C":
        if c in digitos:       #if c == digitos
            accion = 6
            estadoSig = "C"
        else:
            accion = 7
            estadoSig = "D"

    # D ( ESTADO FINAL ) 
    elif e =="D":
        accion = 0
        estadoFinal = True
        estadoSig = "S"

    # E
    elif e =="E":
        if c == 42:       #if c == *
            accion = 9
            estadoSig = "F"
        else:
            mensaje= f"El carácter {c} no es válido para el estado {e}"
            print(mensaje)
            error=Error("", mensaje ,"")
    # F
    elif e =="F":
        if c in c1:       #if c ==  C1
            accion = 10
            estadoSig = "F"
        elif c == 42:       #if c == *
            accion = 11
            estadoSig = "G"
        else:
            mensaje= f"El carácter {c} no es válido para el estado {e}"
            print(mensaje)
            error=Error("", mensaje ,"")
        
    # G
    elif e =="G":
        if c in c2:       #if c ==  C2
            accion = 12
            estadoSig = "F"
        elif c == 47:       #if c == /
            accion = 14
            estadoSig = "S"
        elif c == 42:       #if c == *
            accion = 13
            estadoSig = "G"
        else:
            mensaje= f"El carácter {c} no es válido para el estado {e}"
            print(mensaje)
            error=Error("", mensaje ,"")

    # H
    elif e =="H":
        
        if c == 41:       #if c ==   =
            accion = 19
            estadoSig = "I"
        else:
            accion= 20
            estadoSig = "J"

    # I ( ESTADO FINAL ) 
    elif e =="I":
        accion=0
        estadoFinal = True
        estadoSig = "S"
    
    # J  ( ESTADO FINAL ) 
    elif e =="J":
        accion=0
        estadoFinal = True
        estadoSig = "S"

    # K 
    elif e =="K":
        if c in c3:       #if c ==  C3
            accion = 16
            estadoSig = "K"
        elif c == 34:       #if c == ""
            accion = 17
            estadoSig = "L"
        else:
            mensaje= f"El carácter {c} no es válido para el estado {e}"
            print(mensaje)
            error=Error("", mensaje ,"")

        
    # L  ( ESTADO FINAL ) 
    elif e =="L":
        accion=0
        estadoFinal = True
        estadoSig = "S"


    # M
    elif e =="M":

        if c == 41:       #if c ==   =
            accion = 22
            estadoSig = "N"
        else:
            accion = 23
            estadoSig = "O"
    
    
    # N ( ESTADO FINAL )
    elif e =="N":
        accion=0
        estadoFinal = True
        estadoSig = "S"

    # O
    elif e =="O":
        accion=0
        estadoFinal = True
        estadoSig = "S"
    
    # P
    elif e =="P":
        if c == 38:       #if c == &
            accion = 25
            estadoSig = "Q"
        else:
            mensaje= f"El carácter {c} no es válido para el estado {e}"
            print(mensaje)
            error=Error("", mensaje ,"")

    # Q ( ESTADO FINAL )
    elif e =="Q":
        accion=0
        estadoFinal = True
        estadoSig = "S"

    # R ( ESTADO FINAL )
    elif e =="R":
        accion=0
        estadoFinal = True
        estadoSig = "S"

    # T ( ESTADO FINAL )
    elif e =="T":
        accion=0
        estadoFinal = True
        estadoSig = "S"

    # U ( ESTADO FINAL )
    elif e =="U":
        accion=0
        estadoFinal = True
        estadoSig = "S"

    # V ( ESTADO FINAL )
    elif e =="V":
        accion=0
        estadoFinal = True
        estadoSig = "S"

    # W ( ESTADO FINAL )
    elif e =="W":
        accion=0
        estadoFinal = True
        estadoSig = "S"

    # X ( ESTADO FINAL )
    elif e =="X":
        accion=0
        estadoFinal = True
        estadoSig = "S"

    # Y ( ESTADO FINAL )
    elif e =="Y":
        accion=0
        estadoFinal = True
        estadoSig = "S"
    
    #Z ( ESTADO FINAL )
    elif e == "Z":
        accion=0
        estadoFinal = True
        estadoSig = "S"


    
    return accion, estadoSig, estadoFinal, error
