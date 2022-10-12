#-----------------ACCIONES SEMANTICAS--------------------
def accionesSemanticas (a,ctr):
    global lexema
    global valor
    global listaTokens

    c=chr(ctr)

    if a == 0:
        print("La acción 0 no es válida") 
    elif a == 1:
        print("leer")
    elif a == 2:
        lexema= c
    elif a == 3:     
        lexema= lexema + c
    elif a == 4:
        #POR HACER
        if lexema in palabrasReservadas:
            token = Token(lexema, "-")
            listaTokens.append(token)
        else: 
            try:
                lugar = buscarLugarTSNombre(lexema)
                token = Token(lexema, lugar)
                listaTokens.append(token)
            except:
                print("No se ha encontrado, se inserta en la pos:",len(TablaSimbolos) )
                entrada3 = EntradasTablaSimbolos()
                entrada3.setValores(len(TablaSimbolos),"z", "holaMundo")
                TablaSimbolos.append(entrada3)
                lugar = entrada3.pos

        
    elif a == 5:
        valor = int(c) 
    elif a == 6:
        valor= (int(valor) * 10) + int(c)
    elif a == 7:
        if int(valor) > 32767:
            print("ERROR")
        else:
            
            token = Token("cteEntera", int(valor))
            listaTokens.append(token)

    elif a == 8:
        pass
    elif a == 9:
        lexema= "" 
    elif a == 10:
        lexema= lexema + c
    elif a == 11:
        if len(lexema) > 64:
            print("ERROR")
        else:
            token = Token("cadena", lexema)
            listaTokens.append(token)
    elif a == 12:
        pass
    elif a == 13:
        token = Token("asignacion", "-")
        listaTokens.append(token)
    elif a == 14:
        token = Token("opRelacional", 1)
        listaTokens.append(token)
    elif a == 15:
        pass
    elif a == 16:
        token = Token("asigMultiplicacion", "-")
        listaTokens.append(token)
    elif a == 17:
        token = Token("opAritmetico",1)
        listaTokens.append(token)
    elif a == 18:
        print("leer")
    elif a == 19:
        token = Token("opLogico",1)
        listaTokens.append(token)
    
    elif a == 20:
        token = Token("abrirParantesis","-")
        listaTokens.append(token)
        
    elif a == 21:
        token = Token("cerrarParantesis","-")
        listaTokens.append(token)
    elif a == 22:
        token = Token("abrirCorchete","-")
        listaTokens.append(token)
    elif a == 23:
        token = Token("cerrarCorchete","-")
        listaTokens.append(token)
    elif a == 24:
        token = Token("ptoComa","-")
        listaTokens.append(token)
    elif a == 25:
        token = Token("coma","-")
        listaTokens.append(token)
    elif a == 26:
        token = Token("opAritmetico",2)
        listaTokens.append(token)
    elif a == 27:
        token = Token("dosPuntos","-")
        listaTokens.append(token)
    else:
        ("Acción no valida")