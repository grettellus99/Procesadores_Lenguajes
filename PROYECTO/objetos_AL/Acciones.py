
from objetos_AL.datos import *
from GestorError import Error



#-----------------ACCIONES SEMANTICAS--------------------
def accionesSemanticas (a,ctr,listaTokens,tabla):
    global lexema       # para tokens de tipo palabra reservada, cadena e identidicador 
    global valor        # para tokens de tipo constante entera
    #global listaTokens  # lista de tokens para guardar los tokens una vez se creen
    leer=False  # saber si se necesita leer el próximo carácter
    error=False
    
    c=chr(ctr)
    
    if a == 0:
        print("Alcanzado estado final")   # no es una accion válida
    elif a == 1:
        leer=True   # debe leerse el próximo carácter
    
    elif a == 2:
        lexema= c
        leer=True   # debe leerse el próximo carácter
    
    elif a == 3:     
        lexema= lexema + c
        leer=True   # debe leerse el próximo carácter
    
    elif a == 4:
        if lexema in palabrasReservadas:
            listaTokens.addTokenPalabraReservada(lexema)    # agrega token de tipo palabra reservada a la lista y el fichero
        else:          
                resul = tabla.buscarLugarTSNombre(lexema)
                pos=resul[0]
                insertar=resul[1]
                if(insertar==False):
                    listaTokens.addTokenIdentificador(pos) # agrega token id a la lista y el fichero
                else:  # si no devuelve False lo encontró
                    pos = tabla.insertarValor(lexema)
                    listaTokens.addTokenIdentificador(pos)
                    print(f"No se ha encontrado el identificador {lexema}, se inserta en la pos: {pos}")     
        
    elif a == 5:
        valor = int(c) 
        leer=True      # debe leerse el próximo carácter
    
    elif a == 6:
        valor= valor*10 + int(c)
        leer=True      # debe leerse el próximo carácter
    
    elif a == 7:
        if (valor > 32767):
            print("ERROR")
            # Crear un objeto Error con el mensaje específico para devolverlo como valor de retorno 
            error=Error(60,f"ERROR LÉXICO - El número introducido está fuera de rango.\n\t NUM: {valor} es mayor que 32767.", "")         
        else:
            listaTokens.addTokenConstEntera(valor) # agrega token cteEntera a la lista y el fichero

    elif a == 8 or a == 9 or a == 10 or a == 11 or a == 12 or a == 13 or a == 14:    # acciones correspondientes a comentarios
        print("LEER")
        leer=True      # debe leerse el próximo carácter   
    
    elif a == 15:
        lexema= ""
        leer=True      # debe leerse el próximo carácter   
    
    elif a == 16:
        lexema= lexema + c
        leer=True      # debe leerse el próximo carácter   
    
    elif a == 17:
        if len(lexema) > 64:
            print("ERROR")
             # Crear un objeto Error con el mensaje específico para devolverlo como valor de retorno 
            error=Error(61,f"ERROR LÉXICO - La cadena introducida tiene más del número máximo de caracteres permitidos: 64. \n\t CAD: '{lexema}'.", "")
        else:
            listaTokens.addTokenCadena(lexema) # agrega token cadena a la lista y el fichero

    elif a == 18:
        leer=True      # debe leerse el próximo carácter 
    
    elif a == 19:
        listaTokens.addTokenOperadoresSignos("opRelacional", 1)   # agrega token operador relacional a la lista y el fichero
   
    elif a == 20:
        listaTokens.addTokenOperadoresSignos("asignacion", " ")   # agrega token operador asignación a la lista y el fichero
   
    elif a == 21:
        leer=True      # debe leerse el próximo carácter
    
    elif a == 22:
        listaTokens.addTokenOperadoresSignos("asigMultiplicacion", " ")   # agrega token operador asignación a la lista y el fichero
   
    elif a == 23:
        listaTokens.addTokenOperadoresSignos("opAritmetico",1)   # agrega token operador aritmético a la lista y el fichero
   
    elif a == 24:
        leer=True      # debe leerse el próximo carácter
        
    elif a == 25:
        listaTokens.addTokenOperadoresSignos("opLogico",1)   # agrega token operador lógico a la lista y el fichero

    elif a == 26:
        listaTokens.addTokenOperadoresSignos("abrirParentesis"," ")   # agrega token abrir paréntesis a la lista y el fichero
        
    elif a == 27:
        listaTokens.addTokenOperadoresSignos("cerrarParentesis"," ")   # agrega token cerrar paréntesis a la lista y el fichero
        
    elif a == 28:
        listaTokens.addTokenOperadoresSignos("abrirCorchete"," ")   # agrega token abrir corchete a la lista y el fichero
       
    elif a == 29:
        listaTokens.addTokenOperadoresSignos("cerrarCorchete"," ")   # agrega token cerrar corchete a la lista y el fichero
      
    elif a == 30:
        listaTokens.addTokenOperadoresSignos("ptoComa"," ")   # agrega token punto y coma a la lista y el fichero
      
    elif a == 31:
        listaTokens.addTokenOperadoresSignos("coma"," ")   # agrega token coma a la lista y el fichero
      
    elif a == 32:
        listaTokens.addTokenOperadoresSignos("dosPuntos"," ")   # agrega token dosPuntos a la lista y el fichero
      
    elif a == 33:
        listaTokens.addTokenOperadoresSignos("opAritmetico",2)   # agrega token operador aritmético 2 a la lista y el fichero
      
    else:
        print("Acción no válida")
    
    return leer, error