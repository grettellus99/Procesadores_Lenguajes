from objetos_AL.Acciones import accionesSemanticas
from objetos_AL.MatrizTransiciones import matrizTransiciones
from objetosGenerales.Reader import Reader
from objetos_AL.TS import TablaSimbolos
from objetos_AL.Token import ListaTokens
from objetosGenerales.GestorError import *


class AnalizadorLexico():

    def __init__(self):
        #------------ Inicializaciones ------------------  
        self.tabla = TablaSimbolos()
        self.listaTokens = ListaTokens()
        self.errores = GestorError()
        self.leer=True
        self.estadoSiguiente="S"
        self.estadoFinal=False
        self.accion=0
        self.error=False
        self.c=""    
        
        #------------ path a partir de Reader.py ------------
        self.readFicheroFuente = Reader("../Ficheros Fuente/fichero_fuente.txt")  
    
    
    def pedirToken(self):
        self.terminado = False
        seguir = True
        while(seguir):
            if(self.leer):   # si la accion anterior no devuelve leer en true NO se lee el siguiente carácter
                self.c=self.readFicheroFuente.readSigCaracter()
    
            # si el carácter leído es False es fin de fichero pero puede que todavía no se
            # haya realizado la última acción en transiciones con o.c como transición final
            # así que se comprueba que el estado actual sea S
            if(self.c==False and self.estadoSiguiente == "S"):  
                self.terminado=True
    
            # si Terminado es False sigue
            # determinar la siguiente transicion con el último caracter leído
            if(self.terminado==False):    
                transicion=matrizTransiciones(self.estadoSiguiente,self.c)
    
                self.accion=transicion[0]            # obtener la siguiente acción semántica
                self.estadoSiguiente=transicion[1]   # obtener el estado siguiente dado el carácter
                self.estadoFinal=transicion[2]       # es True si es un estado final
                self.error=transicion[3]             # NO es False si hay un error en las transiciones
        
        
                if(self.error):
                     #   Si hay un error y no ha terminado de leer --> Leer siguiente caracter hasta delimitador
                    if(self.estadoSiguiente != "S" and (self.error.cod == 52 or self.error.cod == 53 or self.error.cod == 54)):
                        while(c!=10 and c!=13 and c!=False): 
                            c=self.readFicheroFuente.readSigCaracter()
                    elif(self.estadoSiguiente != "S" and (self.error.cod == 51 or self.error.cod == 55)):
                            self.leer=False
                
                    elif(self.estadoSiguiente == "S" and self.error.cod == 50):
                        self.leer=True
                
                    self.error.linea = f"{self.readFicheroFuente.numLinea}"
                    self.errores.crearError(self.error)  
            
                    # Reinicializar el estado
                    self.estadoSiguiente = "S"        
                    self.error = False 
        
                elif(self.estadoFinal):    # se llega a un estado final
                    self.seguir = False # se para el bucle porque ya se generó el siguiente token
                    
                else:
                    resAccion = accionesSemanticas(self.accion,self.c,self.listaTokens,self.tabla)    # realizar la accion semantica correspondiente
                    self.leer=resAccion[0]
                    self.error=resAccion[1]
            
                    if(self.error):
                        #   Si hay un error y no ha terminado de leer --> Leer siguiente caracter hasta delimitador
                        self.error.linea = f"{self.readFicheroFuente.numLinea}"
                        self.errores.crearError(self.error)  
             
                        self.error= False
                  
            else:   # si c es FALSE el fichero ha terminado
                seguir=False
                self.readFicheroFuente.close()
                self.listaTokens.addEndOfFile()
                #for i in self.listaTokens.tokens:
                #   print(str(i.nombre) +"\t"+ str(i.valor) + "\n")
          
        t = self.listaTokens.getLastToken()
        return t,self.terminado