from TablaSimbolos.TS import TablaSimbolos
from objetosGenerales.Reader import Reader

class GestorTablaSimbolos():
    
    def __init__(self):
        
        self.currentTablaID = -1
        
        # crear el reader al fichero de salida de la Tabla de Símbolos
        self.writerFichero = Reader("../Ficheros Salida/tabla.txt")
        self.writerFichero.write("\n",True)  # sobreescribir la anterior compilacion
        
        # dictionary (hash table) para obtener la pos o id
        self.bloqueTS = {}
        self.listaTS = {}
        
        self.ultimaTS = False

    def crearTabla(self):
        ts = TablaSimbolos()
        self.listaTS.__setitem__(ts.getId(),ts)
        self.bloqueTS.__setitem__(ts.getId(),self.currentTablaID)
        self.currentTablaID = ts.getId()
        
    def getTablaActual(self):
        return self.listaTS.get(self.currentTablaID)
           
    def removeTable(self):
        # Escribir la tabla en el fichero
        self.writerFichero.write(self.getTablaActual().toString(),False)
        
        # Eliminar la tabla actual
        self.listaTS.__delitem__(self.currentTablaID)
        antID = self.currentTablaID
        
        # Obtener ID tabla anterior
        self.currentTablaID = self.bloqueTS.get(self.currentTablaID)
        
        # Eliminar del registro tabla actual
        self.bloqueTS.__delitem__(antID)
        
    def buscarEntradaPorID(self, entId):
        entrada = None
        
        tablaID = self.currentTablaID
        self.ultimaTS = self.listaTS.get(tablaID)
        
        entrada = self.ultimaTS.buscarEntradaID(entId)
        
        seguir = True
        # Buscar la entrada en todas las tablas disponibles
        while(entrada == None and seguir):
            tablaID = self.bloqueTS.get(tablaID)
            if (tablaID == None):
                seguir = False
            else:
                self.ultimaTS = self.listaTS(tablaID)
                
                if self.ultimaTS == None:
                    seguir = False
                else:
                    entrada = self.ultimaTS.buscarEntradaID(entId)
        
        return entrada
    
    def buscarEntradaPorLexema(self, lexema):
        entrada = None
        
        tablaID = self.currentTablaID
        self.ultimaTS = self.listaTS.get(tablaID)
        
        entrada = self.ultimaTS.buscarLugarTSNombre(lexema)
        
        seguir = True
        # Buscar la entrada en todas las tablas disponibles
        while((entrada == None and entrada == False) and seguir):
            tablaID = self.bloqueTS.get(tablaID)
            if (tablaID == None):
                seguir = False 
            else:
                self.ultimaTS = self.listaTS(tablaID)
                
                if self.ultimaTS == None:
                    seguir = False
                else:
                    entrada = self.ultimaTS.buscarLugarTSNombre(lexema)
        
        return entrada
    
    # buscar el lexema en la tabla actual 
    def buscarEntradaTablaActualLexema(self,lexema):
        entrada = self.buscarEntradaPorLexema(lexema)
        
        if entrada.getTabla() != self.currentTablaID:
            return False
        else:
            return entrada
    
    def insertarEntrada(self,lexema):
        tabla = self.listaTS.get(self.currentTablaID)
        
        return tabla.insertarValor(lexema,tabla.getID())
    
    def insertarEntradaTG(self,lexema):
        tabla= self.listaTS.get(1)
        
        return tabla.insertarValor(lexema,tabla.getID())
    
    def insertarTipoTamTS(self,entID, tipo, tamanho):
        entrada = self.buscarEntradaPorID(entID)
        
        if entrada != None and entrada != False:
            
            entrada.setTipo(tipo)
            
            if(tamanho != False):
                self.ultimaTS = self.listaTS(entrada.getTabla())
            
                entrada.setDespl(self.ultimaTS.getUltimoDespl())
                self.ultimaTS.setUltimoDespl(self.ultimaTS.getUltimoDespl() + tamanho)
    
    def insertarTipoParametros(self,entID, tipoLista):
        entrada = self.buscarEntradaPorID(entID)
        
        if entrada != None and entrada != False:
            for t in tipoLista:
                entrada.setTipoParametros(t)
    
    def insertarTipoDevuelto(self,entID, tipo):
        entrada = self.buscarEntradaPorID(entID)
        
        if entrada != None and entrada != False:
            entrada.setTipoDevuelto(tipo) 
                
    def buscarTipo(self,entID):
        tipo = False
        entrada = self.buscarEntradaPorID(entID)
        if entrada != None and entrada != False:
            tipo = entrada.getTipo()
        
        return tipo
    
    def buscarTipoParametros(self,entID):
        tipo = False
        entrada = self.buscarEntradaPorID(entID)
        if entrada != None and entrada != False:
            tipo = entrada.getTipoParametros()
        
        return tipo

    def buscarTipoDevuelto(self,entID):
        tipo = False
        entrada = self.buscarEntradaPorID(entID)
        if entrada != None and entrada != False:
            tipo = entrada.getTipoDevuelto()
        
        return tipo