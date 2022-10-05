from ast import List
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

TablaSimbolos=[] 

entrada = EntradasTablaSimbolos()
entrada.setValores(0,"x",9)
TablaSimbolos.append(entrada)

entrada2 = EntradasTablaSimbolos()
entrada2.setValores(1,"y",5)
TablaSimbolos.append(entrada2)

print(TablaSimbolos[0].pos)
print(TablaSimbolos[1].nombre)

entrada4 = EntradasTablaSimbolos()
entrada4.setValores(len(TablaSimbolos),"j",99)
TablaSimbolos.append(entrada4)


try:
    lugar = buscarLugarTS(5)
    print(lugar)
except:
    print("No se ha encontrado, se inserta en la pos:",len(TablaSimbolos) )
    entrada3 = EntradasTablaSimbolos()
    entrada3.setValores(len(TablaSimbolos),"z", "holaMundo")
    TablaSimbolos.append(entrada3)

for e in TablaSimbolos:
    print("Variable ",e.pos," = " ,e.nombre) 