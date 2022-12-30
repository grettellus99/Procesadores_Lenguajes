from analizadorSintactico import AnalizadorSintactico

analizadorSintactico = AnalizadorSintactico()

terminado = None

while(terminado == None):
    terminado = analizadorSintactico.analisisSintactico()

if terminado == False:
    print("Error detectado")
else:
    print("Programa correcto")
