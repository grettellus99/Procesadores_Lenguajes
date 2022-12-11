from analizadorSintactico import AnalizadorSintactico

analizadorSintactico = AnalizadorSintactico()

terminado = False


while(terminado == False):
    terminado = analizadorSintactico.analisisSintactico()


