import os.path
class Reader:
    
    ### Constructor del Reader que necesita un path a un archivo ####
    ### Guarda la referencia al archivo abierto si este está disponible ###
    def _init_ (self, f_path):
        self.path=f_path
        self.numLinea=0
        self.numCar=0
        try:
            if(os.path.exists(self.path)):  # el path introducido existe?
                f = open(f_path)    # abrir el archivo
                if(f.readable()):   # permiso de lectura?
                    self.file=f        # atributo file de objeto apunta al archivo abierto
                else:
                    print(f"El fichero {self.path} no tiene permisos de lectura")
            else:
                print(f"El fichero {self.path} no existe")
        except OSError as err:
            print("Error: {0}",format(err))

    ### Devuelve la linea numero numLinea de un archivo
    def readLine():
        f=Reader.file
        linea=""
        i=0
        try:
            while i<Reader.numLinea: 
                linea = f.readline() #leer la lineas hasta llegar a la pedida
                i+=1
            Reader.numLinea +=1
            linea = f.readline() #la linea pedida
        except OSError as err:
            print("Error: {0}",format(err))
        
        return linea #retornar la linea pedida
    
        ### MALLL ###
    def readSigCaracter(endFile):
        endFile=False
        try:
            linea=Reader.readLine() 
        except OSError as err:
            print("Error: {0}",format(err))
        #if()
        c=linea[Reader.numCar]
        if(c=="/0" | c==3 ):
            endFile=True
        
        if(endFile):
            return endFile
        else:
            Reader.numCar+=1
            return c
            
        

              
    
    ## Cierra el fichero
    def close ():
        closed= False
        try:
            Reader.file.close()
            closed=True 
        except OSError as err:
            print("Error: {0}",format(err))
        return closed
    
    
       
    ## Escribe en el fichero
    #def write(texto):

    