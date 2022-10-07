from asyncio.windows_events import NULL
import re
import array

#------------------TABLA DE SIMBOLOS------------------
class EntradasTablaSimbolos():
    def __init__(self):
        pass
    def setValores(self,p,n,v):
        self.pos = p
        self.nombre = n
        self.valor = v

def buscarLugarTSNombre(n):
    for e in TablaSimbolos:
        if e.nombre == n:
            print("encontrado en posicion:", e.pos)
            return TablaSimbolos[e.pos].nombre

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
            try:
                lugar = buscarLugarTSNombre(lexema)
                token = Token(lexema, lugar)
                listaTokens.append(token)
            except:
                print("No se ha encontrado, se inserta en la pos:",len(TablaSimbolos) )
                entrada3 = EntradasTablaSimbolos()
                entrada3.setValores(len(TablaSimbolos),"z", "holaMundo")
                TablaSimbolos.append(entrada3)
                lugar = entrada3.pos

        
    if a == 5:
        valor = c 
    if a == 6:
        valor= valor + c
    if a == 7:
        if int(valor) > 32767:
            print("ERROR")
        else:
            
            token = Token("cteEntera", int(valor))
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
        elif c == 32:
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


    
#-----------LEER CARACTER-----------
pos=0
def leerCaracter (t,p):
    c = ord(t[p])
    global pos
    pos = pos+1
    return c







#------------------------DATOS------------------------

#-------TIPOS de caracteres que pueden entrar  
digitos = range(48,57+1) 
#32=espacio
palabrasReservadas = ["switch", "case", "default", "break", "let", "int", 
                    "boolean", "string", "if", "function", 
                    "input", "print", "return" "eof"]
c1 = list(range(33,42)) + list(range(43,126+1)) 
c2 = list(range(33,42)) + list(range(43,47)) + list(range(48,126+1))
c3 = list(range(33,34)) + list(range(35,126+1))

token = Token("coma","-")
#Programa a compilar
texto = input("CÓDIGO: ")
#Inicializar 
estadoInicial ="S"
print("Elemento posicion= ",pos)
caracterLeido = leerCaracter(texto,pos)

#Para los TOKENS
lexema =""
valor = ""
listaTokens = []

#Para la TS
TablaSimbolos=[]


#------------------BUCLE TRANSICIONES-------------------
transiccion = MatrizTransicciones(estadoInicial,caracterLeido)
for x in texto:
    print(caracterLeido,"=",x)
    estadoActual = transiccion[1]
    accionARealizar = transiccion[0]
    esFinal = transiccion[2]
    print("Accion a realizar: ", accionARealizar)
    accionesSemanticas(accionARealizar,caracterLeido)

    print(transiccion)    
    print("Posicion=",pos)
    print("LEXEMA=",lexema)
    print("VALOR=", valor)
    
    try:    
        caracterLeido = leerCaracter(texto,pos)
        transiccion = MatrizTransicciones(estadoActual,caracterLeido)
    except:
        print("FIN DE TEXTO")

#IMPIRMIR TS
for e in TablaSimbolos:
    print("Variable ",e.pos," = " ,e.nombre)
    print("estoy dentro")
for e in listaTokens:
    print("TOKEN",e.nombre, "VALOR= ", e.valor)
    print("estoy dentro")

