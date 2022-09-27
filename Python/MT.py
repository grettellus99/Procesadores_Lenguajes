def MatrizTransicciones(e,c):

    accion=0
    estadoSig=e
    letras =[a_zA_Z]
    
    # S
    if e =="S":
        if c == 104:
            accion = 1
            estadoSig = "A"
        if c == 97:
            accion = 2
            estadoSig = "B"
    

    # A
    if e =="A":
        if c == 111:
            accion = 3
            estadoSig = "C"
        if c == 97:
            accion = 4
            estadoSig = "Otra"

    # B
    # A
    # C
    # D
    # E
    # F
    # G
    # H
    # I
    # J
    # K
    # L
    # M
    # N
    # O
    # P
    # Q
    # R
    # T
    # U
    # V
    # W
    # X
    # Y



    
    return accion,estadoSig, "hola"