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
        
        self.noCrear = False
        
        self.ultimaTS = False

    # crear una tabla
    def crearTabla(self):
        
        if self.noCrear == False:
            ts = TablaSimbolos()
            self.listaTS.__setitem__(ts.getId(),ts)
            self.bloqueTS.__setitem__(ts.getId(),self.currentTablaID)
            self.currentTablaID = ts.getId()
        else:
            self.noCrear = False
        
    # devuelve la tabla actual
    def getTablaActual(self):
        return self.listaTS.get(self.currentTablaID)
      
    # elimina la tabla actual y cambia la tabla actual a la anterior      
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
    
    # busca la entrada en las tablas activas por id    
    def buscarEntradaPorID(self, entId):
        entrada = None
        
        tablaID = self.currentTablaID
        self.ultimaTS = self.listaTS.get(tablaID)
        
        entrada = self.ultimaTS.buscarEntradaID(int(entId))
        
        seguir = True
        # Buscar la entrada en todas las tablas disponibles
        while(entrada == None and seguir):
            tablaID = self.bloqueTS.get(tablaID)
            if (tablaID == -1):
                seguir = False
            else:
                self.ultimaTS = self.listaTS.get(tablaID)
                
                if self.ultimaTS == None:
                    seguir = False
                else:
                    entrada = self.ultimaTS.buscarEntradaID(int(entId))
        
        return entrada
    
    # busca la entrada en las tablas activas por lexema 
    def buscarEntradaPorLexema(self, lexema):
        entrada = None
        
        tablaID = self.currentTablaID
        
        if tablaID == -1:
            self.crearTabla()
            self.noCrear = True
            tablaID = self.currentTablaID
        
        self.ultimaTS = self.listaTS.get(tablaID)
        
        entrada = self.ultimaTS.buscarTSNombre(lexema)
        
        seguir = True
        # Buscar la entrada en todas las tablas disponibles
        while((entrada == None or entrada == False) and seguir):
            tablaID = self.bloqueTS.get(tablaID)
            if (tablaID == None):
                seguir = False 
            else:
                self.ultimaTS = self.listaTS.get(tablaID)
                
                if self.ultimaTS == None:
                    seguir = False
                else:
                    entrada = self.ultimaTS.buscarTSNombre(lexema)
        
        return entrada
    
    # buscar el lexema en la tabla actual 
    def buscarEntradaTablaActualLexema(self,lexema):
        entrada = self.buscarEntradaPorLexema(lexema)
        
        if entrada == False or entrada == None:
            return False
        elif entrada.getTabla() != self.currentTablaID:
            return False
        else:
            return entrada
    
    # inserta la entrada en la tabla actual
    def insertarEntrada(self,lexema):
        tabla = self.listaTS.get(self.currentTablaID)
        
        return tabla.insertarValor(lexema,tabla.getId())
    
    # inserta la entrada en la tabla global
    def insertarEntradaTG(self,lexema):
        tabla= self.listaTS.get(1)
        
        return tabla.insertarValor(lexema,tabla.getId())
    
    # insertar el tipo de un id y actualizar el valor de proximo desplazamiento con el tamaño
    def insertarTipoTamTS(self,entID, tipo, tamanho):
        entrada = self.buscarEntradaPorID(int(entID))
        
        if entrada != None and entrada != False:
            
            entrada.setTipo(tipo)
            
            if(tamanho != False):
                self.ultimaTS = self.listaTS.get(entrada.getTabla())
            
                entrada.setDespl(self.ultimaTS.getUltimoDespl())
                self.ultimaTS.setUltimoDespl(self.ultimaTS.getUltimoDespl() + tamanho)
    
    # insertar el tipo de parametros de una entrada de tipo funcion
    def insertarTipoParametros(self,entID, tipoLista):
        entrada = self.buscarEntradaPorID(int(entID))
        
        if entrada != None and entrada != False:
            if type(tipoLista) is list:
                for t in tipoLista:
                    entrada.setTipoParametros(t)
                    entrada.setModoParametros("1")
            else:
                entrada.setTipoParametros(tipoLista)
                entrada.setModoParametros("1")
    
    # insertar el tipo de retorno de una entrada de tipo funcion
    def insertarTipoDevuelto(self,entID, tipo):
        entrada = self.buscarEntradaPorID(int(entID))
        
        if entrada != None and entrada != False:
            entrada.setTipoDevuelto(tipo) 
     
    # buscar el tipo de una entrada           
    def buscarTipo(self,entID):
        tipo = False
        entrada = self.buscarEntradaPorID(int(entID))
        if entrada != None and entrada != False:
            tipo = entrada.getTipo()
        
        return tipo
    
    # buscar el tipo de parametros de una entrada   
    def buscarTipoParametros(self,entID):
        tipo = False
        entrada = self.buscarEntradaPorID(int(entID))
        if entrada != None and entrada != False:
            tipo = entrada.getTipoParametros()
        
        return tipo

    # buscar el tipo de retorno de una entrada  
    def buscarTipoDevuelto(self,entID):
        tipo = False
        entrada = self.buscarEntradaPorID(int(entID))
        if entrada != None and entrada != False:
            tipo = entrada.getTipoDevuelto()
        
        return tipo