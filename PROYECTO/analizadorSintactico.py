from objetosGenerales.Reader import Reader
from analizadorLexico import AnalizadorLexico
from objetosASintac.Tabla import Tabla
from objetosASintac.datos import noTerminales
from objetosASintac.datos import tokenOp
from objetosASintac.datos import convertirOp
from objetosASemantico.datos import accionesSemanticas
from objetosGenerales.GestorError import Error
from objetosASemantico.Simbolo import Simbolo
from objetosASemantico.Acciones import VarAnalizadorSemantico
from TablaSimbolos.GestorTS import GestorTablaSimbolos
from objetosASemantico.Acciones import accionesAnalizadorSemantico


class AnalizadorSintactico():
    def __init__(self) :
        
        # Analizador lexico
        self.analizadorLexico = AnalizadorLexico()
        
        # Tabla de transiciones sintacticas 
        self.tablaAS = Tabla()
       
        # Error
        self.error =  False
        
        # Variables Aalizadador Semantico
        self.zona_decl = VarAnalizadorSemantico("zona_decl",False)
        self.decl_impl = VarAnalizadorSemantico("decl_impl",False)
        
        # Gestor Tabla Simbolos
        self.gestorTS =  GestorTablaSimbolos()
        
        #----------- Parse ------------------
        #------------ path a partir de Reader.py ------------
        self.writerParse = Reader("../Ficheros Salida/parse.txt") 
    
    def analisisSintactico(self):
        
        
        #------------- Analizador Sintáctico -----------------
        seguir = True
        terminado = False
        error = False
        pedirToken = True
        while(seguir):
            if(pedirToken):
                respAL = self.analizadorLexico.pedirToken(self.gestorTS,self.zona_decl.valor, self.decl_impl.valor)
                siguienteToken = respAL[0]
                terminado = respAL[1]
                
                self.tablaAS.setTokenActual(siguienteToken)
                siguienteToken = self.tablaAS.getTokenActual()
                
                pedirToken = False
            
            peticionToken = False
            
            while(pedirToken == False and error == False):
        
                cimaPila = self.tablaAS.pila.pop() # obtener el último elemento de la pila       
                if type(cimaPila) is Simbolo and cimaPila.nombreSimbolo in noTerminales:
                    self.tablaAS.aux.append(cimaPila) # añadir el simbolo a la pila auxiliar
        
                    resTabla = self.tablaAS.comprobarToken(cimaPila) # la cima de la pila es un no terminal y se necesita modificar
                                                            # la pila dado el token actual
            
                    peticionToken = resTabla[0] # determinar si se necesita pedir otro token
            
                    error = resTabla[1] # determinar si hubo un error sintáctico
                elif (type(cimaPila) is Simbolo) == False and cimaPila in accionesSemanticas:
                    
                    resAcciones = accionesAnalizadorSemantico(cimaPila,self.zona_decl.valor,self.decl_impl.valor,self.gestorTS,self.tablaAS.pila,self.tablaAS.aux)
                    
                    self.zona_decl.valor = resAcciones[0]
                    self.decl_impl.valor = resAcciones[1]
                    self.error = resAcciones[2]
                    
                # si la cima de la pila no es un no Terminal o una accion semantica (implica que es terminal)
                else: 
                # el token debe coincidir con la cima de la pila
                    if type(cimaPila) is Simbolo and siguienteToken == cimaPila.nombreSimbolo:

                        if siguienteToken == "id":
                            cimaPila.addAtributo("pos",self.tablaAS.valorToken)
                        
                        self.tablaAS.aux.append(cimaPila) # añadir el simbolo a la pila auxiliar
                        peticionToken = True   # el token (terminal) coincide con la cima de la pila
                        
                    elif (type(cimaPila) is Simbolo) == False and siguienteToken == cimaPila:
                        
                        self.tablaAS.aux.append(Simbolo(cimaPila)) # añadir el simbolo a la pila auxiliar
                        peticionToken = True   # el token (terminal) coincide con la cima de la pila
                    
                    else: # ----------- ERROR ------------ #
                        # el token (terminal) no coincide con la cima de la pila
                        
                        # Convertir los tokens de operadores en su valor para mejorar el mensaje de error
                        if siguienteToken in tokenOp:
                            siguienteToken = convertirOp[tokenOp.index(siguienteToken)]
                         
                        if (type(cimaPila) is Simbolo) == False and cimaPila in tokenOp:
                            cimaPila = convertirOp[tokenOp.index(cimaPila)]
                        
                        error = Error(100,f"ERROR SINTÁCTICO - Token {siguienteToken} no esperado. Se esperaba {cimaPila}", "")

                if peticionToken:
                    anteriorElemento = cimaPila
                    cimaPila = self.tablaAS.pila.pop()  # obtener el último elemento de la pila
                    if (cimaPila in accionesSemanticas)==False:
                        pedirToken = True
                        peticionToken = False
                        self.tablaAS.pila.append(cimaPila)
                        cimaPila = anteriorElemento
                    else:
                        self.tablaAS.pila.append(cimaPila)
                        cimaPila = anteriorElemento
                    
                if(terminado or (error != False)):
                    seguir = False    

        # Termina el bucle porque detecta un error LEXICO | SINTACTICO | SEMANTICO o porque llega al final del analisis
        if(error == False):
            parse = self.tablaAS.parse
            self.writerParse.writeParse(parse) # Escribir el parse en el fichero parse.txt
            
        else:
            
            ### GESTIONAR ERRORES ####
            self.writerParse.writeParse("ERROR")         # invalidar el fichero parse
            errores = self.analizadorLexico.errores      # obtener el gestor de errores del AL
            
            if error.cod == 226: # error producido por comparar el valor de retorno declarado de la funcion con el valor de retorno actual y estos no son iguales
                                # Como se hace al final del bloque el numLinea actual no sería correcto
                linea = self.analizadorLexico.lineaPrincipioBloque # Obtener la linea donde estaba el token function
            else:
                linea = self.analizadorLexico.readFicheroFuente.numLinea     # obtener el num de línea actual
            
            error.linea = linea     # actualizar la linea del error obtenido
    
            errores.crearError(error)   # crear el error agregándolo a la lista del gestor y al fichero errores
        
        # Terminar la ejecucion del A. Sintactico + Semantico.
        if(terminado):
            return True
        else:
            return False