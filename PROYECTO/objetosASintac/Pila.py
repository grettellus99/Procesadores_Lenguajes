
class Pila():
    def __init__(self):
         self.pila = []
    
    def append(self, t):
        self.pila.append(t)
        
    def pop(self):
        if len(self.pila) > 0:
            return self.pila.pop()
        return False    
    
    def equipara(self,sim):
        elemPila= self.pop()
        if(sim==elemPila):
            return True
        else:
            return False
    
    def getFromTope(self,pos):
        tope = len(self.pila) - 1  # ultima pos de la pila
        return self.pila[tope - pos]