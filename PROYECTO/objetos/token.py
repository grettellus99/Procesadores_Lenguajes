from objetos.Reader import Reader

class Token:
    def __init__(self,n,v):
            self.nombre = n
            self.valor = v
            

class ListaTokens:
    def __init__(self):
            self.tokens=[]
       ##### Inicilizar fichero tokens.txt ####
            self.writeFichero = Reader("../Ficheros Salida/tokens.txt")
            self.writeFichero.write("\n",True)
    
    def addFichero(self,token):
        try:
            self.writeFichero.write(token,False)    # escribir el nuevo token en el fichero
        except OSError as err:
            print("Error: {0}",format(err)) 
    
    def addTokenPalabraReservada(self,lexema):
        token=Token(lexema, " ")     # añadir a la lista como Token
        self.tokens.append(token)
        
        tokenFichero="< "+lexema+" ,  >"    # añadir al fichero 
        self.addFichero(tokenFichero)
    
    def addTokenIdentificador(self,pos):
        token=Token("id",pos)     # añadir a la lista como Token
        self.tokens.append(token)
        
        tokenFichero="< id  , "+ str(pos) +" >"    # añadir al fichero 
        self.addFichero(tokenFichero)
      
    def addTokenConstEntera(self,valor):
        token=Token("cteEntera",valor)     # añadir a la lista como Token
        self.tokens.append(token)
        
        tokenFichero="< cteEntera , " + str(valor) +" >"    # añadir al fichero 
        self.addFichero(tokenFichero)     

    def addTokenCadena(self,lexema):
        token=Token("cadena",lexema)     # añadir a la lista como Token
        self.tokens.append(token)
        
        tokenFichero="< cadena , " + lexema +" >"    # añadir al fichero 
        self.addFichero(tokenFichero)     
    
    def addTokenOperadoresSignos(self,op,num):
        token=Token(op,num)     # añadir a la lista como Token
        self.tokens.append(token)
        
        tokenFichero="< "+op+" , "+ str(num) +" >"    # añadir al fichero 
        self.addFichero(tokenFichero)     
    
    def addEndOfFile(self):
        token=Token("eof"," ")
        self.tokens.append(token)
        
        tokenFichero="< eof ,  >"
        self.addFichero(tokenFichero)
