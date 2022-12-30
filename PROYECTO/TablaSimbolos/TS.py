from TablaSimbolos.EntradaTS import EntradaTablaSimbolos

# Tabla de Simbolos    
class TablaSimbolos():
    NTABLAS = 0
    def __init__(self):
        TablaSimbolos.NTABLAS+=1
        self.id = TablaSimbolos.NTABLAS
        
        self.indices = {}
        self.entradas = {}
        
        self.ultimoDespl = 0
        
        
    def toString(self):
        salida = f"CONTENIDOS DE LA TABLA # {self.id} :\n\n"
        for e in self.entradas.values():
            salida += e.toString()
        return salida
    
    def getId(self):
        return self.id
    
    def getUltimoDespl(self):
        return self.ultimoDespl
    
    def setUltimoDespl(self,despl):
        self.ultimoDespl = despl
    
    def insertarValor(self,lex,idTabla):
        
        entrada = EntradaTablaSimbolos(lex)
        entrada.setTabla(idTabla)
        self.indices.__setitem__(lex,entrada.getId())
        self.entradas.__setitem__(entrada.getId(),entrada)

        return entrada.getId()
        
    # Obtener el id (pos) del lexema en el mapa lexema --> pos y con este la entrada 
    # Si no lo encuetra devuelve falso
    def buscarTSNombre(self,lexema):
        keys = list(self.indices.keys())
        entrada = False
        if lexema in keys:
            entrada = self.entradas.get(self.indices.get(lexema)) 
        return entrada  # devolver la entrada correspondiente al id del identificador. Si no lo encuentra retorna False

    # Obtener el objeto EntradaTablaSimbolos dado el id (pos)
    def buscarEntradaID(self,id):
        return self.entradas.get(id)