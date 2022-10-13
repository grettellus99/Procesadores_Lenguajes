from objetos.Reader import Reader

# Definir una entrada en la Tabla de Simbolos
class EntradaTablaSimbolos():
    def __init__(self,n,p):
        self.pos=p
        self.nombre=n
        

# Tabla de Simbolos    
class TablaSimbolos():
    def __init__(self):
        self.identificadores=[]     # array de identificadores
        self.writerFichero = Reader("../Ficheros Salida/tabla.txt")     # crear el reader al fichero de salida de la Tabla de Símbolos
        self.writerFichero.write("Tabla de Símbolos",True)     # Borrar lo escrito por compilaciones anteriores
        
    def insertarValor(self,n):
        pos= len(self.identificadores)      # la posicion a insertar será la última de la lista de identificadores
                                            # determinado por la longitud actual del array
        entrada=EntradaTablaSimbolos(n,pos)     # creacion de un objeto EntradaTS para definirle atributos internos nombre y posicion
        self.identificadores.append(entrada)      # agregar el objeto crado al final del array de identificadores de la TS
        
        try:
            self.writerFichero.write("LEXEMA: " + n + "\t" +"POSICION: " + str(pos), False)      # escribir la nueva entrada en el fichero SIN sobrescribir
        except OSError as err:
            print("Error: {0}",format(err))
        
        return pos      # devolver la posicion donde fue insertada la nueva entrada (final del array)
        
    def buscarLugarTSNombre(self,nombre):
        
        entradas=self.identificadores
        tamanoTS= len(entradas)
        i=0;
        pos=False;
        encontrado=False
        insertar=True
        while(i<tamanoTS):
            ## Como es case sensitive tiene que coincidir en mayúsculas y minúsculas
            if(entradas[i].nombre == nombre):
                encontrado = True
            if(encontrado):
                pos=i
                i=tamanoTS  # terminar el bucle en la siguiente iteracion sin break
                insertar=False            
            else:
                i+=1        # siguiente posicion        
        
        return pos,insertar  # devolver la posición del identificador. Si no lo encuentra retorna False

        