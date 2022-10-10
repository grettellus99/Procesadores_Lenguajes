
## NO TERMINADO ##
def fileReader (despLinea):
    f = open("../Ficheros Fuente/fichero_fuente.txt")

    linea="";
    i=0
    while i<despLinea:
        linea = f.readline()
        i+=1
    
    linea = f.readline()
    f.close()
    return linea

