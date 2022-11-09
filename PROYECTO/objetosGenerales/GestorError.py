from objetosGenerales.Reader import Reader

# Definir una clase error
class Error():
    def __init__ (self,cod,mensaje,linea):
        self.cod=cod
        self.mensaje=mensaje
        self.linea=linea
        
class GestorError():
     
    def __init__ (self):
          ##### Inicilizar fichero tokens.txt ####
        self.writeFichero = Reader("../Ficheros Salida/errores.txt")
        self.writeFichero.write("\n",True)
        self.listaErrores=[]
        
        
    def addFichero(self,mensaje):
        try:
            self.writeFichero.write(mensaje,False)    # escribir el nuevo token en el fichero
        except OSError as err:
            print("Error: {0}",format(err)) 
    
    def crearError(self,error):
        # Añadir el error a la lista de errores 
        self.listaErrores.append(error)
        
        # Escribir el error en el fichero
        mensajeError= f"Línea {error.linea} - Código de error {error.cod}: \n\t {error.mensaje}"
        self.addFichero(mensajeError)
        self.addFichero("\n")
    
        