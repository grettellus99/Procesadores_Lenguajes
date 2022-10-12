
from Reader import Reader

r=Reader("../Ficheros Fuente/fichero_fuente.txt")


while(True):
    c = r.readSigCaracter()
    if(c==False):
        break;
    print(c)
   
r.close()

w=Reader("../Ficheros Salida/tokens.txt")

w.write("<hola,->",True)
w.write("<hola2,->",False)

w.close()