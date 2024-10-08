from objetosASintac.datos import *
from objetosGenerales.GestorError import Error
from objetosASintac.Pila import Pila
from objetosASemantico.Simbolo import Simbolo


# Reglas de grámatica Analizador Sintáctico
class Tabla:
    
    def __init__(self):
        self.token = ""  
        self.valorToken = ""
        self.parse=[]
        self.pila= Pila() # pila principal Analizador Sintactico
        self.aux = Pila() # pila auxiliar para Analizador Semantico
         
        ap = Simbolo("A'") 
        self.pila.append(ap)    # inicializar la pila con el axioma
        
    
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
        
        simnT = nT
        nT = simnT.nombreSimbolo
        
        pedirToken = False
        error=False
    #----------------------------------------------------------------------------------------
        if nT == "A'":
            if tv in firstAprima:
                self.parse.append(1)
                self.pila.append(1.2)
                a = Simbolo("A")
                self.pila.append(a)
                self.pila.append(1.1)
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado", "")
                
        if nT == "A":
            if tv in firstA1:    
                self.parse.append(2)
                a = Simbolo("A")
                self.pila.append(a)
                b = Simbolo("B")
                self.pila.append(b)
            
            elif tv in firstA2:
                self.parse.append(3)
                a = Simbolo("A")   
                self.pila.append(a)
                f = Simbolo("F")
                self.pila.append(f)
            
            elif tv in firstA3:
                self.parse.append(4)
                self.pila.append("eof")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba fin de fichero", "")
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(101,f"ERROR SINTÁCTICO - El token {t} no pertenece al primer elemento de una sentencia válida, una función o es fin de fichero", "")
    #----------------------------------------------------------------------------------------  
        elif nT == "B":
            if tv in firstB1:
                self.parse.append(5)
                self.pila.append(5.2)
                s = Simbolo("S")
                self.pila.append(s)
                self.pila.append(5.1)
                self.pila.append("cerrarParentesis")
                e = Simbolo("E")
                self.pila.append(e)
                self.pila.append("abrirParentesis")
                self.pila.append("if")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: if", "")
            
            elif tv in firstB2:
                self.parse.append(6)
                self.pila.append(6.3)
                n = Simbolo("N")
                self.pila.append(n)
                self.pila.append(6.2)
                t = Simbolo("T")
                self.pila.append(t)
                id = Simbolo("id")
                self.pila.append(id)
                self.pila.append(6.1)
                self.pila.append("let")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: let", "")
            
            elif tv in firstB3:
                self.parse.append(7)
                self.pila.append(7.2)
                s = Simbolo("S")
                self.pila.append(s)
                self.pila.append(7.1)
            
            elif tv in firstB4:
                self.parse.append(8)
                self.pila.append(8.2)
                self.pila.append("cerrarCorchete")
                z = Simbolo("Z")
                self.pila.append(z)
                self.pila.append(8.1)
                self.pila.append("abrirCorchete")
                self.pila.append("cerrarParentesis")
                e = Simbolo("E")
                self.pila.append(e)
                self.pila.append("abrirParentesis")
                self.pila.append("switch")
            
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: switch", "")
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(102,f"ERROR SINTÁCTICO - El token {t} no pertenece al primer elemento de una sentencia válida", "")
            
    #----------------------------------------------------------------------------------------
        elif nT == "S":
            if tv in firstS1:
                self.parse.append(9)
                self.pila.append(9.3)
                self.pila.append("ptoComa")
                sp = Simbolo("S'")
                self.pila.append(sp)
                self.pila.append(9.2)
                id = Simbolo("id")
                self.pila.append(id)
                self.pila.append(9.1)
                
            elif tv in firstS2:
                self.parse.append(10)
                self.pila.append(10.1)
                self.pila.append("ptoComa")
                e = Simbolo("E")
                self.pila.append(e)
                self.pila.append("print")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: print", "")
            
            elif tv in firstS3:
                self.parse.append(11)
                self.pila.append(11.3)
                self.pila.append("ptoComa")
                self.pila.append(11.2)
                id = Simbolo("id")
                self.pila.append(id)
                self.pila.append(11.1)
                self.pila.append("input")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: input", "")
            
            elif tv in firstS4:
                self.parse.append(12)
                self.pila.append(12.1)
                self.pila.append("ptoComa")
                x = Simbolo("X")
                self.pila.append(x)
                self.pila.append("return")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: return", "")
            
            elif tv in firstS5:
                self.parse.append(13)
                self.pila.append(13.1)
                self.pila.append("ptoComa")
                self.pila.append("break")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: break", "")
            
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(103,f"ERROR SINTÁCTICO - Token {t} no pertenece al primer elemento de una sentencia simple válida", "")
            
                
    #----------------------------------------------------------------------------------------
        elif nT == "S'":
            if tv in firstSprima1:
                self.parse.append(14)
                self.pila.append(14.1)
                e = Simbolo("E")
                self.pila.append(e)
                self.pila.append("asignacion")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: =", "")
            
            elif tv in firstSprima2:
                self.parse.append(15)
                self.pila.append(15.1)
                e = Simbolo("E")
                self.pila.append(e)
                self.pila.append("asigMultiplicacion")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: *=", "")
            
            elif tv in firstSprima3:
                self.parse.append(16)
                self.pila.append(16.1)
                self.pila.append("cerrarParentesis")
                l = Simbolo("L")
                self.pila.append(l)
                self.pila.append("abrirParentesis")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: ( ", "")

            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(104,f"ERROR SINTÁCTICO - Token {t} no es una asignación válida o la llamada a una función", "")
            
    #----------------------------------------------------------------------------------------
        elif nT == "E":
            if tv in firstE1:
                self.parse.append(17)
                self.pila.append(17.1)
                ep = Simbolo("E'")
                self.pila.append(ep)
                r = Simbolo("R")
                self.pila.append(r)

            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(105,f"ERROR SINTÁCTICO - Token {t} no pertenece a una expresión válida", "")
            
    #----------------------------------------------------------------------------------------    
        elif nT == "E'":
            if tv in followEprima:
                self.parse.append(18)
                self.pila.append(18.1)           
            
            elif tv in firstEprima2:
                self.parse.append(19)
                self.pila.append(19.1)
                ep = Simbolo("E'")
                self.pila.append(ep)
                r = Simbolo("R")
                self.pila.append(r)
                self.pila.append("opLogico1")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: &&", "")  
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(106,f"ERROR SINTÁCTICO - Token {t} no pertenece a una expresión lógica u otra expresión válida", "")
                
    #---------------------------------------------------------------------------------------   
        elif nT == "R":
            if tv in firstR1:
                self.parse.append(20)
                self.pila.append(20.1)
                rp = Simbolo("R'")
                self.pila.append(rp)
                u = Simbolo("U")
                self.pila.append(u)
                
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(107,f"ERROR SINTÁCTICO - Token {t} no pertenece a una expresión válida", "")          

    #----------------------------------------------------------------------------------------             
        elif nT == "R'":
            if tv in followRprima:
                self.parse.append(21)
                self.pila.append(21.1)
            
            elif tv in firstRprima2:
                self.parse.append(22)
                self.pila.append(22.1)
                rp = Simbolo("R'")
                self.pila.append(rp)
                u = Simbolo("U")
                self.pila.append(u)
                self.pila.append("opRelacional1")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: ==", "")
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(108,f"ERROR SINTÁCTICO - Token {t} no pertenece a una expresión relacional u otra expresión válida", "")
                          
    #-----------------------------------------------------------------------------------------
        elif nT == "U":
            if tv in firstU1:
                self.parse.append(23)
                self.pila.append(23.1)
                up = Simbolo("U'")
                self.pila.append(up)
                v = Simbolo("V")
                self.pila.append(v)
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(109,f"ERROR SINTÁCTICO - Token {t} no pertenece a una expresión válida", "")
    
    
    
    #----------------------------------------------------------------------------------------- 
        elif nT == "U'":
            if tv in followUprima:
                self.parse.append(24)
                self.pila.append(24.1)
            
            elif tv in firstUprima2:
                self.parse.append(25)
                self.pila.append(25.1)
                up = Simbolo("U'")
                self.pila.append(up)
                v = Simbolo("V")
                self.pila.append(v)
                self.pila.append("opAritmetico2")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: +", "")

            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(110,f"ERROR SINTÁCTICO - Token {t} no pertenece a una expresión aritmética de suma u otra expresión válida", "")
    
    #-----------------------------------------------------------------------------------------
        elif nT == "V":
            if tv in firstV1:
                self.parse.append(26)
                self.pila.append(26.1)
                vp = Simbolo("V'")
                self.pila.append(vp)
                p = Simbolo("P")
                self.pila.append(p)
                
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(111,f"ERROR SINTÁCTICO - Token {t} no pertenece a una expresión válida", "")
        
    #-----------------------------------------------------------------------------------------
        elif nT == "V'":
            if tv in followVprima:
                self.parse.append(27)
                self.pila.append(27.1)
            
            elif tv in firstVprima2:
                self.parse.append(28)
                self.pila.append(28.1)
                vp = Simbolo("V'")
                self.pila.append(vp)
                p = Simbolo("P")
                self.pila.append(p)
                self.pila.append("opAritmetico1")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: *", "")

            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(112,f"ERROR SINTÁCTICO - Token {t} no pertenece a una expresión aritmética de multiplicacion u otra expresión válida", "")
        
    #-----------------------------------------------------------------------------------------   
        elif nT == "P":
            if tv in firstP1:
                self.parse.append(29)
                self.pila.append(29.3)
                pp = Simbolo("P'")
                self.pila.append(pp)
                self.pila.append(29.2)
                id = Simbolo("id")
                self.pila.append(id)
                self.pila.append(29.1)
            
            elif tv in firstP2:
                self.parse.append(30)
                self.pila.append(30.1)
                self.pila.append("cerrarParentesis")
                e = Simbolo("E")
                self.pila.append(e)
                self.pila.append("abrirParentesis")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: ( ", "")

            elif tv in firstP3:
                self.parse.append(31)
                self.pila.append(31.1)
                self.pila.append("cteEntera")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba una constante entera", "")


            elif tv in firstP4:
                self.parse.append(32)
                self.pila.append(32.1)
                self.pila.append("cadena")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba una cadena", "")

            elif tv in firstP5:
                self.parse.append(33)
                self.pila.append(33.1)
                self.pila.append("true")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: true", "")

            elif tv in firstP6:
                self.parse.append(34)
                self.pila.append(34.1)
                self.pila.append("false")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: false", "")

            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(113,f"ERROR SINTÁCTICO - Token {t} no pertenece a una expresión válida", "")
        
    #-----------------------------------------------------------------------------------------               
        elif nT == "P'":
            if tv in followPprima:
                self.parse.append(35)
                self.pila.append(35.1)

            elif tv in firstPprima2:
                self.parse.append(36)
                self.pila.append(36.1)
                self.pila.append("cerrarParentesis")
                l = Simbolo("L")
                self.pila.append(l)
                self.pila.append("abrirParentesis")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: (", "")

            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(114,f"ERROR SINTÁCTICO - Token {t} no es un identificador de variable o la llamada a una función", "")
        
    #-----------------------------------------------------------------------------------------   
        elif nT == "L":
            if tv in firstL1:
                self.parse.append(37)
                self.pila.append(37.1)
                q = Simbolo("Q")
                self.pila.append(q)
                e = Simbolo("E")
                self.pila.append(e)
            
            elif tv in followL:
                self.parse.append(38)
                self.pila.append(38.1)
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(115,f"ERROR SINTÁCTICO - Token {t} no es un argumento de función válido porque no pertenece a una expresión válida", "")
            
    #-----------------------------------------------------------------------------------------               
        elif nT == "Q":
            if tv in firstQ1:
                self.parse.append(39)
                self.pila.append(39.1)
                q = Simbolo("Q")
                self.pila.append(q)
                e = Simbolo("E")
                self.pila.append(e)
                self.pila.append("coma")
                 
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                    
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: ,", "")

            elif tv in followQ:
                self.parse.append(40)
                self.pila.append(40.1)
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(116,f"ERROR SINTÁCTICO - Token {t} de función válido porque no pertenece a una expresión válida", "")
            
    #-----------------------------------------------------------------------------------------   
        elif nT == "X":
            if tv in firstX1:
                self.parse.append(41)
                self.pila.append(41.1)
                e = Simbolo("E")
                self.pila.append(e)
            
            elif tv in followX:
                self.parse.append(42)
                self.pila.append(42.1)
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(117,f"ERROR SINTÁCTICO - Token {t} no es un valor de retorno de función válido porque no pertenece a una expresión válida", "")
            
    #-----------------------------------------------------------------------------------------               
        elif nT == "T":
            if tv in firstT1:
                self.parse.append(43)
                self.pila.append(43.1)
                self.pila.append("int")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: int", "")
            
            elif tv in firstT2:
                self.parse.append(44)
                self.pila.append(44.1)
                self.pila.append("boolean")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: boolean", "")
             
            elif tv in firstT3:
                self.parse.append(45)
                self.pila.append(45.1)
                self.pila.append("string")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: string", "")
                 
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(118,f"ERROR SINTÁCTICO - Token {t} no es un tipo de variable válido", "")         
    
    #-----------------------------------------------------------------------------------------   
        elif nT == "F":
            if tv in firstF1:
                self.parse.append(46)
                self.pila.append(46.4)
                self.pila.append("cerrarCorchete")
                c = Simbolo("C")
                self.pila.append(c)
                self.pila.append("abrirCorchete")
                self.pila.append(46.3)
                self.pila.append("cerrarParentesis")
                d = Simbolo("D")
                self.pila.append(d)
                self.pila.append("abrirParentesis")
                h = Simbolo("H")
                self.pila.append(h)
                self.pila.append(46.2)
                id = Simbolo("id")
                self.pila.append(id)
                self.pila.append(46.1)
                self.pila.append("function")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: function", "")      
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(119,f"ERROR SINTÁCTICO - Token {t} no pertenece a una declaración válida de una función", "")         
    
    #-----------------------------------------------------------------------------------------               
        elif nT == "H":
            if tv in firstH1:
                self.parse.append(47)
                self.pila.append(47.1)
                t = Simbolo("T")
                self.pila.append(t)
            
            elif tv in followH:
                self.parse.append(48)
                self.pila.append(48.1)
                
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(120,f"ERROR SINTÁCTICO - Token {t} no es un tipo de valor de retorno de función válido", "")         
    
    #-----------------------------------------------------------------------------------------   
        elif nT == "D":
            if tv in firstD1:
                self.parse.append(49)
                self.pila.append(49.1)
                k = Simbolo("K")
                self.pila.append(k)
                id = Simbolo("id")
                self.pila.append(id)
                t = Simbolo("T")
                self.pila.append(t)
            
            elif tv in followD:
                self.parse.append(50)
                self.pila.append(50.1)
                
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(121,f"ERROR SINTÁCTICO - Token {t} no es una declaración válida de un argumento de una función", "")         
    
    #-----------------------------------------------------------------------------------------               
        elif nT == "K":
            if tv in firstK1:
                self.parse.append(51)
                self.pila.append(51.1)
                k = Simbolo("K")
                self.pila.append(k)
                id = Simbolo("id")
                self.pila.append(id)
                t = Simbolo("T")
                self.pila.append(t)
                self.pila.append("coma")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: ,", "")
            
            elif tv in followK:
                self.parse.append(52)
                self.pila.append(52.1)
                
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(122,f"ERROR SINTÁCTICO - Token {t} no es una declaración válida de un argumento de una función", "")         
    
    #-----------------------------------------------------------------------------------------   
        elif nT == "C":
            if tv in firstC1:
                self.parse.append(53)
                self.pila.append(53.2)
                cp = Simbolo("C'")
                self.pila.append(cp)
                b = Simbolo("B")
                self.pila.append(b)
                self.pila.append(53.1)
                    
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(123,f"ERROR SINTÁCTICO - Token {t} no pertenece a una sentencia válida", "")         
    
        
    #-----------------------------------------------------------------------------------------  
        elif nT == "C'":
            if tv in firstC1prima:
                self.parse.append(54)
                self.pila.append(54.2)
                cp = Simbolo("C'")
                self.pila.append(cp)
                b = Simbolo("B")
                self.pila.append(b)
                self.pila.append(54.1)
                
            elif tv in followCprima:
                self.parse.append(55)
                self.pila.append(55.1)
                
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(124,f"ERROR SINTÁCTICO - Token {t} no pertenece a una sentencia válida", "")         
    
        
    #-----------------------------------------------------------------------------------------              
        elif nT == "N":
            if tv in firstN1:
                self.parse.append(56)
                self.pila.append(56.1)
                self.pila.append("ptoComa")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: ;", "")
                
            elif tv in firstN2:
                self.parse.append(57)
                self.pila.append(57.1)
                self.pila.append("ptoComa")
                e = Simbolo("E")
                self.pila.append(e)
                self.pila.append("asignacion")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: =", "")
                
            elif tv in firstN3:
                self.parse.append(58)
                self.pila.append(58.1)
                self.pila.append("ptoComa")
                e = Simbolo("E")
                self.pila.append(e)
                self.pila.append("asigMultiplicacion")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                    
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba *=", "")
                
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(125,f"ERROR SINTÁCTICO - Token {t} no es una asignación válida", "")         
    
    #-----------------------------------------------------------------------------------------   
        elif nT == "Z":
            if tv in firstZ1:
                self.parse.append(59)
                self.pila.append(59.3)
                zp = Simbolo("Z'")
                self.pila.append(zp)
                self.pila.append(59.2)
                o = Simbolo("O")
                self.pila.append(o)
                self.pila.append(59.1)
                self.pila.append("dosPuntos")
                self.pila.append("cteEntera")
                self.pila.append("case")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: case", "")  
            
            elif tv in firstZ2:
                self.parse.append(60)
                self.pila.append(60.2)
                o = Simbolo("O")
                self.pila.append(o)
                self.pila.append(60.1)
                self.pila.append("dosPuntos")
                self.pila.append("default")
                
                if(self.pila.equipara(tv)):
                    pedirToken=True
                    ts = Simbolo(tv)
                    self.aux.append(ts)
                else:
                    if t in tokenOp:
                        t = convertirOp[tokenOp.index(t)]
                    error=Error(100,f"ERROR SINTÁCTICO - Token {t} no esperado. Se esperaba: case", "")  
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(126,f"ERROR SINTÁCTICO - Token {t} no es un cuerpo válido para la condicional múltiple switch", "")         
    
    #-----------------------------------------------------------------------------------------               
        elif nT == "O":
            if tv in firstO1:
                self.parse.append(61)
                self.pila.append(61.3)
                op = Simbolo("O")
                self.pila.append(op)
                self.pila.append(61.2) 
                b = Simbolo("B") 
                self.pila.append(b)
                self.pila.append(61.1) 
            
            elif tv in followO:
                self.parse.append(62)
                self.pila.append(62.1)
                
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(127,f"ERROR SINTÁCTICO - Token {t} no pertenece a una sentencia válida", "")         
            
    #-----------------------------------------------------------------------------------------   
        elif nT == "Z'":
            if tv in firstZprima1:
                self.parse.append(63)
                self.pila.append(63.2)
                z = Simbolo("Z")
                self.pila.append(z)
                self.pila.append(63.1)
            
            elif tv in followZprima:
                self.parse.append(64)
                self.pila.append(64.1)
            
            else:
                if t in tokenOp:
                    t = convertirOp[tokenOp.index(t)]
                error=Error(128,f"ERROR SINTÁCTICO - Token {t} no pertenece a una sentencia válida", "")         
                 
    #-----------------------------------------------------------------------------------------               
        return pedirToken,error