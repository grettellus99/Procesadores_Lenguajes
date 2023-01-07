from analizadorSintactico import AnalizadorSintactico


class AnalizadorSemantico():
    def __init__(self):
        self.analizadorSintactico = AnalizadorSintactico()
        self.terminado = None


    def analisisSemantico(self):
        while(self.terminado == None):
            self.terminado = self.analizadorSintactico.analisisSintactico()

        if self.terminado == False:
            print("Error detectado")
        else:
            print("Programa correcto")
