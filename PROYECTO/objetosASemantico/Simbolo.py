from objetosASintac.datos import noTerminales


# Clase Atributo para definir la estructura de un atributo de un simbolo
class Atributo():
    def __init__(self,nombre,valor):
        self.nombreAtributo = nombre
        self.valorAtributo = valor

# Clase simbolo para representar los No Terminales con sus atributos
class Simbolo():
    def __init__(self,nombre):
        self.nombreSimbolo = nombre
        
        self.listaAtributos = []
        
    def addAtributo(self,n,v):
        atributo = Atributo(n,v)
        self.listaAtributos.append(atributo)
        
    def setValorAtributo(self,n,v):
        for atributo in self.listaAtributos:
            if atributo.nombreAtributo == n:
                atributo.valorAtributo = v
                return True       
        # si no encontro el atributo en la lista, lo añade con su valor v
        self.addAtributo(n,v)
        return True
    
    # Metodo para obtener el valor del atributo de nombre n del simbolo
    def getValorAtributo(self,n):
        for atributo in self.listaAtributos:
            if atributo.nombreAtributo == n:
                return atributo.valorAtributo   # devolver el valor del atributo
        return None # devolver None porque no se encontro el atributo
    