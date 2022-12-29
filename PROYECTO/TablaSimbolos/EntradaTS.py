
# Definicion de Tipos
class Tipo ():
    UNDEFINED = "undefined"
    ENTERO = "tipo_entero"
    CADENA = "tipo_cadena"
    LOGICO = "tipo_logico"
    FUNCION = "tipo_funcion"
    VACIO = "tipo_vacio"
    OK = "tipo_ok"
    ERROR = "tipo_error"

# Definir una entrada en la Tabla de Simbolos
class EntradaTablaSimbolos():
    ENTRADA_ID = 0
    NUM_ETIQUETA = 1
    
    def __init__(self,lex):
        # Definir el lexema
        self.lexema=lex
        
        # Definir el id
        self.id = EntradaTablaSimbolos.ENTRADA_ID
        # Tipo inicial NO DEFINIDO
        self.tipo = Tipo.UNDEFINED
        
        # Desplazamiento inicial negativo 
        # ( entero | cadena | logico )
        self.despl = -1
        
        # Num Parametros inicial negaativo (funcion)
        self.numParametros = -1
        
        # Tipo parametros inicial vacio (funcion)
        self.tipoParametros = []
        
        # Metodo paso de parametros inicial vacio (funcion)
        self.modoParametros = []
        
        # Tipo devuelto no definido
        self.tipoDevuelto = Tipo.UNDEFINED
        
        # Etiqueta no definida
        self.etiqueta = ""
        
        # Tabla a la que pertenece
        self.tabla = 0
        
        # Obtener siguiente id
        EntradaTablaSimbolos.ENTRADA_ID+=1

        
    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id
    
    def getTabla(self):
        return self.tabla
    
    def setTabla(self, idTabla):
        self.tabla = idTabla
    
    def getLexema(self):
        return self.lexema
    
    def getTipo(self):
        return self.tipo
    
    def setTipo (self,tipo):
        self.tipo = tipo
    
    def getDespl(self):
        return self.despl
   
    def setDespl (self,despl):
        self.despl = despl
    
    def getNumParametros(self):
        return self.numParametros
    
    def setNumParametros(self,num):
        self.numParametros = num
    
    def getTipoParametros(self):
        return self.tipoParametros
    
    def setTipoParametros(self,tp):
        self.tipoParametros.append(tp)
    
    def getModoParametros(self):
        return self.modoParametros
    
    def setModoParametros(self,metodo):
        self.modoParametros.append(metodo)
    
    def getTipoDevuelto(self):
        return self.tipoDevuelto
    
    def setTipoDevuelto(self,tipo):
        self.tipoDevuelto = tipo
    
    def getEtiqueta(self):
        return self.etiqueta
    
    def setEtiqueta(self):
        self.etiqueta = "Et" + str(self.lexema) + str(EntradaTablaSimbolos.NUM_ETIQUETA)
        EntradaTablaSimbolos.NUM_ETIQUETA+=1
    
    
    def toString(self):
        salida = "\t* LEXEMA :\t" + f"'{self.lexema}'" + "\n" + "\tATRIBUTOS :\n"
        salida += "\t+ tipo :\t"+str(self.tipo) + "\n"
        
        if self.tipo != Tipo.FUNCION:    
            salida += "\t+ despl :\t"+str(self.despl) + "\n\t----------- ----------\n"
        else:
            salida += "\t\t+ numPar :\t"+str(self.numParametros) + "\n"
            
            cont = 1
            for t in self.tipoParametros:
               salida += f"\t\t\t+ tipoParam{str(cont)} :\t"+ str(t) + "\n"
               salida += f"\t\t\t\t+ modoParam{str(cont)} :\t"+ str(self.modoParametros[cont-1]) + "\n"
               cont+=1
            salida += f"\t\t\t+ tipoRetorno :\t"+ str(self.tipoDevuelto) + "\n"
            salida += f"\t\t+ etiqFuncion :\t"+ str(self.etiqueta) + "\n\t----------- ----------\n"
              
        return salida