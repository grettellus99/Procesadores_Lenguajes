from objetos.Token import *
from objetos.transiciones import matrizTransiciones
from objetos.acciones import *
from objetos.Reader import *
from objetos.datos import *

print(matrizTransiciones("S",104))

def buscarLugarTSNombre(n):
    for e in TablaSimbolos:
        if e.nombre == n:
            print("encontrado en posición:", e.pos)
            return TablaSimbolos[e.pos].nombre
def esreservada(palabra):
    esreservada= False
    for p in palabrasReservadas:
        if(p==palabra):
            esreservada = True
    
    return esreservada
pos=0
def leerCaracter (t,p):
    c = ord(t[p])
    global pos
    pos = pos+1
    return c
#------------------------DATOS------------------------

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
transicion = matrizTransiciones(estadoInicial,caracterLeido)
for x in texto:
    print(caracterLeido,"=",x)
    estadoActual = transicion[1]
    accionARealizar = transicion[0]
    esFinal = transicion[2]
    print("Accion a realizar: ", accionARealizar)
    accionesSemanticas(accionARealizar,caracterLeido)

    print(transicion)    
    print("Posicion=",pos)
    print("LEXEMA=",lexema)
    print("VALOR=", valor)
    
    try:    
        caracterLeido = leerCaracter(texto,pos)
        transicion = matrizTransiciones(estadoActual,caracterLeido)
    except:
        print("FIN DE TEXTO")

#IMPIRMIR TS
for e in TablaSimbolos:
    print("Variable ",e.pos," = " ,e.nombre)
    print("estoy dentro")
for e in listaTokens:
    print("TOKEN",e.nombre, "VALOR= ", e.valor)
    print("estoy dentro")

