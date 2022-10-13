
from objetos.Acciones import accionesSemanticas
from objetos.MatrizTransiciones import matrizTransiciones
from objetos.Reader import Reader
from objetos.TS import TablaSimbolos
from objetos.Token import ListaTokens
from objetos.datos import op

#------------ Inicializaciones ------------------

#------------ path a partir de Reader.py ------------
readFicheroFuente = Reader("../Ficheros Fuente/fichero_fuente.txt")
writerErrores=Reader("../Ficheros Salida/errores.txt")
writerErrores.write("Errores de compilación",True)

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
seguir = True
while(seguir):
    if(leer):   # si la accion anterior no devuelve leer en true NO se lee el siguiente carácter
        c=readFicheroFuente.readSigCaracter()
    
    if(c):  # si c no es False sigue
        # determinar la siguiente transicion con el último caracter leído
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
        
        if(estadoFinal): # reestablecer leer estados dende S es estado final
            if c in op:
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
        for i in listaTokens.tokens:
            print(str(i.nombre) +"\t"+ str(i.valor) + "\n")
        #writerTokens.write("< eof , - >", False) # Agregar el token fin de fichero a la lista de tokens
        print("Fin de fichero")
        