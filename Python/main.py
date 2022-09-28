import array



class Token:
    def __init__(self):
            self.nombre = "variable"
            self.valor = 0

def MatrizTransicciones(e,c):
    accion=0
    estadoSig=e
    if e =="S":
        if c == 104:
            accion = 1
            estadoSig = "A"
        if c == 97:
            accion = 2
            estadoSig = "B"
    if e =="A":
        if c == 111:
            accion = 3
            estadoSig = "C"
        if c == 97:
            accion = 4
            estadoSig = "Otra"

    return accion,estadoSig, "hola"


    
#LEER CARACTER
pos=0
def leerCaracter (t,p):
    c = ord(texto[p])
    global pos
    pos = pos+1
    return c




token = Token()
texto = input("CÓDIGO: ")
estadoInicial ="S"
print("Elemento posicion= ",pos)
caracterLeido = leerCaracter(texto,pos)

"""
transiccion = MatrizTransicciones(estadoInicial,caracterLeido)
estadoActual = transiccion[1]
accionARealizar = transiccion[0]
print(transiccion)
caracterLeido = leerCaracter(texto,pos)


transiccion = MatrizTransicciones(estadoActual,caracterLeido)
print(transiccion)
"""

#TRANSICIONES
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
        estadoActual = estadoInicial
        
    caracterLeido = leerCaracter(texto,pos)
    transiccion = MatrizTransicciones(estadoActual,caracterLeido)






print ("token: ", token.nombre)
print ("valor: ", token.valor)


