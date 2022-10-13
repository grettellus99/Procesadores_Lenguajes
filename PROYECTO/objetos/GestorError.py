# Definir una clase error
class Error():
    def __init__ (self,cod,mensaje,linea):
        self.codigo=cod
        self.mensaje=mensaje
        self.linea=linea
        