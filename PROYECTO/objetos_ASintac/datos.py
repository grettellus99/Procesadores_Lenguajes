#------- Simbolos No Terminales -------------
noTerminales = ["A","B","S","S'","E","E'","R","R'","U","U'","V","V'","P","P'","L","Q","X","T","F","H","D","K","C","N","Z","O","O'"]

# --------- FIRST Y FOLLOW --------------------

#----------- A -------------
firstA1 = ["if", "let","switch","id","print","input","return"]
firstA2 = ["function"]
firstA3 = ["eof"]

followA = ["eof"]

#----------- B -------------
firstB1 = ["if"]
firstB2 = ["let"]
firstB3 = ["id","print","input","return"]
firstB4 = ["switch"]

followB = ["if", "let","switch","id","print","input","return", "function", "eof", "cerrarParentesis","break","case","default"]

#---------- S ------------------
firstS1 = ["id"]
firstS2 = ["print"]
firstS3 = ["input"]
firstS4 = ["return"]

followS = [] + followB

#--------- S' ------------------
firstSprima1 = ["asignacion"]
firstSprima2 = ["asigMultiplicacion"]
firstSprima3 = ["abrirParentesis"]

followSprima = ["ptoComa"]

#--------- E --------------------

firstE1 = ["id","abrirParentesis","cteEntera","cadena","true","false"]

followE = ["cerrarParentesis","ptoComa","coma"]

#--------- E' ---------------------

firstEprima2 = ["opLogico1"]

followEprima = [] + followE

#--------- R ---------------------

firstR1 = ["id","abrirParentesis","cteEntera","cadena","true","false"]

followR = ["opLogico1"] + followE

#--------- R' --------------------

firstRprima2 = ["opRelacional1"]

followRprima = [] + followR

#-------- U -------------------

firstU1 = ["id","abrirParentesis","cteEntera","cadena","true","false"]

followU = ["opRelacional1"] + followR

#-------- U' -------------------

firstUprima2 = ["opAritmetico2"]

followUprima = [] + followU

#-------- V -------------------

firstV1 = ["id","abrirParentesis","cteEntera","cadena","true","false"]

followV = ["opAritmetico2"] + followU

#-------- V' -------------------

firstVprima2 = ["opAritmetico1"]

followVprima = [] + followV

#--------- P --------------------

firstP1 = ["id"]
firstP2 = ["abrirParentesis"]
firstP3 = ["cteEntera"]
firstP4 = ["cadena"]
firstP5 = ["true"]
firstP6 = ["false"]

followP = ["opAritmetico1"] + followV

#--------- P' --------------------

firstPprima2 = ["abrirParentesis"]

followPprima = [] +  followP

#---------- L --------------------

firstL1 = ["id","abrirParentesis","cteEntera","cadena","true","false"]

followL = ["cerrarParentesis"]

#---------- Q --------------------

firstQ1 = ["coma"]

followQ = [] + followL

#---------- X --------------------

firstX1 = ["id","abrirParentesis","cteEntera","cadena","true","false"]

followX = ["ptoComa"]

#---------- T --------------------

firstT1 = ["int"]

firstT2 = ["boolean"]

firstT3 = ["string"]

followT = ["id", "cerrarParentesis", "ptoComa", "asignacion", "asigMultiplicacion"]

#---------- F --------------------

firstF1 = ["function"]

followF = ["if", "let", "switch", "id", "print", "input", "return", "function", "eof"]

#---------- H --------------------

firstH1 = ["int", "boolean", "string"]

followH = ["abrirParentesis"]

#---------- D --------------------

firstD1 = ["int", "boolean", "string"]

followD = ["cerrarParentesis"]

#---------- K --------------------

firstK1 = ["coma"]

followK = [] + followD

#---------- C --------------------

firstC1 = ["if", "let", "switch", "id", "print", "input", "return"]

followC = ["cerrarCorchete"]

#---------- N --------------------

firstN1 = ["ptoComa"] 

firstN2 = ["asignacion"] 

firstN3 = ["asigMultiplicacion"]

followN = ["if", "let","switch","id","print","input","return", "function", "eof", "cerrarParentesis","break","case","default"]

#---------- Z --------------------

firstZ1 = ["case"]

firstZ2 = ["default"]

followZ= ["cerrarCorchete"]

#---------- O --------------------

firstO1 = ["if", "let", "switch", "id", "print", "input", "return"]

firstO2 = ["break"]

followO = ["case", "default"] + followZ

#---------- O' --------------------

firstOprima1 = ["if", "let", "switch", "id", "print", "input", "return"]

firstOprima2 = ["break"]

followOprima = [] + followO

