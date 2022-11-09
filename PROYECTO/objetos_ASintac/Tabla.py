from objetos_ASintac.datos import *
from objetosGenerales.GestorError import Error
from objetos_ASintac.Pila import Pila


# Reglas de grámatica Analizador Sintáctico
class Tabla:
    
    def __init__(self):
        self.token = ""  
        self.valorToken = ""
        self.parse=[]
        self.pila= Pila()
        self.pila.append("A")    #inicializar la pila con el axioma
        
    
    # Establecer el token actual
    def setTokenActual(self,t):
        self.token = t.nombre
        self.valorToken = str(t.valor)
     
    def getTokenActual(self):
        t = self.token
        tv = ""
        if(t != "id" and t != "cadena" and t != "cteEntera"):
            tv = t + self.valorToken
        else:
            tv = t
        return tv  
    
    def getTokenName(self):
        tv = self.getTokenActual()
        if tv in tokenOp:
            l = tokenOp
            index = l.index(tv)
            tv = convertirOp[index]   
        return tv
     
    def comprobarToken(self,nT):
  
    # ----------- INICIALIZAR  -----------   
        tv=self.getTokenActual()
        t = self.getTokenName()
        
        pedirToken = False
        error=False
    #----------------------------------------------------------------------------------------
        if nT == "A":
            if tv in firstA1:    
                self.parse.append(1)
                self.pila.append("A")
                self.pila.append("B")
            
            elif tv in firstA2:
                self.parse.append(2)   
                self.pila.append("A")
                self.pila.append("F")
            
            elif tv in firstA3:
                self.parse.append(3)
                self.pila.append("eof")
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
    #----------------------------------------------------------------------------------------  
        elif nT == "B":
            if tv in firstB1:
                self.parse.append(4)
                self.pila.append("S")
                self.pila.append("cerrarParentesis")
                self.pila.append("E")
                self.pila.append("abrirParentesis")
                self.pila.append("if")
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif tv in firstB2:
                self.parse.append(5)
                self.pila.append("N")
                self.pila.append("T")
                self.pila.append("id")
                self.pila.append("let")
                
                if(self.pila.equipara(t)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif tv in firstB3:
                self.parse.append(6)
                self.pila.append("S")
            
            elif tv in firstB4:
                self.parse.append(7)
                self.pila.append("cerrarCorchete")
                self.pila.append("Z")
                self.pila.append("abrirCorchete")
                self.pila.append("cerrarParentesis")
                self.pila.append("U")
                self.pila.append("abrirParentesis")
                self.pila.append("switch")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
    #----------------------------------------------------------------------------------------
        elif nT == "S":
            if tv in firstS1:
                self.parse.append(8)
                self.pila.append("ptoComa")
                self.pila.append("S'")
                self.pila.append("id")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif tv in firstS2:
                self.parse.append(9)
                self.pila.append("ptoComa")
                self.pila.append("E")
                self.pila.append("print")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif tv in firstS3:
                self.parse.append(10)
                self.pila.append("ptoComa")
                self.pila.append("id")
                self.pila.append("input")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif tv in firstS4:
                self.parse.append(11)
                self.pila.append("ptoComa")
                self.pila.append("X")
                self.pila.append("return")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
                
    #----------------------------------------------------------------------------------------
        elif nT == "S'":
            if tv in firstSprima1:
                self.parse.append(12)
                self.pila.append("E")
                self.pila.append("asignacion")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif tv in firstSprima2:
                self.parse.append(13)
                self.pila.append("U")
                self.pila.append("asigMultiplicacion")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif tv in firstSprima3:
                self.parse.append(14)
                self.pila.append("cerrarParentesis")
                self.pila.append("L")
                self.pila.append("abrirParentesis")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")

            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
    #----------------------------------------------------------------------------------------
        elif nT == "E":
            if tv in firstE1:
                self.parse.append(15)
                self.pila.append("E'")
                self.pila.append("R")

            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
    #----------------------------------------------------------------------------------------    
        elif nT == "E'":
            if tv in followE:
               self.parse.append(16)             
            
            elif tv in firstEprima2:
                self.parse.append(17)
                self.pila.append("E'")
                self.pila.append("R")
                self.pila.append("opLogico1")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")  
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
                
    #---------------------------------------------------------------------------------------   
        elif nT == "R":
            if tv in firstR1 or tv in firstR1:
                self.parse.append(18)
                self.pila.append("R'")
                self.pila.append("U")
                
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")          

    #----------------------------------------------------------------------------------------             
        elif nT == "R'":
            if tv in followRprima:
                self.parse.append(19)
            
            elif tv in firstRprima2:
                self.parse.append(20)
                self.pila.append("R'")
                self.pila.append("U")
                self.pila.append("opRelacional1")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
                          
    #-----------------------------------------------------------------------------------------
        elif nT == "U":
            if tv in firstU1:
                self.parse.append(21)
                self.pila.append("U'")
                self.pila.append("V")
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
    
    
    
    #----------------------------------------------------------------------------------------- 
        elif nT == "U'":
            if tv in followUprima:
                self.parse.append(22)
            
            elif tv in firstUprima2:
                self.parse.append(23)
                self.pila.append("U'")
                self.pila.append("V")
                self.pila.append("opAritmetico2")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")

            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
    
    #-----------------------------------------------------------------------------------------
        elif nT == "V":
            if tv in firstV1:
                self.parse.append(24)
                self.pila.append("V'")
                self.pila.append("P")
                
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
        
    #-----------------------------------------------------------------------------------------
        elif nT == "V'":
            if tv in followVprima:
                self.parse.append(25)
            
            elif tv in firstVprima2:
                self.parse.append(26)
                self.pila.append("V'")
                self.pila.append("P")
                self.pila.append("opAritmetico1")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")

            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
        
    #-----------------------------------------------------------------------------------------   
        elif nT == "P":
            if tv in firstP1:
                self.parse.append(27)
                self.pila.append("P'")
                self.pila.append("id")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")

            elif tv in firstP2:
                self.parse.append(28)
                self.pila.append("cerrarParentesis")
                self.pila.append("E")
                self.pila.append("abrirParentesis")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")

            elif tv in firstP3:
                self.parse.append(29)
                self.pila.append("cteEntera")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")


            elif tv in firstP4:
                self.parse.append(30)
                self.pila.append("cadena")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")

            elif tv in firstP5:
                self.parse.append(31)
                self.pila.append("true")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")

            elif tv in firstP6:
                self.parse.append(32)
                self.pila.append("false")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")

            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
        
    #-----------------------------------------------------------------------------------------               
        elif nT == "P'":
            if tv in followPprima:
                self.parse.append(33)

            elif tv in firstPprima2:
                self.parse.append(34)
                self.pila.append("cerrarParentesis")
                self.pila.append("L")
                self.pila.append("abrirParentesis")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")

            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
        
    #-----------------------------------------------------------------------------------------   
        elif nT == "L":
            if tv in firstL1:
                self.parse.append(35)
                self.pila.append("Q")
                self.pila.append("E")
            
            elif tv in followL:
                self.parse.append(36)
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
    #-----------------------------------------------------------------------------------------               
        elif nT == "Q":
            if tv in firstQ1:
                self.parse.append(37)
                self.pila.append("Q")
                self.pila.append("E")
                self.pila.append("coma")
                 
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")

            elif tv in followQ:
                self.parse.append(38)
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
    #-----------------------------------------------------------------------------------------   
        elif nT == "X":
            if tv in firstX1:
                self.parse.append(39)
                self.pila.append("E")
            
            elif tv in followX:
                self.parse.append(40)
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
    #-----------------------------------------------------------------------------------------               
        elif nT == "T":
            if tv in firstT1:
                self.parse.append(41)
                self.pila.append("int")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif tv in firstT2:
                self.parse.append(42)
                self.pila.append("boolean")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
             
            elif tv in firstT3:
                self.parse.append(43)
                self.pila.append("string")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
                 
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")         
    
    #-----------------------------------------------------------------------------------------   
        elif nT == "F":
            if tv in firstF1:
                self.parse.append(44)
                self.pila.append("cerrarCorchete")
                self.pila.append("C")
                self.pila.append("abrirCorchete")
                self.pila.append("cerrarParentesis")
                self.pila.append("D")
                self.pila.append("abrirParentesis")
                self.pila.append("H")
                self.pila.append("id")
                self.pila.append("function")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")      
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")         
    
    #-----------------------------------------------------------------------------------------               
        elif nT == "H":
            if tv in firstH1:
                self.parse.append(45)
                self.pila.append("T")
            
            elif tv in followH:
                self.parse.append(46)
                
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")         
    
    #-----------------------------------------------------------------------------------------   
        elif nT == "D":
            if tv in firstD1:
                self.parse.append(47)
                self.pila.append("K")
                self.pila.append("id")
                self.pila.append("T")
            
            elif tv in followD:
                self.parse.append(48)
                
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")         
    
    #-----------------------------------------------------------------------------------------               
        elif nT == "K":
            if tv in firstK1:
                self.parse.append(49)
                self.pila.append("K")
                self.pila.append("id")
                self.pila.append("T")
                self.pila.append("coma")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
            
            elif tv in followK:
                self.parse.append(50)
                
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")         
    
    #-----------------------------------------------------------------------------------------   
        elif nT == "C":
            if tv in firstC1:
                self.parse.append(51)
                self.pila.append("C")
                self.pila.append("B")
                
            elif tv in followC:
                self.parse.append(52)
                
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")         
    
        
    #-----------------------------------------------------------------------------------------               
        elif nT == "N":
            if tv in firstN1:
                self.parse.append(53)
                self.pila.append("ptoComa")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
                
            elif tv in firstN2:
                self.parse.append(54)
                self.pila.append("E")
                self.pila.append("asignacion")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
                
            elif tv in firstN3:
                self.parse.append(55)
                self.pila.append("E")
                self.pila.append("asigMultiplicacion")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
                
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")         
    
    #-----------------------------------------------------------------------------------------   
        elif nT == "Z":
            if tv in firstZ1:
                self.parse.append(56)
                self.pila.append("Z")
                self.pila.append("O")
                self.pila.append(":")
                self.pila.append("cteEntera")
                self.pila.append("case")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")  
            
            elif tv in firstZ2:
                self.parse.append(57)
                self.pila.append("O")
                self.pila.append(":")
                self.pila.append("default")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")  
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")         
    
    #-----------------------------------------------------------------------------------------               
        elif nT == "O":
            if tv in firstO1:
                self.parse.append(58)
                self.pila.append("O'")  
                self.pila.append("B") 
            
            elif tv in firstO2:
                self.parse.append(59)
                self.pila.append("ptoComa")  
                self.pila.append("break")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")  
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")         
            
    #-----------------------------------------------------------------------------------------   
        elif nT == "O'":
            if tv in firstOprima1:
                self.parse.append(60)
                self.pila.append("O'")  
                self.pila.append("B") 
            
            elif tv in firstOprima2:
                self.parse.append(61)
                self.pila.append("ptoComa")  
                self.pila.append("break")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                else:
                    error=Error(0,f"ERROR SINTÁCTICO - Token {t} no esperado", "")  
            
            elif tv in followOprima:
                self.parse.append(62)
            
            else:
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")         
                 
    #-----------------------------------------------------------------------------------------               
        return pedirToken,error