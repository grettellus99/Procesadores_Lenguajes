from asyncio.windows_events import NULL
import re
import array


#----------------------TOKENS-------------------------
class Token:
    def __init__(self,n,v):
            self.nombre = n
            self.valor = v

#-----------------ACCIONES SEMANTICAS--------------------
def accionesSemanticas (a,ctr):
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
        #POR HACER
        if lexema in palabrasReservadas:
            token = Token(lexema, "-")
            listaTokens.append(token)
        else:
           #pos = buscarLugarTS()
            if pos >= 0:
                token = Token(lexema, pos)
                listaTokens.append(token)
            else:
               #pos = insertarTS()
                token = Token(lexema, pos)
                listaTokens.append(token)

    if a == 5:
        valor = c 
    if a == 6:
        valor= valor *10 + c
    if a == 7:
        if valor > 32767:
            print("ERROR")
        else:
            
            token = Token("cteEntera", valor)
            listaTokens.append(token)

    if a == 8:
        print("leer")
    if a == 9:
        lexema= "" 
    if a == 10:
        lexema= lexema + c
    if a == 11:
        if len(lexema) > 64:
            print("ERROR")
        else:
            token = Token("cadena", lexema)
            listaTokens.append(token)
    if a == 12:
        print("leer")
    if a == 13:
        token = Token("asignacion", "-")
        listaTokens.append(token)
    if a == 14:
        token = Token("opRelacional", 1)
        listaTokens.append(token)
    if a == 15:
        print("leer")
    if a == 16:
        token = Token("asigMultiplicacion", "-")
        listaTokens.append(token)
    if a == 17:
        token = Token("opAritmetico",1)
        listaTokens.append(token)
    if a == 18:
        print("leer")
    if a == 19:
        token = Token("opLogico",1)
        listaTokens.append(token)
    
    if a == 20:
        token = Token("abrirParantesis","-")
        listaTokens.append(token)
        
    if a == 21:
        token = Token("cerrarParantesis","-")
        listaTokens.append(token)
    if a == 22:
        token = Token("abrirCorchete","-")
        listaTokens.append(token)
    if a == 23:
        token = Token("cerrarCorchete","-")
        listaTokens.append(token)
    if a == 24:
        token = Token("ptoComa","-")
        listaTokens.append(token)
    if a == 25:
        token = Token("coma","-")
        listaTokens.append(token)
    if a == 26:
        token = Token("opAritmetico",2)
        listaTokens.append(token)



#----------Funcion: saber si la palabra es reservada-------
def esreservada(palabra):
    esreservada= False
    for p in palabrasReservadas:
        if(p==palabra):
            esreservada = True
    
    return esreservada




#-----------TRANSICIONES-----------
def MatrizTransicciones(e,cct):
    accion=0
    estadoSig=""
    estadoFinal = False
    c=cct

    
    letras = list(range(65,90+1)) + list(range(97,122+1))
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
            accion = 27
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
        elif c in delimitadores:
            accion = 21 
            estadoSig = "S"
        elif c == 58:
            accion = 26
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
            accion=4
            estadoSig = "B"
    # B
    if e =="B":
        estadoFinal = True
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
    
    # J
    if e =="J":
        estadoFinal = True

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


    
#-----------LEER CARACTER-----------
pos=0
def leerCaracter (t,p):
    c = ord(t[p])
    global pos
    pos = pos+1
    return c







#------------------------DATOS------------------------

#-------TIPOS de caracteres que pueden entrar  
digitos = range(0,9+1)
#32=espacio 
delimitadores = [32]
palabrasReservadas = ["switch", "case", "default", "break", "let", "int", 
                    "boolean", "string", "if", "function", 
                    "input", "print", "return" "eof"]
c1 = list(range(33,42)) + list(range(43,126+1)) 
c2 = list(range(33,42)) + list(range(43,47)) + list(range(48,126+1))
c3 = list(range(33,34)) + list(range(35,126+1))

token = Token()
#Programa a compilar
texto = input("CÓDIGO: ")
#Inicializar 
estadoInicial ="S"
print("Elemento posicion= ",pos)
caracterLeido = leerCaracter(texto,pos)

#Para los TOKENS
lexema =""
valor = 0
listaTokens = []


#------------------BUCLE TRANSICIONES-------------------
transiccion = MatrizTransicciones(estadoInicial,caracterLeido)
for x in texto:
    print(caracterLeido)
    estadoActual = transiccion[1]
    accionARealizar = transiccion[0]
    esFinal = transiccion[2]
    print(transiccion)    
    print("Posicion=",pos)

    #Si es estado final, volvemos a S
    if esFinal:
        estadoActual = "S"
        
    caracterLeido = leerCaracter(texto,pos)
    transiccion = MatrizTransicciones(estadoActual,caracterLeido)




