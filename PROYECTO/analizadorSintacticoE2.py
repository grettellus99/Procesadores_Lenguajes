from objetosGenerales.Reader import Reader
from analizadorLexico import AnalizadorLexico
from objetos_ASintac.Tabla import Tabla
from objetos_ASintac.datos import noTerminales
from objetosGenerales.GestorError import Error

#------------- Inicializaciones ---------------
analizadorLexico = AnalizadorLexico()

tablaAS = Tabla()

listaNT = noTerminales

error =  False

#----------- Parse ------------------
#------------ path a partir de Reader.py ------------
writerParse = Reader("../Ficheros Salida/parse.txt") 


#------------- Analizador Sintáctico -----------------
seguir = True
terminado = False

while(seguir):
    
    respAL = analizadorLexico.pedirToken()
    siguienteToken = respAL[0]
    terminado = respAL[1]
    
    tablaAS.setTokenActual(siguienteToken)
    
    pedirToken = False
    while(pedirToken == False and error == False):
        
        cimaPila = tablaAS.pila.pop() # obtener el último elemento de la pila
        
        if cimaPila in noTerminales:
            resTabla = tablaAS.comprobarToken(cimaPila) # la cima de la pila es un no terminal y se necesita modificar
                                                            # la pila dado el token actual
            
            pedirToken = resTabla[0] # determinar si se necesita pedir otro token
            
            error = resTabla[1] # determinar si hubo un error sintáctico
        
        # si la cima de la pila no es un no Terminal (implica que es terminal)
        else: 
            # el token debe coincidir con la cima de la pila
                if(siguienteToken == cimaPila):
                    pedirToken = True   # el token (terminal) coincide con la cima de la pila
                else: 
                    # el token (terminal) no coincide con la cima de la pila
                    error = Error(100,f"ERROR SINTÁCTICO - Token {siguienteToken} no esperado", "")
                
    if(terminado or error != False):
        seguir = False    

if(error != False):
    parse = tablaAS.parse
    writerParse.writeParse(parse)
    
else:
    ### GESTIONAR ERRORES ####
    errores = analizadorLexico.errores
    linea = analizadorLexico.readFicheroFuente.linea
    error.linea = linea
    
    errores.crearError(error)