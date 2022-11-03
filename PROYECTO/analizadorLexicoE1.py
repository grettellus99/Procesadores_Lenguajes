
from objetos_AL.Acciones import accionesSemanticas
from objetos_AL.MatrizTransiciones import matrizTransiciones
from objetos_AL.Reader import Reader
from objetos_AL.TS import TablaSimbolos
from objetos_AL.Token import ListaTokens
from GestorError import *

#------------ Inicializaciones ------------------

#------------ path a partir de Reader.py ------------
readFicheroFuente = Reader("../Ficheros Fuente/fichero_fuente.txt")

#----- Creación de la instancia GLOBAL de Tabla de Símbolos --------------
tabla = TablaSimbolos()
listaTokens = ListaTokens()
errores=GestorError()

leer=True
estadoSiguiente="S"
estadoFinal=False
accion=0
error=False
c=""

#------------- ANALIZADOR LÉXICO ---------------------
terminado = False
seguir = True
while(seguir):
    if(leer):   # si la accion anterior no devuelve leer en true NO se lee el siguiente carácter
        c=readFicheroFuente.readSigCaracter()
    
    # si el carácter leído es False es fin de fichero pero puede que todavía no se
    # haya realizado la última acción en transiciones con o.c como transición final
    # así que se comprueba que el estado actual sea S
    if(c==False and estadoSiguiente == "S"):  
        terminado=True
    
    # si Terminado es False sigue
    # determinar la siguiente transicion con el último caracter leído
    if(terminado==False):    
        transicion=matrizTransiciones(estadoSiguiente,c)
    
        accion=transicion[0]            # obtener la siguiente acción semántica
        estadoSiguiente=transicion[1]   # obtener el estado siguiente dado el carácter
        estadoFinal=transicion[2]       # es True si es un estado final
        error=transicion[3]             # NO es False si hay un error en las transiciones
        
        
        
        if(error):
            #   Si hay un error y no ha terminado de leer --> Leer siguiente caracter hasta delimitador
            if(estadoSiguiente != "S" and (error.cod == 52 or error.cod == 53 or error.cod == 54)):
                while(c!=10 and c!=13 and c!=False): 
                    c=readFicheroFuente.readSigCaracter();
            elif(estadoSiguiente != "S" and (error.cod == 51 or error.cod == 55)):
                leer=False
                
            elif(estadoSiguiente == "S" and error.cod == 50):
                leer=True
                
            error.linea = f"{readFicheroFuente.numLinea}"
            errores.crearError(error)  
            
            # Reinicializar el estado
            estadoSiguiente = "S"        
            error= False 
        
        elif(estadoFinal):    # c es un caracter que no está en una transicion o.c
            leer=True
        else:
            resAccion = accionesSemanticas(accion,c,listaTokens,tabla)    # realizar la accion semantica correspondiente
            leer=resAccion[0]
            error=resAccion[1]
            
            if(error):
                #   Si hay un error y no ha terminado de leer --> Leer siguiente caracter hasta delimitador
                error.linea = f"{readFicheroFuente.numLinea}"
                errores.crearError(error)  
             
                error= False
                  
    else:   # si c es FALSE el fichero ha terminado
        seguir=False
        readFicheroFuente.close()
        listaTokens.addEndOfFile()
        for i in listaTokens.tokens:
            print(str(i.nombre) +"\t"+ str(i.valor) + "\n")
        