from TablaSimbolos.EntradaTS import Tipo
from objetosGenerales.GestorError import Error


class VarAnalizadorSemantico():
    def __init__(self,n,v):
        self.nombre=n
        self.valor=v

def compararListas(l1,l2):
    res = True
    i = 0
    len1 = 0
    len2 = 0
    if type(l1) is list:
        len1 = len(l1)
    else:
        len1=1
    
    if type(l2) is list:
        len2 = len(l2)
    else:
        len2=1
    
    if(len1 == len2 and len1>1): # comparar los elementos de ambas listas
        for l in l1:
            if(l != l2[i]):
                res = False
            i+=1
    elif(len1 == len2 and len1==1): # comparar cuando la cant de elementos que contienen es 1
        if type(l1) is list:      # l1 es una lista
            if l2 is list:      # l2 es una lista
                if l1[0] != l2[0]:
                   res = False
            else:               # l2 NO es una lista
                if l1[0] != l2:
                    res = False
        else:               # l1 NO es una lista
            if type(l2) is list:      # l2 es una lista
                if l1 != l2[0]:
                   res = False
            else:
                if l1 != l2:    # l2 NO es una lista
                    res = False      
    else:
        res = False
    return res

def getTipoString(listaTipos):
    valor = ""
    resp=""
    if type(listaTipos) is list:
        l = len(listaTipos)
    else:
        l=1
    i=0
    if l > 1:
        for tipo in listaTipos:
            valor = tipo.split("_")
            resp += valor[len(valor) - 1]
            i+=1
            if(i<l):
                resp += " x "
    else:
        valor = listaTipos.split("_")

        resp += valor[len(valor) - 1]
    return resp

def accionesAnalizadorSemantico(a,zona,dec_impl,gestorTS,pila,aux):
    error = False
    
    # ------------------ 1 ------------------------
    
    if a == 1.1:
        # Creacion Tabla Global
        gestorTS.crearTabla()
    
    elif a == 1.2:
        # Liberacion Tabla Global
        gestorTS.removeTable()
    
    # ----------------- 5 --------------------------
    
    elif a == 5.1:
        s = pila.getFromTope(0)
        b = aux.getFromTope(4)
        # S.funcion = B.funcion
        s.setValorAtributo("funcion",b.getValorAtributo("funcion"))
        s.setValorAtributo("switch",b.getValorAtributo("switch")) 
    
    elif a == 5.2:
        b = aux.getFromTope(5)
        s = aux.getFromTope(0)
        e = aux.getFromTope(2)
        
        if(e.getValorAtributo("tipo") == Tipo.LOGICO):
           b.setValorAtributo("tipo",s.getValorAtributo("tipo"))
        else:
            b.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(201,f"ERROR SEMÁNTICO - La expresión evaluada como condición no es de tipo lógico", "")

        b.setValorAtributo("tipoRet",s.getValorAtributo("tipoRet"))

        aux.pop() # S
        aux.pop() # cerrarParentesis
        aux.pop() # E
        aux.pop() # abrirParentesis
        aux.pop() # if
        #aux.pop() # B
        
    # --------------- 6 ----------------
    elif a == 6.1:
        zona = True
    
    elif a == 6.2:
        id =  aux.getFromTope(1)
        t = aux.getFromTope(0)
        gestorTS.insertarTipoTamTS(id.getValorAtributo("pos"),t.getValorAtributo("tipo"),t.getValorAtributo("tamanho"))   
        
        zona = False
            
    elif a == 6.3:
        
        b = aux.getFromTope(4)
        n = aux.getFromTope(0)
        id = aux.getFromTope(2)
        
        idTipo = gestorTS.buscarTipo(id.getValorAtributo("pos"))
        nTipo = n.getValorAtributo("tipo")
        
        if((nTipo == Tipo.VACIO) or ( idTipo == nTipo)):
            b.setValorAtributo("tipo",Tipo.OK)
        else:
            b.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(202,f"ERROR SEMÁNTICO - Se le debe asignar una expresión de tipo {getTipoString(idTipo)} al identificador. La expresión asignada es de tipo {getTipoString(nTipo)}", "") 
        
        aux.pop() # N
        aux.pop() # T
        aux.pop() # id
        aux.pop() # let
        #aux.pop() # B
    
    # -------------------- 7 ------------------
    elif a == 7.1:
        s = pila.getFromTope(0)
        b = aux.getFromTope(0)
        
        s.setValorAtributo("funcion",b.getValorAtributo("funcion"))
        s.setValorAtributo("switch",b.getValorAtributo("switch"))
    
    elif a == 7.2:
        
        s = aux.getFromTope(0)
        b = aux.getFromTope(1)
        
        b.setValorAtributo("tipo",s.getValorAtributo("tipo"))
        b.setValorAtributo("tipoRet",s.getValorAtributo("tipoRet"))
    
        aux.pop() # S
        #aux.pop() # B
        
    # ---------------- 8 ------------------
    elif a == 8.1:
        
        b = aux.getFromTope(5)
        z = pila.getFromTope(0)
        
        z.setValorAtributo("funcion",b.getValorAtributo("funcion"))
        z.setValorAtributo("switch",True)
        
    
    elif a == 8.2:
        
        e = aux.getFromTope(4)
        b = aux.getFromTope(7)
        z = aux.getFromTope(1)
        
        eTipo = e.getValorAtributo("tipo")
        zTipo = z.getValorAtributo("tipo")
        
        if(eTipo == Tipo.ENTERO):
            if (zTipo == Tipo.OK):
                b.setValorAtributo("tipo",Tipo.OK)
            else:
                b.setValorAtributo("tipo",Tipo.ERROR)
                error = Error(203,f"ERROR SEMÁNTICO - Existencia de sentencias no válidas en el cuerpo del switch", "")
        else:
            b.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(204,f"ERROR SEMÁNTICO - La expresión que se evalúa debe ser de tipo entero. La expresión es de tipo {getTipoString(uTipo)}", "")
        
        b.setValorAtributo("tipoRet",z.getValorAtributo("tipoRet"))
        
        aux.pop() # cerrarCorchete
        aux.pop() # Z
        aux.pop() # abrirCorchete
        aux.pop() # cerrarParentesis 
        aux.pop() # E
        aux.pop() # abrirParentesis 
        aux.pop() # switch
        #aux.pop() # B     
    
    
    # ------------------- 9 --------------------
    elif a == 9.1:
        dec_impl = True
    
    elif a == 9.2:
        
        id = aux.getFromTope(0)
        
        idPos= id.getValorAtributo("pos")
        
        idTipo = gestorTS.buscarTipo(idPos)
        
        if(idTipo == False or idTipo == Tipo.UNDEFINED):
            gestorTS.insertarTipoTamTS(idPos, Tipo.ENTERO, 2)  
        
        dec_impl = False
          
    elif a == 9.3:
        
        s = aux.getFromTope(3)
        id = aux.getFromTope(2)
        sprima = aux.getFromTope(1)
        
        idPos = id.getValorAtributo("pos")
        idTipo = gestorTS.buscarTipo(idPos)
        
        if(idTipo == Tipo.FUNCION):
            if(compararListas(gestorTS.buscarTipoParametros(idPos), sprima.getValorAtributo("tipo"))):
                s.setValorAtributo("tipo",Tipo.OK)
            else:
                idTipoPar = gestorTS.buscarTipoParametros(idPos)
                sprimaTipo = sprima.getValorAtributo("tipo")
                
                s.setValorAtributo("tipo",Tipo.ERROR)
                error = Error(205,f"ERROR SEMÁNTICO - Los parámetros pasados a la función deben ser de tipo {getTipoString(idTipoPar)}. Los parámetros pasados son de tipo {getTipoString(sprimaTipo)}", "")
                
        elif(idTipo == sprima.getValorAtributo("tipo")):
            s.setValorAtributo("tipo",Tipo.OK)
        else:
            sprimaTipo = sprima.getValorAtributo("tipo")
            s.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(206,f"ERROR SEMÁNTICO - La expresión asignada al identificador es de tipo {getTipoString(sprimaTipo)} cuando debe ser el mismo tipo que este ( {getTipoString(idTipo)} )", "")
        
        aux.pop() # ptoComa
        aux.pop() # S'
        aux.pop() # id 

    # -------------------- 10 ----------------
    elif a == 10.1:
        s = aux.getFromTope(3)
        e = aux.getFromTope(1)
        
        eTipo = e.getValorAtributo("tipo")
        
        if (eTipo == Tipo.ENTERO or eTipo == Tipo.CADENA):
            s.setValorAtributo("tipo",Tipo.OK)
        elif(eTipo == Tipo.FUNCION):
            idPos = e.getValorAtributo("pos") 
            idTD = gestorTS.buscarTipoDevuelto(idPos)
            if(idTD == Tipo.ENTERO or idTD == Tipo.CADENA):
                s.setValorAtributo("tipo",Tipo.OK)
            else:
                s.setValorAtributo("tipo",Tipo.ERROR)
                error = Error(207,f"ERROR SEMÁNTICO - La expresión a 'imprimir' debe ser una cadena o un entero", "") 
        else:
            s.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(207,f"ERROR SEMÁNTICO - La expresión a 'imprimir' debe ser una cadena o un entero", "")
            
        aux.pop() # ptoComa
        aux.pop() # E
        aux.pop() # print 
    
    # ------------------ 11 -----------------
    elif a == 11.1:
        dec_impl = True

    elif a == 11.2:
        
        id = aux.getFromTope(0)
        
        idPos= id.getValorAtributo("pos")
        idTipo = gestorTS.buscarTipo(idPos)
        
        if(idTipo == False or idTipo == Tipo.UNDEFINED):
            gestorTS.insertarTipoTamTS(idPos, Tipo.ENTERO, 2) 
             
        dec_impl = False
    
    elif a == 11.3:
        
        s = aux.getFromTope(3)
        id = aux.getFromTope(1)
        
        idPos = id.getValorAtributo("pos")
        idTipo = gestorTS.buscarTipo(idPos)
        
        if(idTipo == Tipo.ENTERO or idTipo == Tipo.CADENA):
            s.setValorAtributo("tipo",Tipo.OK) 
        else:
            s.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(208,f"ERROR SEMÁNTICO - El identificador debe ser una cadena o un entero", "")
        
        aux.pop() # ptoComa
        aux.pop() # id
        aux.pop() # input   
              
    # ----------- 12 ------------
    elif a == 12.1:
        s = aux.getFromTope(3)
        x = aux.getFromTope(1)
        
        xTipo = x.getValorAtributo("tipo")
        
        if(xTipo != Tipo.ERROR):
            if s.getValorAtributo("funcion"):
                s.setValorAtributo("tipo", Tipo.OK)
                s.setValorAtributo("tipoRet", xTipo)
                
            else:
                s.setValorAtributo("tipo", Tipo.ERROR)
                error = Error(209,f"ERROR SEMÁNTICO - La sentencia return solo puede ser declarada en el cuerpo de una función", "")
        else:         
            s.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(210,f"ERROR SEMÁNTICO - La expresión de retorno es incorrecta", "")

        
        
        aux.pop() # ptoComa
        aux.pop() # X
        aux.pop() # return
    
    # --------------- 13 ----------------
    elif a == 13.1:
        s = aux.getFromTope(2)

        sSwt = s.getValorAtributo("switch")
        
        if sSwt:
            s.setValorAtributo("tipo", Tipo.OK)
        else:
            s.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(211,f"ERROR SEMÁNTICO - La sentencia BREAK solo puede declararse dentro del CASE O DEFAULT de un SWITCH", "")
        
        aux.pop() # ptoComa
        aux.pop() # break

    # --------------- 14 ----------------
    elif a == 14.1:
        
        sprima = aux.getFromTope(2)
        e = aux.getFromTope(0)
        
        sprima.setValorAtributo("tipo", e.getValorAtributo("tipo"))
        
        aux.pop() # =
        aux.pop() # E
    
    # -------------- 15 ------------------
    elif a == 15.1:
        
        sprima = aux.getFromTope(2)
        e = aux.getFromTope(0)
        
        if(e.getValorAtributo("tipo") == Tipo.ENTERO):
            sprima.setValorAtributo("tipo", Tipo.ENTERO)
        else:
            sprima.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(212,f"ERROR SEMÁNTICO - La expresión debe ser de tipo entero", "")

        aux.pop() # *=
        aux.pop() # E
    
    # ----------------- 16 -----------------
    elif a == 16.1:
        
        sprima = aux.getFromTope(3)
        l = aux.getFromTope(1)
        
        sprima.setValorAtributo("tipo", l.getValorAtributo("tipo"))
        
        aux.pop() # cerrarParentesis
        aux.pop() # L
        aux.pop() # abrirParentesis
        
    # --------------- 17 -----------------
    elif a == 17.1:
        
        e = aux.getFromTope(2)
        r = aux.getFromTope(1)
        eprima = aux.getFromTope(0)
        
        rTipo = r.getValorAtributo("tipo")
        eprimaTipo = eprima.getValorAtributo("tipo")
        
        if(rTipo == eprimaTipo or eprimaTipo == Tipo.VACIO):
            e.setValorAtributo("tipo", rTipo)
        else:
            e.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(213,f"ERROR SEMÁNTICO - Las expresiones son de tipos diferentes", "")
        
        aux.pop() # E'
        aux.pop() # R
        
    # --------------- 18 -------------------
    elif a == 18.1:
        
        eprima = aux.getFromTope(0)
        
        eprima.setValorAtributo("tipo", Tipo.VACIO)
    
    # --------------- 19 ---------------------
    elif a == 19.1:
       
        eprima = aux.getFromTope(3)
        eprima1 = aux.getFromTope(0)
        r = aux.getFromTope(1)
       
        rTipo = r.getValorAtributo("tipo")
        ep1Tipo = eprima1.getValorAtributo("tipo")
        
        if(rTipo == Tipo.LOGICO and (ep1Tipo == Tipo.LOGICO or ep1Tipo == Tipo.VACIO)):
            r.setValorAtributo("tipo", rTipo)
        else:
            r.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(214,f"ERROR SEMÁNTICO - La expresión debe ser de tipo lógico", "")

        aux.pop() # E'1
        aux.pop() # R
        aux.pop() # &&
        
    # ---------------- 20 ----------------
    elif a == 20.1:

        rprima = aux.getFromTope(0)
        u = aux.getFromTope(1)
        r = aux.getFromTope(2)
       
        rprimaTipo = rprima.getValorAtributo("tipo")
        uTipo = u.getValorAtributo("tipo")
        
        if(rprimaTipo == uTipo  and rprimaTipo != Tipo.ERROR):
            r.setValorAtributo("tipo", Tipo.LOGICO)
        elif(rprimaTipo == Tipo.VACIO and uTipo != Tipo.ERROR):
            r.setValorAtributo("tipo", uTipo)
        else:
            r.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(215,f"ERROR SEMÁNTICO - Las expresiones son de tipos diferentes", "")

        aux.pop() # R'
        aux.pop() # U
    
    # ------------- 21 ---------   
    elif a == 21.1:
        
        rprima = aux.getFromTope(0)
        
        rprima.setValorAtributo("tipo", Tipo.VACIO)
    
    # ----------- 22 ---------------
    elif a == 22.1:

        rprima = aux.getFromTope(3)
        u = aux.getFromTope(1)
        rprima1 = aux.getFromTope(0)
       
        rprima1Tipo = rprima1.getValorAtributo("tipo")
        uTipo = u.getValorAtributo("tipo")
        
        if((rprima1Tipo == uTipo or (rprima1Tipo == Tipo.VACIO)) and rprima1Tipo != Tipo.ERROR and uTipo != Tipo.ERROR):
            rprima.setValorAtributo("tipo", uTipo)
        else:
            rprima.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(216,f"ERROR SEMÁNTICO - Las expresiones son de tipos diferentes", "")

        aux.pop() # R'1
        aux.pop() # U
        aux.pop() # ==
        
    # --------------- 23 -------------
    elif a == 23.1:
        
        uprima = aux.getFromTope(0)
        v = aux.getFromTope(1)
        u = aux.getFromTope(2)
       
        uprimaTipo = uprima.getValorAtributo("tipo")
        vTipo = v.getValorAtributo("tipo")
        
        if((vTipo == uprimaTipo or (uprimaTipo == Tipo.VACIO)) and uprimaTipo != Tipo.ERROR and vTipo != Tipo.ERROR):
            u.setValorAtributo("tipo", vTipo)
        else:
            u.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(217,f"ERROR SEMÁNTICO - Las expresiones son de tipos diferentes", "")

        aux.pop() # U'
        aux.pop() # V
        
    # ------------- 24 --------------
    elif a == 24.1:
        
        uprima = aux.getFromTope(0)
        
        uprima.setValorAtributo("tipo", Tipo.VACIO)
    
    # ------------ 25 ---------------
    elif a == 25.1:
        
        v = aux.getFromTope(1)
        uprima1 = aux.getFromTope(0)
        uprima = aux.getFromTope(3)

        vTipo = v.getValorAtributo("tipo")
        u1Tipo = uprima1.getValorAtributo("tipo")
        
        if((vTipo == Tipo.ENTERO and ( u1Tipo == Tipo.VACIO or u1Tipo == Tipo.ENTERO)) and u1Tipo != Tipo.ERROR and vTipo != Tipo.ERROR):
            uprima.setValorAtributo("tipo", vTipo)
        else:
            uprima.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(218,f"ERROR SEMÁNTICO - Las expresiones no son de tipo entero", "")

        aux.pop() # U'1
        aux.pop() # V  
        aux.pop() # +
    
    # --------------- 26 -------------------      
    elif a == 26.1:
        
        vprima = aux.getFromTope(0)
        v = aux.getFromTope(2)
        p = aux.getFromTope(1)
       
        vprimaTipo = vprima.getValorAtributo("tipo")
        pTipo = p.getValorAtributo("tipo")
        
        if((pTipo == vprimaTipo or (vprimaTipo == Tipo.VACIO)) and vprimaTipo != Tipo.ERROR and pTipo != Tipo.ERROR):
            v.setValorAtributo("tipo", pTipo)
        else:
            v.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(219,f"ERROR SEMÁNTICO - Las expresiones son de tipos diferentes", "")

        aux.pop() # V'
        aux.pop() # P
        
    # ------------- 27 --------------
    elif a == 27.1:
        
        vprima = aux.getFromTope(0)
        
        vprima.setValorAtributo("tipo", Tipo.VACIO)

    # --------------- 28 -------------------      
    elif a == 28.1:
        
        vprima1 = aux.getFromTope(0)
        vprima = aux.getFromTope(2)
        p = aux.getFromTope(1)
       
        vprima1Tipo = vprima1.getValorAtributo("tipo")
        pTipo = p.getValorAtributo("tipo")
        
        if((pTipo == Tipo.ENTERO and ( vprima1Tipo == Tipo.VACIO or vprima1Tipo == Tipo.ENTERO)) and vprima1Tipo != Tipo.ERROR and pTipo != Tipo.ERROR):
            vprima.setValorAtributo("tipo", pTipo)
        else:
            vprima.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(220,f"ERROR SEMÁNTICO - Las expresiones no son de tipo entero", "")

        aux.pop() # V'1
        aux.pop() # P
        aux.pop() # *
    
    # --------------- 29 -----------------
    elif a == 29.1:
        dec_impl = True

    elif a == 29.2:
        
        id = aux.getFromTope(0)
        
        idPos= id.getValorAtributo("pos")
        idTipo = gestorTS.buscarTipo(idPos)
        
        if(idTipo == False or idTipo == Tipo.UNDEFINED):
            gestorTS.insertarTipoTamTS(idPos, Tipo.ENTERO, 2)  
        
        dec_impl = False
    
    elif a == 29.3:
        
        pprima = aux.getFromTope(0)
        id = aux.getFromTope(1)
        p = aux.getFromTope(2)
        
        idPos = id.getValorAtributo("pos")
        pprimaTipo = pprima.getValorAtributo("tipo")
        idTipo = gestorTS.buscarTipo(idPos)
        pprimaFuncion = pprima.getValorAtributo("esfuncion")
        
        if(idTipo == Tipo.FUNCION):
            if(compararListas(gestorTS.buscarTipoParametros(idPos), pprimaTipo)):
                idTD = gestorTS.buscarTipoDevuelto(idPos)
                p.setValorAtributo("tipo", idTD)
            else:
                idTipoPar = gestorTS.buscarTipoDevuelto(idPos)
                p.setValorAtributo("tipo", Tipo.ERROR)
                error = Error(221,f"ERROR SEMÁNTICO - Los parámetros pasados a la función deben ser de tipo {getTipoString(idTipoPar)}. Los parámetros pasados son de tipo {getTipoString(pprimaTipo)}", "")
        elif(pprimaTipo == Tipo.VACIO and pprimaFuncion == False):
            p.setValorAtributo("tipo", idTipo)
        else:
            p.setValorAtributo("tipo", Tipo.ERROR)
            id = gestorTS.buscarEntradaPorID(idPos)
            idLexema = id.getLexema()
            error = Error(222,f"ERROR SEMÁNTICO - El identificador ${idLexema} no fue declarado como una función", "")
          
        aux.pop() # P'
        aux.pop() # id
        
    # ----------------- 30 ----------------------
    elif a == 30.1:
        
        p = aux.getFromTope(3)
        e = aux.getFromTope(1)
        
        p.setValorAtributo("tipo", e.getValorAtributo("tipo")) 
    
        aux.pop() # cerrarParentesis
        aux.pop() # E
        aux.pop() # abrirParentesis
    
    # ----------------- 31 ----------------------
    elif a == 31.1:
        
        p = aux.getFromTope(1)
        
        p.setValorAtributo("tipo", Tipo.ENTERO) 
    
        aux.pop() # cteEntera

    # ----------------- 32 ----------------------
    elif a == 32.1:
        
        p = aux.getFromTope(1)
        
        p.setValorAtributo("tipo", Tipo.CADENA) 
    
        aux.pop() # cadena
    
    # ----------------- 33 ----------------------
    elif a == 33.1:
        
        p = aux.getFromTope(1)
        
        p.setValorAtributo("tipo", Tipo.LOGICO) 
    
        aux.pop() # true

    # ----------------- 34 ----------------------
    elif a == 34.1:
        
        p = aux.getFromTope(1)
        
        p.setValorAtributo("tipo", Tipo.LOGICO) 
    
        aux.pop() # false
    
    # ----------------- 35 ----------------------
    elif a == 35.1:
        
        pprima = aux.getFromTope(0)
        
        pprima.setValorAtributo("tipo", Tipo.VACIO)
        pprima.setValorAtributo("esfuncion", False) 
    
    # ----------------- 36 ----------------------
    elif a == 36.1:
        
        pprima = aux.getFromTope(3)
        l = aux.getFromTope(1)
        
        pprima.setValorAtributo("tipo", l.getValorAtributo("tipo")) 
        pprima.setValorAtributo("esfuncion", True)
        
        aux.pop() # cerrarParenetesis
        aux.pop() # L
        aux.pop() # abrirParentesis    
    
    # ---------------- 37 --------------------------
    elif a == 37.1:
        
        q = aux.getFromTope(0)
        e = aux.getFromTope(1)
        l = aux.getFromTope(2)
        
        qTipo = q.getValorAtributo("tipo")
        eTipo = e.getValorAtributo("tipo")
        if(qTipo != Tipo.VACIO and qTipo != Tipo.ERROR):
            if(eTipo != Tipo.ERROR):
                lTipo = [eTipo]
                for qt in qTipo:
                    lTipo.append(qt)
                l.setValorAtributo("tipo",lTipo)
            else:
                l.setValorAtributo("tipo", Tipo.ERROR)
                error = Error(223,f"ERROR SEMÁNTICO - Expresión incorrecta en el primer argumento de la llamada a la función", "")
        
        elif(eTipo != Tipo.ERROR and qTipo != Tipo.ERROR):
            lTipo = [eTipo]
            l.setValorAtributo("tipo",lTipo)
        
        else:
            l.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(224,f"ERROR SEMÁNTICO - Expresión incorrecta en los argumentos de la llamada a la función", "")
    
        aux.pop() # Q
        aux.pop() # E

    # ----------------- 38 ----------------------
    elif a == 38.1:
        
        l = aux.getFromTope(0)
        
        l.setValorAtributo("tipo", Tipo.VACIO)
        
    # ---------------- 39 --------------------------
    elif a == 39.1:
        
        q = aux.getFromTope(3)
        e = aux.getFromTope(1)
        q1 = aux.getFromTope(0)
        
        q1Tipo = q1.getValorAtributo("tipo")
        eTipo = e.getValorAtributo("tipo")
        
        if(q1Tipo != Tipo.VACIO and q1Tipo != Tipo.ERROR):
            if(eTipo != Tipo.ERROR):
                qTipo = [eTipo]
                for qt in q1Tipo:
                    qTipo.append(qt)
                q.setValorAtributo("tipo",qTipo)
            else:
                q.setValorAtributo("tipo", Tipo.ERROR)
                error = Error(224,f"ERROR SEMÁNTICO - Expresión incorrecta en los argumentos de la llamada a la función", "")
        
        elif(eTipo != Tipo.ERROR and q1Tipo != Tipo.ERROR):
            qTipo = [eTipo]
            q.setValorAtributo("tipo",qTipo)
        
        else:
            q.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(224,f"ERROR SEMÁNTICO - Expresión incorrecta en los argumentos de la llamada a la función", "")
    
        aux.pop() # Q
        aux.pop() # E
        aux.pop() # coma

    # ----------------- 40 ----------------------
    elif a == 40.1:
        
        q = aux.getFromTope(0)
        
        q.setValorAtributo("tipo", Tipo.VACIO)
    
    # ----------------- 41 ---------------------
    elif a == 41.1:
        x = aux.getFromTope(1)
        e = aux.getFromTope(0)
        
        x.setValorAtributo("tipo", e.getValorAtributo("tipo"))
        

        aux.pop() # E
    
    # ---------------- 42 --------------------
    elif a == 42.1:

        x = aux.getFromTope(0)
        
        x.setValorAtributo("tipo", Tipo.VACIO)
    
    # --------------- 43 ----------------------
    elif a == 43.1:
        
        t = aux.getFromTope(1)
        
        t.setValorAtributo("tipo",Tipo.ENTERO)
        t.setValorAtributo("tamanho",2)
        
        aux.pop() # int      

    # --------------- 44 ----------------------
    elif a == 44.1:
        
        t = aux.getFromTope(1)
        
        t.setValorAtributo("tipo",Tipo.LOGICO)
        t.setValorAtributo("tamanho",2)
        
        aux.pop() # boolean   

    # --------------- 45 ----------------------
    elif a == 45.1:
        
        t = aux.getFromTope(1)
        
        t.setValorAtributo("tipo",Tipo.CADENA)
        t.setValorAtributo("tamanho",128)
        
        aux.pop() # string
    
    # ------------- 46 ------------------------
    elif a == 46.1:
        zona = True
    
    elif a == 46.2:
        # Creacion Tabla Local
        gestorTS.crearTabla()
    
    elif a == 46.3:
        
        id = aux.getFromTope(4)
        d = aux.getFromTope(1)
        h = aux.getFromTope(3)
        
        idPos = id.getValorAtributo("pos")
        dTipo = d.getValorAtributo("tipo")
        hTipo = h.getValorAtributo("tipo") 
        
        gestorTS.insertarTipoTamTS(idPos, Tipo.FUNCION, False)
        gestorTS.insertarTipoParametros(idPos,dTipo)
        gestorTS.insertarTipoDevuelto(idPos,hTipo)
        
        zona = False
        
    elif a == 46.4:
        c = aux.getFromTope(1)
        h = aux.getFromTope(6)
        
        cTipoRet = c.getValorAtributo("tipoRet")
        hTipo = h.getValorAtributo("tipo")
        
        if(cTipoRet != hTipo):
            if(cTipoRet == None and hTipo != Tipo.VACIO):
                error = Error(225,f"ERROR SEMÁNTICO - El tipo del valor de retorno {getTipoString(cTipoRet)} no coincide con el tipo valor de retorno declarado {getTipoString(hTipo)}", "") 
        # Liberacion Tabla Local
        gestorTS.removeTable()
    
        aux.pop() # cerrarCorchete
        aux.pop() # C
        aux.pop() # abrirCorchete
        aux.pop() # cerrarParentesis
        aux.pop() # D
        aux.pop() # abrirParentesis
        aux.pop() # H
        aux.pop() # id
        aux.pop() # function
    
    # --------------- 47 ------------------ 
    elif a == 47.1:

        t = aux.getFromTope(0)
        h = aux.getFromTope(1)
        
        tTipo = t.getValorAtributo("tipo")
        
        h.setValorAtributo("tipo", tTipo)
        
        aux.pop() # T
        
    # --------------- 48 -----------------
    elif a == 48.1:

        h = aux.getFromTope(0)
        
        h.setValorAtributo("tipo", Tipo.VACIO)
        
    # --------------- 49 -----------------
    elif a == 49.1:

        k = aux.getFromTope(0)
        id = aux.getFromTope(1)
        t = aux.getFromTope(2)
        d = aux.getFromTope(3)
        
        kTipo = k.getValorAtributo("tipo")
        
        idPos = id.getValorAtributo("pos")
        
        tTipo = t.getValorAtributo("tipo")
        tTamanho = t.getValorAtributo("tamanho")
        
        if(kTipo != Tipo.VACIO and kTipo != Tipo.ERROR):
            dTipo=[tTipo]
            for t in kTipo:
                dTipo.append(t)
            d.setValorAtributo("tipo", dTipo)
            
        elif (kTipo != Tipo.ERROR):
            dTipo = [tTipo]
            d.setValorAtributo("tipo", dTipo)
        
        else: 
            d.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(226,f"ERROR SEMÁNTICO - Sentencia incorrecta en la declaración de los parámetros de la función", "") 
        
        gestorTS.insertarTipoTamTS(idPos,tTipo,tTamanho)
        
        kLista = k.getValorAtributo("listaTT")
        if type(kLista) is list:
            for el in kLista:
                gestorTS.insertarTipoTamTS(el[0],el[1],el[2])
        
        aux.pop() # K
        aux.pop() # id
        aux.pop() # T
        
    # --------------- 50 -----------------
    elif a == 50.1:

        d = aux.getFromTope(0)
        
        d.setValorAtributo("tipo", Tipo.VACIO) 
        
    # --------------- 51 -----------------
    elif a == 51.1:

        k1 = aux.getFromTope(0)
        id = aux.getFromTope(1)
        t = aux.getFromTope(2)
        k = aux.getFromTope(4)
        
        k1Tipo = k1.getValorAtributo("tipo")
        
        idPos = id.getValorAtributo("pos")
        
        tTipo = t.getValorAtributo("tipo")
        tTamanho = t.getValorAtributo("tamanho")
        
        if(k1Tipo != Tipo.VACIO and k1Tipo != Tipo.ERROR):
            kTipo=[tTipo]
            for t in k1Tipo:
                kTipo.append(t)
            k.setValorAtributo("tipo", kTipo)
            
        elif (k1Tipo != Tipo.ERROR):
            kTipo = [tTipo]
            k.setValorAtributo("tipo", kTipo)
        
        else:
            k.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(227,f"ERROR SEMÁNTICO - Sentencia incorrecta en la declaración de los parámetros de la función", "") 
        
        lista = []
        lista.append([idPos,tTipo,tTamanho])
        
        k1Lista = k1.getValorAtributo("listaTT")
        if type(k1Lista) is list:
            for el in k1Lista:
                lista.append(el)
        
        k.setValorAtributo("listaTT",lista)   
        
        aux.pop() # K
        aux.pop() # id
        aux.pop() # T
        aux.pop() # coma
        
    # --------------- 52 -----------------
    elif a == 52.1:

        k = aux.getFromTope(0)
        
        k.setValorAtributo("tipo", Tipo.VACIO) 
    
    # ---------------- 53 -----------------
    elif a == 53.1:
        
        b = pila.getFromTope(0)
        
        b.setValorAtributo("funcion", True)
        
    elif a == 53.2:
        
        b = aux.getFromTope(1)
        cprima = aux.getFromTope(0)
        c = aux.getFromTope(2)
        
        bTipo = b.getValorAtributo("tipo")
        cprimaTipo = cprima.getValorAtributo("tipo")
        
        if(bTipo == Tipo.OK and cprimaTipo == Tipo.OK):
            c.setValorAtributo("tipo",Tipo.OK)
        else:
            c.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(228,f"ERROR SEMÁNTICO - Sentencia incorrecta en el cuerpo de la función", "") 
        
        bTipoRet = b.getValorAtributo("tipoRet")
        cprimaTipoRet = cprima.getValorAtributo("tipoRet")
        
        if(bTipoRet != None and bTipoRet != Tipo.ERROR):
            if(cprimaTipoRet == bTipoRet):
                c.setValorAtributo("tipoRet", bTipoRet)
            elif (cprimaTipoRet == None):
                c.setValorAtributo("tipoRet", bTipoRet)
            else:
                c.setValorAtributo("tipoRet", Tipo.ERROR)
                error = Error(229,f"ERROR SEMÁNTICO - Valores de retorno de la función son de un tipo distinto: {getTipoString(bTipoRet)} y {getTipoString(cprimaTipoRet)}", "") 
        
        elif (cprimaTipoRet != None and cprimaTipoRet != Tipo.ERROR):
            c.setValorAtributo("tipoRet", cprimaTipoRet)
        elif (bTipoRet == Tipo.ERROR or cprimaTipoRet == Tipo.ERROR):
            c.setValorAtributo("tipo", Tipo.ERROR)
            error = Error(230,f"ERROR SEMÁNTICO - Expresión de declaración del valor de retorno de la función incorrecta.", "") 
        
        aux.pop() # C'
        aux.pop() # B  

    # ---------------- 54 -----------------
    elif a == 54.1:
        
        b = pila.getFromTope(0)
        
        b.setValorAtributo("funcion", True)
        
    elif a == 54.2:
        
        b = aux.getFromTope(1)
        cprima1 = aux.getFromTope(0)
        cprima = aux.getFromTope(2)
        
        bTipo = b.getValorAtributo("tipo")
        cprima1Tipo = cprima1.getValorAtributo("tipo")
        
        if(bTipo == Tipo.OK and cprima1Tipo == Tipo.OK):
            cprima.setValorAtributo("tipo",Tipo.OK)
        else:
            cprima.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(231,f"ERROR SEMÁNTICO - Sentencia incorrecta en el cuerpo de la función", "") 
        
        bTipoRet = b.getValorAtributo("tipoRet")
        cprima1TipoRet = cprima1.getValorAtributo("tipoRet")
        
        if(bTipoRet != None and bTipoRet != Tipo.ERROR):
            if(cprima1TipoRet == bTipoRet):
                cprima.setValorAtributo("tipoRet", bTipoRet)
            elif (cprima1TipoRet == None):
                cprima.setValorAtributo("tipoRet", bTipoRet)
            else:
                cprima.setValorAtributo("tipoRet", Tipo.ERROR)
                error = Error(232,f"ERROR SEMÁNTICO - Valores de retorno de la función son de un tipo distinto: {getTipoString(bTipoRet)} y {getTipoString(cprima1TipoRet)}", "") 
        
        elif (cprima1TipoRet != None and cprima1TipoRet != Tipo.ERROR):
            cprima.setValorAtributo("tipoRet", cprima1TipoRet)
        elif (bTipoRet == Tipo.ERROR or cprima1TipoRet == Tipo.ERROR):
            cprima.setValorAtributo("tipoRet", Tipo.ERROR)
            error = Error(233,f"ERROR SEMÁNTICO - Expresión de declaración del valor de retorno de la función incorrecta", "") 
        
        
        aux.pop() # C'1
        aux.pop() # B
    
    # ---------------- 55 ------------------
    elif a == 55.1:
        
        cprima = aux.getFromTope(0)
        
        cprima.setValorAtributo("tipo", Tipo.OK)
    
    # --------------- 56 ---------------------
    elif a == 56.1:
        n = aux.getFromTope(0)
        
        n.setValorAtributo("tipo",Tipo.VACIO)
        
        aux.pop() # ptoComa
        
    # ---------------- 57 ----------------------
    elif a == 57.1:
        n = aux.getFromTope(3)
        e = aux.getFromTope(1)
        
        n.setValorAtributo("tipo",e.getValorAtributo("tipo"))
        
        aux.pop() # ptoComa
        aux.pop() # E
        aux.pop() # =
    
    # ---------------- 58 ----------------------
    elif a == 58.1:
        n = aux.getFromTope(3)
        e = aux.getFromTope(1)
        
        eTipo = e.getValorAtributo("tipo")
        
        if(eTipo == Tipo.ENTERO):
            n.setValorAtributo("tipo",eTipo)
        else:
            n.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(234,f"ERROR SEMÁNTICO - La expresión asignada a multiplicar debe ser de tipo entero, sin embargo es de tipo {getTipoString(eTipo)}", "") 
        
        aux.pop() # ptoComa
        aux.pop() # E
        aux.pop() # *=
        
    # ---------------- 59 ------------------------
    elif a == 59.1:
        o = pila.getFromTope(0)
        z = aux.getFromTope(3)
        
        o.setValorAtributo("funcion",z.getValorAtributo("funcion"))
        o.setValorAtributo("switch",z.getValorAtributo("switch"))
        
    elif a == 59.2:
        z1 = pila.getFromTope(0)
        z = aux.getFromTope(4)
        
        z1.setValorAtributo("funcion",z.getValorAtributo("funcion"))
        z1.setValorAtributo("switch",z.getValorAtributo("switch"))
    
    elif a == 59.3:
        o = aux.getFromTope(1)
        z1 = aux.getFromTope(0)
        z = aux.getFromTope(5)
        
        oTipo = o.getValorAtributo("tipo")
        z1Tipo = z1.getValorAtributo("tipo")
        
        if(oTipo == z1Tipo and z1Tipo == Tipo.OK):
            z.setValorAtributo("tipo",Tipo.OK)
        else:
            z.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(235,f"ERROR SEMÁNTICO - Sentencia incorrecta en el cuerpo del CASE", "") 
        
        aux.pop() # Z'
        aux.pop() # O
        aux.pop() # :
        aux.pop() # cteEntera
        aux.pop() # case
    
    # ----------- 60 ------------------
    elif a == 60.1:
        o = pila.getFromTope(0)
        z = aux.getFromTope(2)
        
        o.setValorAtributo("funcion",z.getValorAtributo("funcion"))
    
    elif a == 60.2:
        o = aux.getFromTope(0)
        z = aux.getFromTope(3)
        
        oTipo = o.getValorAtributo("tipo")
        
        if(oTipo == Tipo.OK):
            z.setValorAtributo("tipo",Tipo.OK)
        else:
            z.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(236,f"ERROR SEMÁNTICO - Sentencia incorrecta en el cuerpo del DEFAULT del switch", "") 
        
        aux.pop() # O
        aux.pop() # :
        aux.pop() # default
    
    # ------------- 61 -------------
    elif a == 61.1:
        b = pila.getFromTope(0)
        o = aux.getFromTope(0)
        
        b.setValorAtributo("funcion",o.getValorAtributo("funcion"))
        b.setValorAtributo("switch",o.getValorAtributo("switch"))

    elif a == 61.2:
        oprima = pila.getFromTope(0)
        o = aux.getFromTope(1)
        
        oprima.setValorAtributo("funcion",o.getValorAtributo("funcion"))
        oprima.setValorAtributo("switch",o.getValorAtributo("switch"))
    
    elif a == 61.3:
        o = aux.getFromTope(2)
        oprima = aux.getFromTope(0)
        b = aux.getFromTope(1)
        
        oprimaTipo = oprima.getValorAtributo("tipo")
        bTipo = b.getValorAtributo("tipo")
        
        if(bTipo == oprimaTipo and oprimaTipo == Tipo.OK):
            o.setValorAtributo("tipo",Tipo.OK)
        else:
            o.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(237,f"ERROR SEMÁNTICO - Sentencia incorrecta", "") 
        
        aux.pop() # O'
        aux.pop() # B      
    
    # ------------- 62 -------------
    elif a == 62.1:
        o = aux.getFromTope(0)
        
        o.setValorAtributo("tipo",Tipo.OK)
    
    # ------------- 63 -------------
    elif a == 63.1:
        zprima = aux.getFromTope(1)
        z = aux.getFromTope(0)
        
        z.setValorAtributo("switch",zprima.getValorAtributo("switch"))
        z.setValorAtributo("funcion",zprima.getValorAtributo("funcion"))
        
        zTipo = z.getValorAtributo("tipo")
        
        if(zTipo == Tipo.OK):
            zprima.setValorAtributo("tipo",Tipo.OK)
        else:
            zprima.setValorAtributo("tipo",Tipo.ERROR)
            error = Error(238,f"ERROR SEMÁNTICO - Sentencia incorrecta", "") 
        
        aux.pop() # Z
        
    # ------------- 64 -------------
    elif a == 64.1:
        zprima = aux.getFromTope(0)
        
        zprima.setValorAtributo("tipo",Tipo.OK)
   
    return zona, dec_impl, error      
    