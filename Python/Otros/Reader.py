import os.path

class Reader:
    
    ### Constructor del Reader que necesita un path a un archivo ####
    ### Guarda la referencia al archivo abierto si este está disponible ###
    def __init__ (self, f_path):
       
        dirname=os.path.dirname(__file__)
        filename=os.path.join(dirname,f_path)
       
        self.path=filename
        self.numLinea=0
        self.numCar=0
        self.linea=""
        
        try:
            if(os.path.exists(self.path)):  # el path introducido existe?
                f = open(self.path)    # abrir el archivo
                if(f.readable()):   # permiso de lectura?
                    self.file=f        # atributo file de objeto apunta al archivo abierto
                else:
                    print(f"El fichero {self.path} no tiene permisos de lectura")
            else:
                print(f"El fichero {self.path} no existe")
        except OSError as err:
            print("Error: {0}",format(err))

    ### Devuelve la linea numero numLinea de un archivo
    def readLine(self,endFile):
        
        f=self.file
        linea=""
        try:
            linea = f.readline()    # la linea pedida
            self.numLinea +=1     # se leyó una línea
             
            if(linea!=""):
                self.linea = linea    # retornar la linea pedida
            else:
                endFile=True    
            return endFile       

        except OSError as err:
            print("Error: {0}",format(err))
    
    # Devuelve el siguiente caracter. Si se acaba el fichero devuelve False      
    def readSigCaracter(self):
        endFile=False
        i=self.numCar
        l= self.linea
        lengthLine= len(l)
        
        if(i>=lengthLine):
            endFile = self.readLine(endFile)  # si la linea se agotó leer una nueva linea
            if(endFile):
                return False # si la nueva linea es eof devolver false
            self.numCar=0
        
        i=self.numCar
        l= self.linea   
        c=ord(l[i])
        self.numCar+=1    # pos sig caracter
        return c
        
    ## Cierra el fichero
    def close (self):
        closed= False
        try:
            self.file.close()
            closed=True 
        except OSError as err:
            print("Error: {0}",format(err))
        return closed
        
    ## Escribe en el fichero sustituyendo todo si sobreescribir es True
    ## o agregando si sobrescribir es False
    def write(self,texto,sobrescribir):
        self.file.close()
        try:
            if(sobrescribir): 
                # "w" permite sobrescribir todo
                f=open(self.path,"w")
                self.file=f
                f.write(texto)
                f.write('\n')       
            else:
                # "a" permite agregar una linea al final
                f=open(self.path,"a")
                self.file=f
                f.write(texto)
                f.write('\n')   
        except OSError as err:
            print("Error: {0}",format(err))
