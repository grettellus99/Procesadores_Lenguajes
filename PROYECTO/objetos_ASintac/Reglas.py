from objetos_ASintac.datos import *
from GestorError import Error
from objetos_ASintac.Pila import Pila


# Reglas de grámatica Analizador Sintáctico
class Reglas:
    
    def __init__(self):
        self.token = ""  
        self.valorToken = ""
        self.parse=[]
        self.pila= Pila()
        
    
    # Establecer el token actual
    def setTokenActual(self,t):
        self.token = t.nombre
        self.valorToken = str(t.valor)
     
     
    def comprobarToken(self,nT,pedirToken,error):
    
    # ----------- INICIALIZAR  -----------   
        t=self.token
        tv=t + self.valorToken
        pedirToken = False
        error=False
    #----------------------------------------------------------------------------------------
        if nT == "A":
            self.pila.equipara(nT)
            if t in firstA1:    
                self.parse.append(1)
                self.pila.append("A")
                self.pila.append("B")
            
            elif t in firstA2:
                self.parse.append(2)   
                self.pila.append("A")
                self.pila.append("F")
            
            elif t in firstA3:
                self.parse.append(3)
                coincide=self.pila.equipara(t)
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
    #----------------------------------------------------------------------------------------  
        elif nT == "B":
            self.pila.equipara(nT)
            if t in firstB1:
                self.parse.append(4)
                self.pila.append("S")
                self.pila.append("cerrarParentesis")
                self.pila.append("E")
                self.pila.append("abrirParentesis")
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif t in firstB2:
                self.parse.append(5)
                self.pila.append("N")
                self.pila.append("T")
                self.pila.append("id")
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif t in firstB3:
                self.parse.append(6)
                self.pila.append("S")
            
            elif t in firstB4:
                self.parse.append(7)
                self.pila.append("cerrarCorchete")
                self.pila.append("Z")
                self.pila.append("abrirCorchete")
                self.pila.append("cerrarParentesis")
                self.pila.append("U")
                self.pila.append("abrirParentesis")
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
    #----------------------------------------------------------------------------------------
        elif nT == "S":
            self.pila.equipara(nT)
            if t in firstS1:
                self.parse.append(8)
                self.pila.append("ptoComa")
                self.pila.append("S'")
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif t in firstS2:
                self.parse.append(9)
                self.pila.append("ptoComa")
                self.pila.append("E")
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif t in firstS3:
                self.parse.append(10)
                self.pila.append("ptoComa")
                self.pila.append("id")
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif t in firstS4:
                self.parse.append(11)
                self.pila.append("ptoComa")
                self.pila.append("X")
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
                
    #----------------------------------------------------------------------------------------
        elif nT == "S'":
            self.pila.equipara(nT)
            if t in firstSprima1:
                self.parse.append(12)
                self.pila.append("E")
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif t in firstSprima2:
                self.parse.append(13)
                self.pila.append("U")
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif t in firstSprima3:
                self.parse.append(14)
                self.pila.append("cerrarParentesis")
                self.pila.append("L")
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
    #----------------------------------------------------------------------------------------
        elif nT == "E":
            if t in firstE1:
                self.parse.append(15)
                self.pila.append("E'")
                self.pila.append("R")
    
    #----------------------------------------------------------------------------------------    
        elif nT == "E'":
            if t in followE:
               self.parse.append(16)             
            
            elif (tv in firstEprima2):
                self.parse.append(17)
                self.pila.append("E'")
                self.pila.append("R")
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")  
                
    #   
       
        

    #----------------------------------------------------------------------------------------             
                
                
        return pedirToken,error