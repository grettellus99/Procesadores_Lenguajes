letras = list(range(65,90+1)) + list(range(97,122+1))

digitos = range(48,57+1) 
#32=espacio
palabrasReservadas = ["switch", "case", "default", "break", "let", "int", 
                    "boolean", "string", "if", "function", 
                    "input", "print", "return" "eof"]
c1 = list(range(33,42)) + list(range(43,255+1))
c2 = list(range(33,42)) + list(range(43,47)) + list(range(48,255+1))
c3 = list(range(33,34)) + list(range(35,255+1))

def matrizTransicciones(e,cct):
    accion=0
    estadoSig=""
    estadoFinal = False
    c=cct

    
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
        elif c == 34:       #if c == ""
            accion = 9
            estadoSig = "K"
        elif c == 47:       #if c == /
            accion = 8
            estadoSig = "E"  
        elif c == 59:       #if c == ;
            accion = 24
            estadoSig = "W"
        elif c == 44:       #if c == , 
            accion = 25
            estadoSig = "X"
        elif c == 42:       #if c == *
            accion = 15
            estadoSig = "M"
        elif c == 43:       #if c == +
            accion = 26
            estadoSig = "Z"
        elif c == 38:       #if c == &
            accion = 18
            estadoSig = "P"
        elif c == 40:       #if c == (
            accion = 20
            estadoSig = "R"
        elif c == 41:       #if c == )
            accion = 21
            estadoSig = "T"
        elif c == 123:       #if c == {
            accion = 22
            estadoSig = "U"
        elif c == 125:       #if c == }
            accion = 23
            estadoSig = "V"
        elif c == 61:       #if c ==   =
            accion = 12
            estadoSig = "H"
        elif c == 32:       #if c == espacio en blanco
            accion = 21 
            estadoSig = "S"
        elif c == 58:       #if c == :
            accion = 27
            estadoSig= "Y"
        else:
            print("El caracter", c," no es valido para el estado", e)
    # A
    if e =="A":
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
    # B
    if e =="B":
        accion=1
        estadoFinal = True
        estadoSig = "S"
        #vaciar Lexema y valor
    

    # C
    if e =="C":
        if c in digitos:       #if c == digitos
            accion = 6
            estadoSig = "C"
        else:
            accion = 7
            estadoSig = "D"

    # D
    if e =="D":

        accion = 1
        estadoFinal = True
        estadoSig = "S"

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
        elif c == 42:       #if c == *
            accion = 8
            estadoSig = "G"
        else:
            print("El caracter", c," no es valido para el estado", e)
        
    # G
    if e =="G":
        if c in c2:       #if c ==  C2
            accion = 8
            estadoSig = "F"
        elif c == 47:       #if c == /
            accion = 8
            estadoSig = "S"
        elif c == 42:       #if c == *
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
        estadoSig = "S"
    
    # J
    if e =="J":
        estadoFinal = True
        estadoSig = "S"

    # K
    if e =="K":
        if c in c3:       #if c ==  C3
            accion = 10
            estadoSig = "K"
        elif c == 34:       #if c == ""
            accion = 11
            estadoSig = "L"
        else:
            print("El caracter", c," no es valido para el estado", e)

        
    # L
    if e =="L":
        estadoFinal = True
        estadoSig = "S"


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
        estadoSig = "S"

    # O
    if e =="O":
        estadoFinal = True
        estadoSig = "S"
    
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
        estadoSig = "S"

    # R
    if e =="R":
        estadoFinal = True
        estadoSig = "S"

    # T
    if e =="T":
        estadoFinal = True
        estadoSig = "S"

    # U
    if e =="U":
        estadoFinal = True
        estadoSig = "S"

    # V
    if e =="V":
        estadoFinal = True
        estadoSig = "S"

    # W
    if e =="W":
        estadoFinal = True
        estadoSig = "S"

    # X
    if e =="X":
        estadoFinal = True
        estadoSig = "S"

    # Y
    if e =="Y":
        estadoFinal = True
        estadoSig = "S"
    
    #Z
    if e == "Z":
        estadoFinal = True
        estadoSig = "S"


    
    return accion,estadoSig, estadoFinal
