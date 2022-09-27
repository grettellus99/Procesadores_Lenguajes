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

    return accion,estadoSig


    

pos=0
def leerCaracter (t,p):
    c = ord(texto[p])
    return c



token = Token()
texto = input("CÓDIGO: ")
estadoInicial ="S"
caracterLeido = leerCaracter(texto,pos)

transiccion = MatrizTransicciones(estadoInicial,caracterLeido)

print(transiccion)
print(chr(232))
print(chr(138))



print ("token: ", token.nombre)
print ("valor: ", token.valor)


