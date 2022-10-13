
from objetos.Acciones import accionesSemanticas
from objetos.MatrizTransiciones import matrizTransiciones
from objetos.Reader import Reader
from objetos.TS import TablaSimbolos
from objetos.Token import ListaTokens

#------------ Inicializaciones ------------------

#------------ path a partir de Reader.py ------------
readFicheroFuente = Reader("../Ficheros Fuente/fichero_fuente.txt")
writerErrores=Reader("../Ficheros Salida/errores.txt")
writerErrores.write("Errores:",True)

writerTokens=Reader("../Ficheros Salida/tokens.txt")

#----- Creación de la instancia GLOBAL de Tabla de Símbolos --------------
tabla = TablaSimbolos()
listaTokens = ListaTokens()

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
            #   GESTION DE ERROES NO COMPLETADA #
            mensajeError="Error en línea "+readFicheroFuente.linea+". "+error.mensaje
            print(mensajeError)
            writerErrores.write(mensajeError,False)
    
        if(estadoFinal):    # c es un caracter que no está en una transicion o.c
            leer=True
        else:
            resAccion = accionesSemanticas(accion,c,listaTokens,tabla)    # realizar la accion semantica correspondiente
            leer=resAccion[0]
            error=resAccion[1]
            if(error):
                #   GESTION DE ERROES NO COMPLETADA #
                mensajeError="Error en línea "+readFicheroFuente.linea+". "+error.mensaje
                print(mensajeError)
                writerErrores.write(mensajeError,False)
                  
    else:   # si c es FALSE el fichero ha terminado
        seguir=False
        readFicheroFuente.close()
        listaTokens.addEndOfFile()
        for i in listaTokens.tokens:
            print(str(i.nombre) +"\t"+ str(i.valor) + "\n")
        