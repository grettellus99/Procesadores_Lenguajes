from ast import List
from asyncio.windows_events import NULL
import re
import array

class EntradasTablaSimbolos():
    def __init__(self):
        pass
    def setValores(self,p,n,v):
        self.pos = p
        self.nombre = n
        self.valor = v

def buscarLugarTS(ps):
    return TablaSimbolos[ps].nombre
def buscarLugarTSNombre(n):
    for e in TablaSimbolos:
        if e.nombre == n:
            print("encontrado en posicion:", e.pos)
            return TablaSimbolos[e.pos].nombre

TablaSimbolos=[] 

entrada = EntradasTablaSimbolos()
entrada.setValores(0,"x",9)
TablaSimbolos.append(entrada)

try:
    lugar = buscarLugarTS(5)
    print(lugar)
except:
    print("No se ha encontrado, se inserta en la pos:",len(TablaSimbolos) )
    entrada3 = EntradasTablaSimbolos()
    entrada3.setValores(len(TablaSimbolos),"z", "holaMundo")
    TablaSimbolos.append(entrada3)
    lugar = entrada3.pos

for e in TablaSimbolos:
    print("Variable ",e.pos," = " ,e.nombre) 

posInTs=buscarLugarTSNombre("j")
print(posInTs)