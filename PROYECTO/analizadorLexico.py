from objetos.token import *
from objetos.transicciones import matrizTransicciones

print(matrizTransicciones("S",104))

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

#-------TIPOS de caracteres que pueden entrar
letras = list(range(65,90+1)) + list(range(97,122+1))

digitos = range(48,57+1) 
#32=espacio
palabrasReservadas = ["switch", "case", "default", "break", "let", "int", 
                    "boolean", "string", "if", "function", 
                    "input", "print", "return" "eof"]
c1 = list(range(33,42)) + list(range(43,255+1))
c2 = list(range(33,42)) + list(range(43,47)) + list(range(48,255+1))
c3 = list(range(33,34)) + list(range(35,255+1))

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

